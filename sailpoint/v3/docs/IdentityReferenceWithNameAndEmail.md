# IdentityReferenceWithNameAndEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type can only be IDENTITY. This is read-only | [optional] 
**id** | **str** | Identity id. | [optional] 
**name** | **str** | Human-readable display name of identity. This is read-only | [optional] 
**email** | **str** | Email address of identity. This is read-only | [optional] 

## Example

```python
from sailpoint.v3.models.identity_reference_with_name_and_email import IdentityReferenceWithNameAndEmail

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityReferenceWithNameAndEmail from a JSON string
identity_reference_with_name_and_email_instance = IdentityReferenceWithNameAndEmail.from_json(json)
# print the JSON string representation of the object
print IdentityReferenceWithNameAndEmail.to_json()

# convert the object into a dict
identity_reference_with_name_and_email_dict = identity_reference_with_name_and_email_instance.to_dict()
# create an instance of IdentityReferenceWithNameAndEmail from a dict
identity_reference_with_name_and_email_form_dict = identity_reference_with_name_and_email.from_dict(identity_reference_with_name_and_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


