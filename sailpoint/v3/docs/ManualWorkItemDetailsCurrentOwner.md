# ManualWorkItemDetailsCurrentOwner

Identity of current work item owner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of current work item owner&#39;s identity. | [optional] 
**id** | **str** | ID of current work item owner&#39;s identity. | [optional] 
**name** | **str** | Display name of current work item owner. | [optional] 

## Example

```python
from sailpoint.v3.models.manual_work_item_details_current_owner import ManualWorkItemDetailsCurrentOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ManualWorkItemDetailsCurrentOwner from a JSON string
manual_work_item_details_current_owner_instance = ManualWorkItemDetailsCurrentOwner.from_json(json)
# print the JSON string representation of the object
print(ManualWorkItemDetailsCurrentOwner.to_json())

# convert the object into a dict
manual_work_item_details_current_owner_dict = manual_work_item_details_current_owner_instance.to_dict()
# create an instance of ManualWorkItemDetailsCurrentOwner from a dict
manual_work_item_details_current_owner_from_dict = ManualWorkItemDetailsCurrentOwner.from_dict(manual_work_item_details_current_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


