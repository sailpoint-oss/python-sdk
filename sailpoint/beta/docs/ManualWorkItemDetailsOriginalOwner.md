# ManualWorkItemDetailsOriginalOwner

Identity of original work item owner, if the work item has been forwarded.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of original work item owner&#39;s identity. | [optional] 
**id** | **str** | ID of original work item owner&#39;s identity. | [optional] 
**name** | **str** | Display name of original work item owner. | [optional] 

## Example

```python
from beta.models.manual_work_item_details_original_owner import ManualWorkItemDetailsOriginalOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ManualWorkItemDetailsOriginalOwner from a JSON string
manual_work_item_details_original_owner_instance = ManualWorkItemDetailsOriginalOwner.from_json(json)
# print the JSON string representation of the object
print ManualWorkItemDetailsOriginalOwner.to_json()

# convert the object into a dict
manual_work_item_details_original_owner_dict = manual_work_item_details_original_owner_instance.to_dict()
# create an instance of ManualWorkItemDetailsOriginalOwner from a dict
manual_work_item_details_original_owner_form_dict = manual_work_item_details_original_owner.from_dict(manual_work_item_details_original_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


