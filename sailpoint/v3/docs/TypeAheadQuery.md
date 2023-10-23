# TypeAheadQuery

Query parameters used to construct an Elasticsearch type ahead query object.  The typeAheadQuery performs a search for top values beginning with the typed values. For example, typing \"Jo\" results in top hits matching \"Jo.\" Typing \"Job\" results in top hits matching \"Job.\" 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The type ahead query string used to construct a phrase prefix match query. | 
**field** | **str** | The field on which to perform the type ahead search. | 
**nested_type** | **str** | The nested type. | [optional] 
**max_expansions** | **int** | The number of suffixes the last term will be expanded into. Influences the performance of the query and the number results returned. Valid values: 1 to 1000. | [optional] [default to 10]
**size** | **int** | The max amount of records the search will return. | [optional] [default to 100]
**sort** | **str** | The sort order of the returned records. | [optional] [default to 'desc']
**sort_by_value** | **bool** | The flag that defines the sort type, by count or value. | [optional] [default to False]

## Example

```python
from v3.models.type_ahead_query import TypeAheadQuery

# TODO update the JSON string below
json = "{}"
# create an instance of TypeAheadQuery from a JSON string
type_ahead_query_instance = TypeAheadQuery.from_json(json)
# print the JSON string representation of the object
print TypeAheadQuery.to_json()

# convert the object into a dict
type_ahead_query_dict = type_ahead_query_instance.to_dict()
# create an instance of TypeAheadQuery from a dict
type_ahead_query_form_dict = type_ahead_query.from_dict(type_ahead_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


