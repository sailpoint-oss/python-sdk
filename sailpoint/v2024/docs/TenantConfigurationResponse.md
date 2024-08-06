# TenantConfigurationResponse

Tenant-wide Reassignment Configuration settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_details** | [**AuditDetails**](AuditDetails.md) |  | [optional] 
**config_details** | [**TenantConfigurationDetails**](TenantConfigurationDetails.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.tenant_configuration_response import TenantConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantConfigurationResponse from a JSON string
tenant_configuration_response_instance = TenantConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print TenantConfigurationResponse.to_json()

# convert the object into a dict
tenant_configuration_response_dict = tenant_configuration_response_instance.to_dict()
# create an instance of TenantConfigurationResponse from a dict
tenant_configuration_response_form_dict = tenant_configuration_response.from_dict(tenant_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


