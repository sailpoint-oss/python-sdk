# AccessProfileDocument

This is more of a complete representation of an access profile.  

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
**source** | [**Reference**](Reference.md) |  | [optional] 
**entitlements** | [**List[BaseEntitlement]**](BaseEntitlement.md) |  | [optional] 
**entitlement_count** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from sailpoint.v3.models.access_profile_document import AccessProfileDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileDocument from a JSON string
access_profile_document_instance = AccessProfileDocument.from_json(json)
# print the JSON string representation of the object
print AccessProfileDocument.to_json()

# convert the object into a dict
access_profile_document_dict = access_profile_document_instance.to_dict()
# create an instance of AccessProfileDocument from a dict
access_profile_document_form_dict = access_profile_document.from_dict(access_profile_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


