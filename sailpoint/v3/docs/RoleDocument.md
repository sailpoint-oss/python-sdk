# RoleDocument

Role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | 
**name** | **str** | The human readable name of the referenced object. | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**description** | **str** | The description of the access item | [optional] 
**created** | **datetime** | A date-time in ISO-8601 format | [optional] 
**modified** | **datetime** | A date-time in ISO-8601 format | [optional] 
**synced** | **datetime** | A date-time in ISO-8601 format | [optional] 
**enabled** | **bool** |  | [optional] 
**requestable** | **bool** | Indicates if the access can be requested | [optional] 
**request_comments_required** | **bool** | Indicates if comments are required when requesting access | [optional] 
**owner** | [**Owner**](Owner.md) |  | [optional] 
**access_profiles** | [**List[Reference]**](Reference.md) |  | [optional] 
**access_profile_count** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from v3.models.role_document import RoleDocument

# TODO update the JSON string below
json = "{}"
# create an instance of RoleDocument from a JSON string
role_document_instance = RoleDocument.from_json(json)
# print the JSON string representation of the object
print RoleDocument.to_json()

# convert the object into a dict
role_document_dict = role_document_instance.to_dict()
# create an instance of RoleDocument from a dict
role_document_form_dict = role_document.from_dict(role_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


