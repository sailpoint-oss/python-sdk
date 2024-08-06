# InnerHit

Inner Hit query object that will cause the specified nested type to be returned as the result matching the supplied query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The search query using the Elasticsearch [Query String Query](https://www.elastic.co/guide/en/elasticsearch/reference/5.2/query-dsl-query-string-query.html#query-string) syntax from the Query DSL extended by SailPoint to support Nested queries. | 
**type** | **str** | The nested type to use in the inner hits query.  The nested type [Nested Type](https://www.elastic.co/guide/en/elasticsearch/reference/current/nested.html) refers to a document \&quot;nested\&quot; within another document. For example, an identity can have nested documents for access, accounts, and apps. | 

## Example

```python
from sailpoint.v2024.models.inner_hit import InnerHit

# TODO update the JSON string below
json = "{}"
# create an instance of InnerHit from a JSON string
inner_hit_instance = InnerHit.from_json(json)
# print the JSON string representation of the object
print InnerHit.to_json()

# convert the object into a dict
inner_hit_dict = inner_hit_instance.to_dict()
# create an instance of InnerHit from a dict
inner_hit_form_dict = inner_hit.from_dict(inner_hit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


