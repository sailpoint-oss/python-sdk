# RequestedItemStatusPreApprovalTriggerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment left for the pre-approval decision | [optional] 
**reviewer** | **str** | The reviewer of the pre-approval decision | [optional] 
**decision** | **str** | The decision of the pre-approval trigger | [optional] 

## Example

```python
from sailpoint.v3.models.requested_item_status_pre_approval_trigger_details import RequestedItemStatusPreApprovalTriggerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemStatusPreApprovalTriggerDetails from a JSON string
requested_item_status_pre_approval_trigger_details_instance = RequestedItemStatusPreApprovalTriggerDetails.from_json(json)
# print the JSON string representation of the object
print(RequestedItemStatusPreApprovalTriggerDetails.to_json())

# convert the object into a dict
requested_item_status_pre_approval_trigger_details_dict = requested_item_status_pre_approval_trigger_details_instance.to_dict()
# create an instance of RequestedItemStatusPreApprovalTriggerDetails from a dict
requested_item_status_pre_approval_trigger_details_from_dict = RequestedItemStatusPreApprovalTriggerDetails.from_dict(requested_item_status_pre_approval_trigger_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


