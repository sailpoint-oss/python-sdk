# RoleDocument

Role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | 
**name** | **str** | The human readable name of the referenced object. | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**description** | **str** | Access item&#39;s description. | [optional] 
**created** | **datetime** | ISO-8601 date-time referring to the time when the object was created. | [optional] 
**modified** | **datetime** | ISO-8601 date-time referring to the time when the object was last modified. | [optional] 
**synced** | **datetime** | ISO-8601 date-time referring to the date-time when object was queued to be synced into search database for use in the search API.   This date-time changes anytime there is an update to the object, which triggers a synchronization event being sent to the search database.  There may be some delay between the &#x60;synced&#x60; time and the time when the updated data is actually available in the search API.  | [optional] 
**enabled** | **bool** | Indicates whether the access item is currently enabled. | [optional] [default to False]
**requestable** | **bool** | Indicates whether the access item can be requested. | [optional] [default to True]
**request_comments_required** | **bool** | Indicates whether comments are required for requests to access the item. | [optional] [default to False]
**owner** | [**BaseAccessAllOfOwner**](BaseAccessAllOfOwner.md) |  | [optional] 
**access_profiles** | [**List[BaseAccessProfile]**](BaseAccessProfile.md) | Access profiles included with the role. | [optional] 
**access_profile_count** | **int** | Number of access profiles included with the role. | [optional] 
**tags** | **List[str]** | Tags that have been applied to the object. | [optional] 
**segments** | [**List[BaseSegment]**](BaseSegment.md) | Segments with the role. | [optional] 
**segment_count** | **int** | Number of segments with the role. | [optional] 
**entitlements** | [**List[BaseEntitlement]**](BaseEntitlement.md) | Entitlements included with the role. | [optional] 
**entitlement_count** | **int** | Number of entitlements included with the role. | [optional] 

## Example

```python
from sailpoint.v3.models.role_document import RoleDocument

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


