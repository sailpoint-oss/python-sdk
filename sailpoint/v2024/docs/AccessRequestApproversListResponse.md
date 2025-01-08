# AccessRequestApproversListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Approver id. | [optional] 
**email** | **str** | Email of the approver. | [optional] 
**name** | **str** | Name of the approver. | [optional] 
**approval_id** | **str** | Id of the approval item. | [optional] 
**type** | **str** | Type of the object returned. In this case, the value for this field will always Identity. | [optional] 

## Example

```python
from sailpoint.v2024.models.access_request_approvers_list_response import AccessRequestApproversListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestApproversListResponse from a JSON string
access_request_approvers_list_response_instance = AccessRequestApproversListResponse.from_json(json)
# print the JSON string representation of the object
print(AccessRequestApproversListResponse.to_json())

# convert the object into a dict
access_request_approvers_list_response_dict = access_request_approvers_list_response_instance.to_dict()
# create an instance of AccessRequestApproversListResponse from a dict
access_request_approvers_list_response_from_dict = AccessRequestApproversListResponse.from_dict(access_request_approvers_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


