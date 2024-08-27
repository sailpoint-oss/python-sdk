# RoleMiningIdentityDistribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Id of the potential role | [optional] 
**distribution** | **List[Dict[str, str]]** |  | [optional] 

## Example

```python
from sailpoint.v2024.models.role_mining_identity_distribution import RoleMiningIdentityDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningIdentityDistribution from a JSON string
role_mining_identity_distribution_instance = RoleMiningIdentityDistribution.from_json(json)
# print the JSON string representation of the object
print(RoleMiningIdentityDistribution.to_json())

# convert the object into a dict
role_mining_identity_distribution_dict = role_mining_identity_distribution_instance.to_dict()
# create an instance of RoleMiningIdentityDistribution from a dict
role_mining_identity_distribution_from_dict = RoleMiningIdentityDistribution.from_dict(role_mining_identity_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


