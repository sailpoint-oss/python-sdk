# Query

Query parameters used to construct an Elasticsearch query object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The query using the Elasticsearch [Query String Query](https://www.elastic.co/guide/en/elasticsearch/reference/5.2/query-dsl-query-string-query.html#query-string) syntax from the Query DSL extended by SailPoint to support Nested queries. | [optional] 
**fields** | **str** | The fields the query will be applied to.  Fields provide you with a simple way to add additional fields to search, without making the query too complicated.  For example, you can use the fields to specify that you want your query of \&quot;a*\&quot; to be applied to \&quot;name\&quot;, \&quot;firstName\&quot;, and the \&quot;source.name\&quot;.  The response will include all results matching the \&quot;a*\&quot; query found in those three fields.  A field&#39;s availability depends on the indices being searched.  For example, if you are searching \&quot;identities\&quot;, you can apply your search to the \&quot;firstName\&quot; field, but you couldn&#39;t use \&quot;firstName\&quot; with a search on \&quot;access profiles\&quot;.  Refer to the response schema for the respective lists of available fields.  | [optional] 
**time_zone** | **str** | The time zone to be applied to any range query related to dates. | [optional] 
**inner_hit** | [**InnerHit**](InnerHit.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.query import Query

# TODO update the JSON string below
json = "{}"
# create an instance of Query from a JSON string
query_instance = Query.from_json(json)
# print the JSON string representation of the object
print Query.to_json()

# convert the object into a dict
query_dict = query_instance.to_dict()
# create an instance of Query from a dict
query_form_dict = query.from_dict(query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


