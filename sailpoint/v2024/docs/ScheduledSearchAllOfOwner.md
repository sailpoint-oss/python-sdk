# ScheduledSearchAllOfOwner

The owner of the scheduled search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | 
**id** | **str** | The ID of the referenced object | 

## Example

```python
from sailpoint.v2024.models.scheduled_search_all_of_owner import ScheduledSearchAllOfOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledSearchAllOfOwner from a JSON string
scheduled_search_all_of_owner_instance = ScheduledSearchAllOfOwner.from_json(json)
# print the JSON string representation of the object
print(ScheduledSearchAllOfOwner.to_json())

# convert the object into a dict
scheduled_search_all_of_owner_dict = scheduled_search_all_of_owner_instance.to_dict()
# create an instance of ScheduledSearchAllOfOwner from a dict
scheduled_search_all_of_owner_from_dict = ScheduledSearchAllOfOwner.from_dict(scheduled_search_all_of_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


