# ApprovalDto

Payload for changing the fields of an approval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **object** | Object representation of a comment on the approval | [optional] 
**approved_by** | [**List[ApprovalIdentity]**](ApprovalIdentity.md) | An array of identities who have approved the approval | [optional] 
**rejected_by** | [**List[ApprovalIdentity]**](ApprovalIdentity.md) | An array of identities who have rejected the approval | [optional] 
**reassign_from** | [**ApprovalIdentity**](ApprovalIdentity.md) |  | [optional] 
**reassign_to** | [**ApprovalIdentity**](ApprovalIdentity.md) |  | [optional] 
**additional_attributes** | **object** | Any additional attributes that the approval request may need | [optional] 

## Example

```python
from sailpoint.v2024.models.approval_dto import ApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalDto from a JSON string
approval_dto_instance = ApprovalDto.from_json(json)
# print the JSON string representation of the object
print(ApprovalDto.to_json())

# convert the object into a dict
approval_dto_dict = approval_dto_instance.to_dict()
# create an instance of ApprovalDto from a dict
approval_dto_from_dict = ApprovalDto.from_dict(approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


