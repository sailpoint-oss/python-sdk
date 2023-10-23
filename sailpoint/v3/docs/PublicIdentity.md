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
**manager** | [**IdentityReference**](IdentityReference.md) |  | [optional] 
**attributes** | [**List[IdentityAttribute]**](IdentityAttribute.md) | The public identity attributes of the identity | [optional] 

## Example

```python
from v3.models.public_identity import PublicIdentity

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


