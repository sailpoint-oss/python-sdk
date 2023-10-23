# IdentityReferenceWithId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | Identity id | [optional] 

## Example

```python
from beta.models.identity_reference_with_id import IdentityReferenceWithId

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityReferenceWithId from a JSON string
identity_reference_with_id_instance = IdentityReferenceWithId.from_json(json)
# print the JSON string representation of the object
print IdentityReferenceWithId.to_json()

# convert the object into a dict
identity_reference_with_id_dict = identity_reference_with_id_instance.to_dict()
# create an instance of IdentityReferenceWithId from a dict
identity_reference_with_id_form_dict = identity_reference_with_id.from_dict(identity_reference_with_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


