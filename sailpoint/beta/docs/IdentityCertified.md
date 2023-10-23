# IdentityCertified


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certification_id** | **str** | the id of the certification item | [optional] 
**certification_name** | **str** | the certification item name | [optional] 
**signed_date** | **str** | the date ceritification was signed | [optional] 
**certifiers** | [**List[CertifierResponse]**](CertifierResponse.md) | this field is deprecated and may go away | [optional] 
**reviewers** | [**List[CertifierResponse]**](CertifierResponse.md) | The list of identities who review this certification | [optional] 
**signer** | [**CertifierResponse**](CertifierResponse.md) |  | [optional] 
**event_type** | **str** | the event type | [optional] 
**dt** | **str** | the date of event | [optional] 

## Example

```python
from beta.models.identity_certified import IdentityCertified

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityCertified from a JSON string
identity_certified_instance = IdentityCertified.from_json(json)
# print the JSON string representation of the object
print IdentityCertified.to_json()

# convert the object into a dict
identity_certified_dict = identity_certified_instance.to_dict()
# create an instance of IdentityCertified from a dict
identity_certified_form_dict = identity_certified.from_dict(identity_certified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


