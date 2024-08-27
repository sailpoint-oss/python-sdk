# IdentityDocumentAllOfManager

Identity's manager.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of identity&#39;s manager. | [optional] 
**name** | **str** | Name of identity&#39;s manager. | [optional] 
**display_name** | **str** | Display name of identity&#39;s manager. | [optional] 

## Example

```python
from sailpoint.v3.models.identity_document_all_of_manager import IdentityDocumentAllOfManager

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDocumentAllOfManager from a JSON string
identity_document_all_of_manager_instance = IdentityDocumentAllOfManager.from_json(json)
# print the JSON string representation of the object
print(IdentityDocumentAllOfManager.to_json())

# convert the object into a dict
identity_document_all_of_manager_dict = identity_document_all_of_manager_instance.to_dict()
# create an instance of IdentityDocumentAllOfManager from a dict
identity_document_all_of_manager_from_dict = IdentityDocumentAllOfManager.from_dict(identity_document_all_of_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


