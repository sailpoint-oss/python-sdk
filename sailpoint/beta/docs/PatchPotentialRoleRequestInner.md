# PatchPotentialRoleRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | The operation to be performed | [optional] 
**path** | **str** | A string JSON Pointer representing the target path to an element to be affected by the operation | 
**value** | [**JsonPatchOperationValue**](JsonPatchOperationValue.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.patch_potential_role_request_inner import PatchPotentialRoleRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPotentialRoleRequestInner from a JSON string
patch_potential_role_request_inner_instance = PatchPotentialRoleRequestInner.from_json(json)
# print the JSON string representation of the object
print(PatchPotentialRoleRequestInner.to_json())

# convert the object into a dict
patch_potential_role_request_inner_dict = patch_potential_role_request_inner_instance.to_dict()
# create an instance of PatchPotentialRoleRequestInner from a dict
patch_potential_role_request_inner_from_dict = PatchPotentialRoleRequestInner.from_dict(patch_potential_role_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


