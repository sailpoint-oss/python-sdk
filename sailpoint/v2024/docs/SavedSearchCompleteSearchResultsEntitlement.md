# SavedSearchCompleteSearchResultsEntitlement

A table of entitlements that match the search criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **str** | The number of rows in the table. | 
**noun** | **str** | The type of object represented in the table. | 
**preview** | **List[List[str]]** | A sample of the data in the table. | 

## Example

```python
from sailpoint.v2024.models.saved_search_complete_search_results_entitlement import SavedSearchCompleteSearchResultsEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSearchCompleteSearchResultsEntitlement from a JSON string
saved_search_complete_search_results_entitlement_instance = SavedSearchCompleteSearchResultsEntitlement.from_json(json)
# print the JSON string representation of the object
print(SavedSearchCompleteSearchResultsEntitlement.to_json())

# convert the object into a dict
saved_search_complete_search_results_entitlement_dict = saved_search_complete_search_results_entitlement_instance.to_dict()
# create an instance of SavedSearchCompleteSearchResultsEntitlement from a dict
saved_search_complete_search_results_entitlement_from_dict = SavedSearchCompleteSearchResultsEntitlement.from_dict(saved_search_complete_search_results_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


