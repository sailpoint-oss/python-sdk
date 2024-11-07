# RoleMatchDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_ref** | [**BaseReferenceDto1**](BaseReferenceDto1.md) |  | [optional] 
**matched_attributes** | [**List[ContextAttributeDto]**](ContextAttributeDto.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.role_match_dto import RoleMatchDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMatchDto from a JSON string
role_match_dto_instance = RoleMatchDto.from_json(json)
# print the JSON string representation of the object
print(RoleMatchDto.to_json())

# convert the object into a dict
role_match_dto_dict = role_match_dto_instance.to_dict()
# create an instance of RoleMatchDto from a dict
role_match_dto_from_dict = RoleMatchDto.from_dict(role_match_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


