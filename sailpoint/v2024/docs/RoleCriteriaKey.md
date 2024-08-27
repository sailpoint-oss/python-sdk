# RoleCriteriaKey

Refers to a specific Identity attribute, Account attibute, or Entitlement used in Role membership criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RoleCriteriaKeyType**](RoleCriteriaKeyType.md) |  | 
**var_property** | **str** | The name of the attribute or entitlement to which the associated criteria applies. | 
**source_id** | **str** | ID of the Source from which an account attribute or entitlement is drawn. Required if type is ACCOUNT or ENTITLEMENT | [optional] 

## Example

```python
from sailpoint.v2024.models.role_criteria_key import RoleCriteriaKey

# TODO update the JSON string below
json = "{}"
# create an instance of RoleCriteriaKey from a JSON string
role_criteria_key_instance = RoleCriteriaKey.from_json(json)
# print the JSON string representation of the object
print(RoleCriteriaKey.to_json())

# convert the object into a dict
role_criteria_key_dict = role_criteria_key_instance.to_dict()
# create an instance of RoleCriteriaKey from a dict
role_criteria_key_from_dict = RoleCriteriaKey.from_dict(role_criteria_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


