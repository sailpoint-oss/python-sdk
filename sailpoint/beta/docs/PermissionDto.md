# PermissionDto

Simplified DTO for the Permission objects stored in SailPoint's database. The data is aggregated from customer systems and is free-form, so its appearance can vary largely between different clients/customers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rights** | **List[str]** | All the rights (e.g. actions) that this permission allows on the target | [optional] [readonly] 
**target** | **str** | The target the permission would grants rights on. | [optional] [readonly] 

## Example

```python
from sailpoint.beta.models.permission_dto import PermissionDto

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionDto from a JSON string
permission_dto_instance = PermissionDto.from_json(json)
# print the JSON string representation of the object
print PermissionDto.to_json()

# convert the object into a dict
permission_dto_dict = permission_dto_instance.to_dict()
# create an instance of PermissionDto from a dict
permission_dto_form_dict = permission_dto.from_dict(permission_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


