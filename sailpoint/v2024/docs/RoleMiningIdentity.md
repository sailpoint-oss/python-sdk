# RoleMiningIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the identity | [optional] 
**name** | **str** | Name of the identity | [optional] 
**attributes** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from sailpoint.v2024.models.role_mining_identity import RoleMiningIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningIdentity from a JSON string
role_mining_identity_instance = RoleMiningIdentity.from_json(json)
# print the JSON string representation of the object
print(RoleMiningIdentity.to_json())

# convert the object into a dict
role_mining_identity_dict = role_mining_identity_instance.to_dict()
# create an instance of RoleMiningIdentity from a dict
role_mining_identity_from_dict = RoleMiningIdentity.from_dict(role_mining_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


