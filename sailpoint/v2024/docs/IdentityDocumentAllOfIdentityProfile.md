# IdentityDocumentAllOfIdentityProfile

Identity's identity profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identity profile&#39;s ID. | [optional] 
**name** | **str** | Identity profile&#39;s name. | [optional] 

## Example

```python
from sailpoint.v2024.models.identity_document_all_of_identity_profile import IdentityDocumentAllOfIdentityProfile

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDocumentAllOfIdentityProfile from a JSON string
identity_document_all_of_identity_profile_instance = IdentityDocumentAllOfIdentityProfile.from_json(json)
# print the JSON string representation of the object
print(IdentityDocumentAllOfIdentityProfile.to_json())

# convert the object into a dict
identity_document_all_of_identity_profile_dict = identity_document_all_of_identity_profile_instance.to_dict()
# create an instance of IdentityDocumentAllOfIdentityProfile from a dict
identity_document_all_of_identity_profile_from_dict = IdentityDocumentAllOfIdentityProfile.from_dict(identity_document_all_of_identity_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


