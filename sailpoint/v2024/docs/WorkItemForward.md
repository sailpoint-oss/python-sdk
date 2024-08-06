# WorkItemForward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_owner_id** | **str** | The ID of the identity to forward this work item to. | 
**comment** | **str** | Comments to send to the target owner | 
**send_notifications** | **bool** | If true, send a notification to the target owner. | [optional] [default to True]

## Example

```python
from sailpoint.v2024.models.work_item_forward import WorkItemForward

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemForward from a JSON string
work_item_forward_instance = WorkItemForward.from_json(json)
# print the JSON string representation of the object
print WorkItemForward.to_json()

# convert the object into a dict
work_item_forward_dict = work_item_forward_instance.to_dict()
# create an instance of WorkItemForward from a dict
work_item_forward_form_dict = work_item_forward.from_dict(work_item_forward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


