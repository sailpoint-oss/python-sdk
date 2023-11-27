# PreApprovalTriggerDetails

Provides additional details about the pre-approval trigger for this request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment left for the pre-approval decision | [optional] 
**reviewer** | **str** | The reviewer of the pre-approval decision | [optional] 
**decision** | **str** | The decision of the pre-approval trigger | [optional] 

## Example

```python
from sailpoint.v3.models.pre_approval_trigger_details import PreApprovalTriggerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PreApprovalTriggerDetails from a JSON string
pre_approval_trigger_details_instance = PreApprovalTriggerDetails.from_json(json)
# print the JSON string representation of the object
print PreApprovalTriggerDetails.to_json()

# convert the object into a dict
pre_approval_trigger_details_dict = pre_approval_trigger_details_instance.to_dict()
# create an instance of PreApprovalTriggerDetails from a dict
pre_approval_trigger_details_form_dict = pre_approval_trigger_details.from_dict(pre_approval_trigger_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


