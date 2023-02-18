"""
Return papers that has at least min(cite_per_year * years, max_citation_threshold) citations

Example usage:

python3 print_high_impact_papers.py --citation_json_path 'citation_json/OSDI.json' --cite_per_year 30 --max_citation_threshold 500 > high_impact_papers/OSDI_high_impact_papers
python3 print_high_impact_papers.py --citation_json_path 'citation_json/SOSP.json' --cite_per_year 30 --max_citation_threshold 500 > high_impact_papers/SOSP_high_impact_papers
python3 print_high_impact_papers.py --citation_json_path 'citation_json/SIGMOD.json' --cite_per_year 30 --max_citation_threshold 500 > high_impact_papers/SIGMOD_high_impact_papers

Input json format:
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
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--citation_json_path', type=str, help="(output) path of the output citation json file, e.g., 'citation_json_path/OSDI.json'")
parser.add_argument('--cite_per_year', type=int, default=30, help="return papers that ")
parser.add_argument('--max_citation_threshold', type=int, default=500, help="all papers having this citation, regardless of year of publication, will be returned")

args = parser.parse_args()
citation_json_path = args.citation_json_path
cite_per_year = args.cite_per_year
max_citation_threshold = args.max_citation_threshold


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

def get_paper_list_from_citation_json_path(citation_json_path):
  """
  return a list of json (dict) objects, each is a paper
  """

  papers = None
  with open(citation_json_path, 'r') as f:
      papers = json.load(f)

  return papers

if __name__ == '__main__':

    papers = get_paper_list_from_citation_json_path(citation_json_path)

    high_impact_papers = dict()

    for title in papers:

        citation_until = int(papers[title]['citation_until']) # year of checking citation on Google scholar
        year = int(papers[title]['year']) # publication year
        citation = papers[title]['citation']

        min_publication = np.min([np.max([cite_per_year * (citation_until - year), cite_per_year]), max_citation_threshold])
        if citation >= min_publication:
            if year != citation_until:
                papers[title]['citation_per_year'] = citation / (citation_until - year)
            else:
                papers[title]['citation_per_year'] = citation
            high_impact_papers[title] = papers[title]

    for title in high_impact_papers:
        year = high_impact_papers[title]['year'] # publication year
        citation = high_impact_papers[title]['citation']
        citation_per_year = high_impact_papers[title]['citation_per_year']
        print("Paper: {}\tYear: {}\tCitation: {}\tCitation per year: {}".format(title, year, citation, citation_per_year))


