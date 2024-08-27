# ServiceProviderConfigurationFederationProtocolDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Federation protocol role | [optional] 
**entity_id** | **str** | An entity ID is a globally unique name for a SAML entity, either an Identity Provider (IDP) or a Service Provider (SP). | [optional] 
**binding** | **str** | Defines the binding used for the SAML flow. Used with IDP configurations. | [optional] 
**auth_context** | **str** | Specifies the SAML authentication method to use. Used with IDP configurations. | [optional] 
**logout_url** | **str** | The IDP logout URL. Used with IDP configurations. | [optional] 
**include_auth_context** | **bool** | Determines if the configured AuthnContext should be used or the default. Used with IDP configurations. | [optional] [default to False]
**name_id** | **str** | The name id format to use. Used with IDP configurations. | [optional] 
**jit_configuration** | [**JITConfiguration**](JITConfiguration.md) |  | [optional] 
**cert** | **str** | The Base64-encoded certificate used by the IDP. Used with IDP configurations. | [optional] 
**login_url_post** | **str** | The IDP POST URL, used with IDP HTTP-POST bindings for IDP-initiated logins. Used with IDP configurations. | [optional] 
**login_url_redirect** | **str** | The IDP Redirect URL. Used with IDP configurations. | [optional] 
**mapping_attribute** | **str** | Return the saml Id for the given user, based on the IDN as SP settings of the org. Used with IDP configurations. | [optional] 
**certificate_expiration_date** | **str** | The expiration date extracted from the certificate. | [optional] 
**certificate_name** | **str** | The name extracted from the certificate. | [optional] 
**alias** | **str** | Unique alias used to identify the selected local service provider based on used URL. Used with SP configurations. | [optional] 
**callback_url** | **str** | The allowed callback URL where users will be redirected to after authentication. Used with SP configurations. | [optional] 

## Example

```python
from sailpoint.v3.models.service_provider_configuration_federation_protocol_details_inner import ServiceProviderConfigurationFederationProtocolDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProviderConfigurationFederationProtocolDetailsInner from a JSON string
service_provider_configuration_federation_protocol_details_inner_instance = ServiceProviderConfigurationFederationProtocolDetailsInner.from_json(json)
# print the JSON string representation of the object
print(ServiceProviderConfigurationFederationProtocolDetailsInner.to_json())

# convert the object into a dict
service_provider_configuration_federation_protocol_details_inner_dict = service_provider_configuration_federation_protocol_details_inner_instance.to_dict()
# create an instance of ServiceProviderConfigurationFederationProtocolDetailsInner from a dict
service_provider_configuration_federation_protocol_details_inner_from_dict = ServiceProviderConfigurationFederationProtocolDetailsInner.from_dict(service_provider_configuration_federation_protocol_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


