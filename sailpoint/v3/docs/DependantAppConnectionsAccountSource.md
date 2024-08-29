# DependantAppConnectionsAccountSource

The Account Source of the connected Application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_for_password_management** | **bool** | Use this Account Source for password management | [optional] [default to False]
**password_policies** | [**List[DependantAppConnectionsAccountSourcePasswordPoliciesInner]**](DependantAppConnectionsAccountSourcePasswordPoliciesInner.md) | A list of Password Policies for this Account Source | [optional] 

## Example

```python
from sailpoint.v3.models.dependant_app_connections_account_source import DependantAppConnectionsAccountSource

# TODO update the JSON string below
json = "{}"
# create an instance of DependantAppConnectionsAccountSource from a JSON string
dependant_app_connections_account_source_instance = DependantAppConnectionsAccountSource.from_json(json)
# print the JSON string representation of the object
print(DependantAppConnectionsAccountSource.to_json())

# convert the object into a dict
dependant_app_connections_account_source_dict = dependant_app_connections_account_source_instance.to_dict()
# create an instance of DependantAppConnectionsAccountSource from a dict
dependant_app_connections_account_source_from_dict = DependantAppConnectionsAccountSource.from_dict(dependant_app_connections_account_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


