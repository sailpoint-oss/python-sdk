# ScheduledSearchName


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the scheduled search.  | [optional] 
**description** | **str** | The description of the scheduled search.  | [optional] 

## Example

```python
from v3.models.scheduled_search_name import ScheduledSearchName

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledSearchName from a JSON string
scheduled_search_name_instance = ScheduledSearchName.from_json(json)
# print the JSON string representation of the object
print ScheduledSearchName.to_json()

# convert the object into a dict
scheduled_search_name_dict = scheduled_search_name_instance.to_dict()
# create an instance of ScheduledSearchName from a dict
scheduled_search_name_form_dict = scheduled_search_name.from_dict(scheduled_search_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


