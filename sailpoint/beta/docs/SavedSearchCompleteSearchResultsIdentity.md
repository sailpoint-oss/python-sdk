# SavedSearchCompleteSearchResultsIdentity

A table of identities that match the search criteria.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **str** | The number of rows in the table. | 
**noun** | **str** | The type of object represented in the table. | 
**preview** | **List[List[str]]** | A sample of the data in the table. | 

## Example

```python
from sailpoint.beta.models.saved_search_complete_search_results_identity import SavedSearchCompleteSearchResultsIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSearchCompleteSearchResultsIdentity from a JSON string
saved_search_complete_search_results_identity_instance = SavedSearchCompleteSearchResultsIdentity.from_json(json)
# print the JSON string representation of the object
print SavedSearchCompleteSearchResultsIdentity.to_json()

# convert the object into a dict
saved_search_complete_search_results_identity_dict = saved_search_complete_search_results_identity_instance.to_dict()
# create an instance of SavedSearchCompleteSearchResultsIdentity from a dict
saved_search_complete_search_results_identity_form_dict = saved_search_complete_search_results_identity.from_dict(saved_search_complete_search_results_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


