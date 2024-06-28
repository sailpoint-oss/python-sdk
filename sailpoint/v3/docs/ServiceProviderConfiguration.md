# ServiceProviderConfiguration

Represents the IdentityNow as Service Provider Configuration allowing customers to log into IDN via an Identity Provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | This determines whether or not the SAML authentication flow is enabled for an org | [optional] [default to False]
**bypass_idp** | **bool** | This allows basic login with the parameter prompt&#x3D;true. This is often toggled on when debugging SAML authentication setup. When false, only org admins with MFA-enabled can bypass the IDP. | [optional] [default to False]
**saml_configuration_valid** | **bool** | This indicates whether or not the SAML configuration is valid. | [optional] [default to False]
**federation_protocol_details** | [**List[ServiceProviderConfigurationFederationProtocolDetailsInner]**](ServiceProviderConfigurationFederationProtocolDetailsInner.md) | A list of the abstract implementations of the Federation Protocol details. Typically, this will include on SpDetails object and one IdpDetails object used in tandem to define a SAML integration between a customer&#39;s identity provider and a customer&#39;s SailPoint instance (i.e., the service provider). | [optional] 

## Example

```python
from sailpoint.v3.models.service_provider_configuration import ServiceProviderConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProviderConfiguration from a JSON string
service_provider_configuration_instance = ServiceProviderConfiguration.from_json(json)
# print the JSON string representation of the object
print ServiceProviderConfiguration.to_json()

# convert the object into a dict
service_provider_configuration_dict = service_provider_configuration_instance.to_dict()
# create an instance of ServiceProviderConfiguration from a dict
service_provider_configuration_form_dict = service_provider_configuration.from_dict(service_provider_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


