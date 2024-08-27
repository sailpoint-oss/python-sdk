# SavedSearchDetailFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FilterType**](FilterType.md) |  | [optional] 
**range** | [**Range**](Range.md) |  | [optional] 
**terms** | **List[str]** | The terms to be filtered. | [optional] 
**exclude** | **bool** | Indicates if the filter excludes results. | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.saved_search_detail_filters import SavedSearchDetailFilters

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSearchDetailFilters from a JSON string
saved_search_detail_filters_instance = SavedSearchDetailFilters.from_json(json)
# print the JSON string representation of the object
print(SavedSearchDetailFilters.to_json())

# convert the object into a dict
saved_search_detail_filters_dict = saved_search_detail_filters_instance.to_dict()
# create an instance of SavedSearchDetailFilters from a dict
saved_search_detail_filters_from_dict = SavedSearchDetailFilters.from_dict(saved_search_detail_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


