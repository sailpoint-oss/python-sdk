# ForwardApprovalDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_owner_id** | **str** | The Id of the new owner | 
**comment** | **str** | The comment provided by the forwarder | 

## Example

```python
from beta.models.forward_approval_dto import ForwardApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardApprovalDto from a JSON string
forward_approval_dto_instance = ForwardApprovalDto.from_json(json)
# print the JSON string representation of the object
print ForwardApprovalDto.to_json()

# convert the object into a dict
forward_approval_dto_dict = forward_approval_dto_instance.to_dict()
# create an instance of ForwardApprovalDto from a dict
forward_approval_dto_form_dict = forward_approval_dto.from_dict(forward_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


