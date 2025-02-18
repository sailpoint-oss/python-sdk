# AccessProfileDocument

More complete representation of an access profile.  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Access item&#39;s description. | [optional] 
**created** | **datetime** | ISO-8601 date-time referring to the time when the object was created. | [optional] 
**modified** | **datetime** | ISO-8601 date-time referring to the time when the object was last modified. | [optional] 
**synced** | **datetime** | ISO-8601 date-time referring to the date-time when object was queued to be synced into search database for use in the search API.   This date-time changes anytime there is an update to the object, which triggers a synchronization event being sent to the search database.  There may be some delay between the &#x60;synced&#x60; time and the time when the updated data is actually available in the search API.  | [optional] 
**enabled** | **bool** | Indicates whether the access item is currently enabled. | [optional] [default to False]
**requestable** | **bool** | Indicates whether the access item can be requested. | [optional] [default to True]
**request_comments_required** | **bool** | Indicates whether comments are required for requests to access the item. | [optional] [default to False]
**owner** | [**BaseAccessOwner**](BaseAccessOwner.md) |  | [optional] 
**id** | **str** | Access profile&#39;s ID. | 
**name** | **str** | Access profile&#39;s name. | 
**source** | [**AccessProfileDocumentAllOfSource**](AccessProfileDocumentAllOfSource.md) |  | [optional] 
**entitlements** | [**List[BaseEntitlement]**](BaseEntitlement.md) | Entitlements the access profile has access to. | [optional] 
**entitlement_count** | **int** | Number of entitlements. | [optional] 
**segments** | [**List[BaseSegment]**](BaseSegment.md) | Segments with the access profile. | [optional] 
**segment_count** | **int** | Number of segments with the access profile. | [optional] 
**tags** | **List[str]** | Tags that have been applied to the object. | [optional] 
**apps** | [**List[AccessApps]**](AccessApps.md) | Applications with the access profile | [optional] 

## Example

```python
from sailpoint.v3.models.access_profile_document import AccessProfileDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileDocument from a JSON string
access_profile_document_instance = AccessProfileDocument.from_json(json)
# print the JSON string representation of the object
print(AccessProfileDocument.to_json())

# convert the object into a dict
access_profile_document_dict = access_profile_document_instance.to_dict()
# create an instance of AccessProfileDocument from a dict
access_profile_document_from_dict = AccessProfileDocument.from_dict(access_profile_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


