# TenantConfigurationDetails

Details of any tenant-wide Reassignment Configurations (eg. enabled/disabled)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Flag to determine if Reassignment Configuration is enabled or disabled for a tenant.  When this flag is set to true, Reassignment Configuration is disabled. | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.tenant_configuration_details import TenantConfigurationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TenantConfigurationDetails from a JSON string
tenant_configuration_details_instance = TenantConfigurationDetails.from_json(json)
# print the JSON string representation of the object
print(TenantConfigurationDetails.to_json())

# convert the object into a dict
tenant_configuration_details_dict = tenant_configuration_details_instance.to_dict()
# create an instance of TenantConfigurationDetails from a dict
tenant_configuration_details_from_dict = TenantConfigurationDetails.from_dict(tenant_configuration_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


