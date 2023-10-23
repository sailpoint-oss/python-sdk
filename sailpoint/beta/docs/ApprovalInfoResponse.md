# ApprovalInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id of approver | [optional] 
**name** | **str** | the name of approver | [optional] 
**status** | **str** | the status of the approval request | [optional] 

## Example

```python
from beta.models.approval_info_response import ApprovalInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalInfoResponse from a JSON string
approval_info_response_instance = ApprovalInfoResponse.from_json(json)
# print the JSON string representation of the object
print ApprovalInfoResponse.to_json()

# convert the object into a dict
approval_info_response_dict = approval_info_response_instance.to_dict()
# create an instance of ApprovalInfoResponse from a dict
approval_info_response_form_dict = approval_info_response.from_dict(approval_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


