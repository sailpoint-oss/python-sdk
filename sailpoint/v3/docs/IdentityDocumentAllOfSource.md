# IdentityDocumentAllOfSource

Identity's source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of identity&#39;s source. | [optional] 
**name** | **str** | Display name of identity&#39;s source. | [optional] 

## Example

```python
from sailpoint.v3.models.identity_document_all_of_source import IdentityDocumentAllOfSource

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDocumentAllOfSource from a JSON string
identity_document_all_of_source_instance = IdentityDocumentAllOfSource.from_json(json)
# print the JSON string representation of the object
print IdentityDocumentAllOfSource.to_json()

# convert the object into a dict
identity_document_all_of_source_dict = identity_document_all_of_source_instance.to_dict()
# create an instance of IdentityDocumentAllOfSource from a dict
identity_document_all_of_source_form_dict = identity_document_all_of_source.from_dict(identity_document_all_of_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


