# DependantAppConnectionsAccountSourcePasswordPoliciesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from sailpoint.v3.models.dependant_app_connections_account_source_password_policies_inner import DependantAppConnectionsAccountSourcePasswordPoliciesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DependantAppConnectionsAccountSourcePasswordPoliciesInner from a JSON string
dependant_app_connections_account_source_password_policies_inner_instance = DependantAppConnectionsAccountSourcePasswordPoliciesInner.from_json(json)
# print the JSON string representation of the object
print(DependantAppConnectionsAccountSourcePasswordPoliciesInner.to_json())

# convert the object into a dict
dependant_app_connections_account_source_password_policies_inner_dict = dependant_app_connections_account_source_password_policies_inner_instance.to_dict()
# create an instance of DependantAppConnectionsAccountSourcePasswordPoliciesInner from a dict
dependant_app_connections_account_source_password_policies_inner_from_dict = DependantAppConnectionsAccountSourcePasswordPoliciesInner.from_dict(dependant_app_connections_account_source_password_policies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


