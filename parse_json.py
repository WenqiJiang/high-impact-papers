import json

data = []
fname = 'dblp_json/OSDI.json'
with open(fname, 'r') as f:
    json_list = json.load(f)


papers = json_list['result']['hits']['hit']
print("length of the file: {}".format(len(paper_list)))

print(papers[0]['info']['title'])
print(papers[0]['info']['year'])