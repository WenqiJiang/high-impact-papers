# Download DBLP database

We can download DBLP papers in json/xml format.

For example, search OSDI: https://dblp.org/search?q=OSDI

Click the download button near the *Publication search results* entry, and select json.

Copy the content to the dblp_json folder as a json file.

## Example Load

```
import json

data = []
fname = 'dblp_json/OSDI.json'
with open(fname, 'r') as f:
    json_list = json.load(f)

papers = json_list['result']['hits']['hit']
print("length of the file: {}".format(len(paper_list)))
```

Example paper:

```
>>> papers[0]
{'@score': '2', '@id': '372466', 'info': {'authors': {'author': [{'@pid': '10/553', 'text': 'Marcos K. Aguilera'}, {'@pid': 'w/HakimWeatherspoon', 'text': 'Hakim Weatherspoon'}]}, 'title': '16th USENIX Symposium on Operating Systems Design and Implementation, OSDI 2022, Carlsbad, CA, USA, July 11-13, 2022', 'venue': 'OSDI', 'publisher': 'USENIX Association', 'year': '2022', 'type': 'Editorship', 'access': 'open', 'key': 'conf/osdi/2022', 'ee': 'https://www.usenix.org/conference/osdi22', 'url': 'https://dblp.org/rec/conf/osdi/2022'}, 'url': 'URL#372466'}
```

Get the title and year :

```
>>> papers[105]['info']['title']
'Virtual Consensus in Delos.'
>>> papers[105]['info']['year']
'2020'
```

