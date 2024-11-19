# RoleMiningPotentialRoleApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the application | [optional] 
**name** | **str** | Name of the application | [optional] 

## Example

```python
from sailpoint.beta.models.role_mining_potential_role_application import RoleMiningPotentialRoleApplication

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningPotentialRoleApplication from a JSON string
role_mining_potential_role_application_instance = RoleMiningPotentialRoleApplication.from_json(json)
# print the JSON string representation of the object
print(RoleMiningPotentialRoleApplication.to_json())

# convert the object into a dict
role_mining_potential_role_application_dict = role_mining_potential_role_application_instance.to_dict()
# create an instance of RoleMiningPotentialRoleApplication from a dict
role_mining_potential_role_application_from_dict = RoleMiningPotentialRoleApplication.from_dict(role_mining_potential_role_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


