# PublicIdentity

Details about a public identity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identity id | [optional] 
**name** | **str** | Human-readable display name of identity. | [optional] 
**alias** | **str** | Alternate unique identifier for the identity. | [optional] 
**email** | **str** | Email address of identity. | [optional] 
**status** | **str** | The lifecycle status for the identity | [optional] 
**identity_state** | **str** | The current state of the identity, which determines how Identity Security Cloud interacts with the identity. An identity that is Active will be included identity picklists in Request Center, identity processing, and more. Identities that are Inactive will be excluded from these features.  | [optional] 
**manager** | [**IdentityReference**](IdentityReference.md) |  | [optional] 
**attributes** | [**List[IdentityAttribute]**](IdentityAttribute.md) | The public identity attributes of the identity | [optional] 

## Example

```python
from sailpoint.v3.models.public_identity import PublicIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of PublicIdentity from a JSON string
public_identity_instance = PublicIdentity.from_json(json)
# print the JSON string representation of the object
print PublicIdentity.to_json()

# convert the object into a dict
public_identity_dict = public_identity_instance.to_dict()
# create an instance of PublicIdentity from a dict
public_identity_form_dict = public_identity.from_dict(public_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


