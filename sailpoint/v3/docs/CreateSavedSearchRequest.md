# CreateSavedSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the saved search.  | [optional] 
**description** | **str** | The description of the saved search.  | [optional] 
**created** | **datetime** | A date-time in ISO-8601 format | [optional] 
**modified** | **datetime** | A date-time in ISO-8601 format | [optional] 
**indices** | [**List[Index]**](Index.md) | The names of the Elasticsearch indices in which to search.  | 
**columns** | **Dict[str, List[Column]]** | The columns to be returned (specifies the order in which they will be presented) for each document type.  The currently supported document types are: _accessprofile_, _accountactivity_, _account_, _aggregation_, _entitlement_, _event_, _identity_, and _role_.  | [optional] 
**query** | **str** | The search query using Elasticsearch [Query String Query](https://www.elastic.co/guide/en/elasticsearch/reference/5.2/query-dsl-query-string-query.html#query-string) syntax from the Query DSL.  | 
**fields** | **List[str]** | The fields to be searched against in a multi-field query.  | [optional] 
**order_by** | **Dict[str, List[str]]** | Sort by index. This takes precedence over the &#x60;sort&#x60; property.  | [optional] 
**sort** | **List[str]** | The fields to be used to sort the search results.  | [optional] 
**filters** | [**SavedSearchDetailFilters**](SavedSearchDetailFilters.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.create_saved_search_request import CreateSavedSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSavedSearchRequest from a JSON string
create_saved_search_request_instance = CreateSavedSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSavedSearchRequest.to_json())

# convert the object into a dict
create_saved_search_request_dict = create_saved_search_request_instance.to_dict()
# create an instance of CreateSavedSearchRequest from a dict
create_saved_search_request_from_dict = CreateSavedSearchRequest.from_dict(create_saved_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


