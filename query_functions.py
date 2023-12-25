''' 
make query function!!
'''
def prefixes():
  return('PREFIX cdm: <http://publications.europa.eu/ontology/cdm#> ')

def select_query():
  return('SELECT DISTINCT ?work ?type ?celex ')

def where_query(doc_type,filter=False,filter_type=''):
  where_start = 'WHERE { ?work cdm:work_has_resource-type <http://publications.europa.eu/resource/authority/resource-type/%s> ' % doc_type
  if filter:
    if filter == "starts_with":
      filter = 'strStarts( ?celex, "%s" )' %filter_type
    elif filter == "contains":
      filter = 'filter contains(?celex,"%s") ' % filter_type
    return where_start + filter
  else:
    return where_start



print(where_query("DEC","starts_with",'6'))

def query(doc_type,filter=False,filter_type=' ',limit=0):
  """Function that creates SPARQL queries

    Args:
        doc_type: string. type of document such as DEC or JUDG; Refer to https://michalovadek.github.io/eurlex/articles/eurlexpkg.html
        filter: string; either "starts_with" or "contains"
        filter_type: string. CO, CJ etc... refer to https://eur-lex.europa.eu/content/tools/TableOfSectors/types_of_documents_in_eurlex.html
        limit: integer. The maximum number of documents to extract

    Returns:
        A SPARQL query
  """
  prefix = prefixes()
  select = select_query()
  where = where_query(doc_type,filter,filter_type)
  query = prefix + select + where
  return( query + 'OPTIONAL{?work cdm:resource_legal_id_celex ?celex.}} LIMIT %s  ' % str(limit))
