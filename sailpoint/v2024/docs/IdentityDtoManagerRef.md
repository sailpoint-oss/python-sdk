# IdentityDtoManagerRef

Identity's manager.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of identity&#39;s manager. | [optional] 
**id** | **str** | ID of identity&#39;s manager. | [optional] 
**name** | **str** | Human-readable display name of identity&#39;s manager. | [optional] 

## Example

```python
from sailpoint.v2024.models.identity_dto_manager_ref import IdentityDtoManagerRef

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDtoManagerRef from a JSON string
identity_dto_manager_ref_instance = IdentityDtoManagerRef.from_json(json)
# print the JSON string representation of the object
print IdentityDtoManagerRef.to_json()

# convert the object into a dict
identity_dto_manager_ref_dict = identity_dto_manager_ref_instance.to_dict()
# create an instance of IdentityDtoManagerRef from a dict
identity_dto_manager_ref_form_dict = identity_dto_manager_ref.from_dict(identity_dto_manager_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


