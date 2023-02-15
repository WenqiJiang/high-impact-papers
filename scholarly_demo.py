"""
Github: https://github.com/scholarly-python-package/scholarly

Documentation: https://scholarly.readthedocs.io/en/latest/?badge=latest
"""

from scholarly import scholarly


""" Search an author """

# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
search_query = scholarly.search_author('Wenqi Jiang')
# Retrieve the first result from the iterator
first_author_result = next(search_query)
scholarly.pprint(first_author_result)

# Retrieve all the details for the author
author = scholarly.fill(first_author_result )
scholarly.pprint(author)

# Take a closer look at the first publication
first_publication = author['publications'][0]
first_publication_filled = scholarly.fill(first_publication)
scholarly.pprint(first_publication_filled)

# Print the titles of the author's publications
publication_titles = [pub['bib']['title'] for pub in author['publications']]
print(publication_titles)

# Which papers cited that publication?
citations = [citation['bib']['title'] for citation in scholarly.citedby(first_publication_filled)]
print(citations)


""" Search a publication """
search_query = scholarly.search_pubs('Microsecond Consensus for Microsecond Applications')
result = next(search_query)
print(result)
print(result['num_citations'])
