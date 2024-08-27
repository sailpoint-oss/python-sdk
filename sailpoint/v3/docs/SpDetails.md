# SpDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Federation protocol role | [optional] 
**entity_id** | **str** | An entity ID is a globally unique name for a SAML entity, either an Identity Provider (IDP) or a Service Provider (SP). | [optional] 
**alias** | **str** | Unique alias used to identify the selected local service provider based on used URL. Used with SP configurations. | [optional] 
**callback_url** | **str** | The allowed callback URL where users will be redirected to after authentication. Used with SP configurations. | [optional] 

## Example

```python
from sailpoint.v3.models.sp_details import SpDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SpDetails from a JSON string
sp_details_instance = SpDetails.from_json(json)
# print the JSON string representation of the object
print(SpDetails.to_json())

# convert the object into a dict
sp_details_dict = sp_details_instance.to_dict()
# create an instance of SpDetails from a dict
sp_details_from_dict = SpDetails.from_dict(sp_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


