# SavedSearchCompleteSearchResults

A preview of the search results for each object type. This includes a count as well as headers, and the first several rows of data, per object type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**SavedSearchCompleteSearchResultsAccount**](SavedSearchCompleteSearchResultsAccount.md) |  | [optional] 
**entitlement** | [**SavedSearchCompleteSearchResultsEntitlement**](SavedSearchCompleteSearchResultsEntitlement.md) |  | [optional] 
**identity** | [**SavedSearchCompleteSearchResultsIdentity**](SavedSearchCompleteSearchResultsIdentity.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.saved_search_complete_search_results import SavedSearchCompleteSearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSearchCompleteSearchResults from a JSON string
saved_search_complete_search_results_instance = SavedSearchCompleteSearchResults.from_json(json)
# print the JSON string representation of the object
print SavedSearchCompleteSearchResults.to_json()

# convert the object into a dict
saved_search_complete_search_results_dict = saved_search_complete_search_results_instance.to_dict()
# create an instance of SavedSearchCompleteSearchResults from a dict
saved_search_complete_search_results_form_dict = saved_search_complete_search_results.from_dict(saved_search_complete_search_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


