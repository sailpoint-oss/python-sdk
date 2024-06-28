# FederationProtocolDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Federation protocol role | [optional] 
**entity_id** | **str** | An entity ID is a globally unique name for a SAML entity, either an Identity Provider (IDP) or a Service Provider (SP). | [optional] 

## Example

```python
from sailpoint.v3.models.federation_protocol_details import FederationProtocolDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FederationProtocolDetails from a JSON string
federation_protocol_details_instance = FederationProtocolDetails.from_json(json)
# print the JSON string representation of the object
print FederationProtocolDetails.to_json()

# convert the object into a dict
federation_protocol_details_dict = federation_protocol_details_instance.to_dict()
# create an instance of FederationProtocolDetails from a dict
federation_protocol_details_form_dict = federation_protocol_details.from_dict(federation_protocol_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


