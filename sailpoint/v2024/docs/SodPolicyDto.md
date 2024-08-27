# SodPolicyDto

SOD policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | SOD policy DTO type. | [optional] 
**id** | **str** | SOD policy ID. | [optional] 
**name** | **str** | SOD policy display name. | [optional] 

## Example

```python
from sailpoint.v2024.models.sod_policy_dto import SodPolicyDto

# TODO update the JSON string below
json = "{}"
# create an instance of SodPolicyDto from a JSON string
sod_policy_dto_instance = SodPolicyDto.from_json(json)
# print the JSON string representation of the object
print(SodPolicyDto.to_json())

# convert the object into a dict
sod_policy_dto_dict = sod_policy_dto_instance.to_dict()
# create an instance of SodPolicyDto from a dict
sod_policy_dto_from_dict = SodPolicyDto.from_dict(sod_policy_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


