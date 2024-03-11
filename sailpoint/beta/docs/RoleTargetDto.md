# RoleTargetDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**BaseReferenceDto**](BaseReferenceDto.md) |  | [optional] 
**account_info** | [**AccountInfoDto**](AccountInfoDto.md) |  | [optional] 
**role_name** | **str** | Specific role name for this target if using multiple accounts | [optional] 

## Example

```python
from sailpoint.beta.models.role_target_dto import RoleTargetDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoleTargetDto from a JSON string
role_target_dto_instance = RoleTargetDto.from_json(json)
# print the JSON string representation of the object
print RoleTargetDto.to_json()

# convert the object into a dict
role_target_dto_dict = role_target_dto_instance.to_dict()
# create an instance of RoleTargetDto from a dict
role_target_dto_form_dict = role_target_dto.from_dict(role_target_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


