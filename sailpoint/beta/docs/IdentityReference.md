# IdentityReference

The manager for the identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | Identity id | [optional] 
**name** | **str** | Human-readable display name of identity. | [optional] 

## Example

```python
from sailpoint.beta.models.identity_reference import IdentityReference

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityReference from a JSON string
identity_reference_instance = IdentityReference.from_json(json)
# print the JSON string representation of the object
print(IdentityReference.to_json())

# convert the object into a dict
identity_reference_dict = identity_reference_instance.to_dict()
# create an instance of IdentityReference from a dict
identity_reference_from_dict = IdentityReference.from_dict(identity_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


