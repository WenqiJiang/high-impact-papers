"""
Example usage:

python3 get_paper_citation_from_json.py --dblp_json_path 'dblp_json/OSDI.json' --citation_json_path 'citation_json/OSDI.json' --sleep_sec 2

Out json format:
{
    paper_title_0: {'year': 2011, 'citation': 123, 'citation_until': 2023}
    paper_title_1: {'year': 2018, 'citation': 321, 'citation_until': 2023}
    ...
}
"""

import argparse 
import json
import os
import time
from scholarly import scholarly

parser = argparse.ArgumentParser()
parser.add_argument('--dblp_json_path', type=str, help="(input) path of the input dblp json file, e.g., 'dblp_json_path/OSDI.json'")
parser.add_argument('--citation_json_path', type=str, help="(output) path of the output citation json file, e.g., 'citation_json_path/OSDI.json'")
parser.add_argument('--sleep_sec', type=float, default=1.0, help="sleep between search, such that Google will not ban us")
parser.add_argument('--since_year', type=int, default=2010, help="only count papers after this year")
parser.add_argument('--current_year', type=int, default=2023, help="current year")

args = parser.parse_args()
dblp_json_path = args.dblp_json_path
citation_json_path = args.citation_json_path
sleep_sec = args.sleep_sec
current_year = args.current_year
since_year = args.since_year

print("Warning: make sure to use proxy before running the script, otherwise the IP might be banned by Google!")
print("Current year: {}".format(current_year))
print("Counting paper since year: {}".format(since_year))

def get_citation_count(paper_title):
    """
    Get the citation count given a paper
    """
    search_query = scholarly.search_pubs(paper_title)
    try:
        result = next(search_query)
        return result['num_citations']
    except:
        return 0

def get_paper_list_from_dblp_json_path(dblp_json_path_path):
  """
  return a list of json (dict) objects, each is a paper
  """

  with open(dblp_json_path_path, 'r') as f:
      json_list = json.load(f)

  papers = json_list['result']['hits']['hit']
  return papers

if __name__ == '__main__':

    papers = get_paper_list_from_dblp_json_path(dblp_json_path)

    citation_json = dict()
    if os.path.exists(citation_json_path):
        with open(citation_json_path, 'r') as f:
            citation_json = json.load(f)

    for paper in papers:
        title = paper['info']['title']
        year = paper['info']['year']
        if int(year) <= since_year:
            continue
        if title not in citation_json:
            citation = get_citation_count(title)
            print("Paper:{}\tYear:{}\tCitation:{}".format(title, year, citation))
            citation_json[title] = {'year': year, 'citation': citation, 'citation_until': current_year}
            time.sleep(sleep_sec)
            with open(citation_json_path, 'w') as f:
                json.dump(citation_json, f)
        else:
            print("Skip... Paper {} already in dict (Year:{}\tCitation:{})".format(title, citation_json[title]['year'], citation_json[title]['citation']))


