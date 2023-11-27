# SavedSearchName


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the saved search.  | [optional] 
**description** | **str** | The description of the saved search.  | [optional] 

## Example

```python
from sailpoint.v3.models.saved_search_name import SavedSearchName

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSearchName from a JSON string
saved_search_name_instance = SavedSearchName.from_json(json)
# print the JSON string representation of the object
print SavedSearchName.to_json()

# convert the object into a dict
saved_search_name_dict = saved_search_name_instance.to_dict()
# create an instance of SavedSearchName from a dict
saved_search_name_form_dict = saved_search_name.from_dict(saved_search_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


