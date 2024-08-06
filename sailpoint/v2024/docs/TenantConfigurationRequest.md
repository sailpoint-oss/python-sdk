# TenantConfigurationRequest

Tenant-wide Reassignment Configuration settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_details** | [**TenantConfigurationDetails**](TenantConfigurationDetails.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.tenant_configuration_request import TenantConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantConfigurationRequest from a JSON string
tenant_configuration_request_instance = TenantConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print TenantConfigurationRequest.to_json()

# convert the object into a dict
tenant_configuration_request_dict = tenant_configuration_request_instance.to_dict()
# create an instance of TenantConfigurationRequest from a dict
tenant_configuration_request_form_dict = tenant_configuration_request.from_dict(tenant_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


