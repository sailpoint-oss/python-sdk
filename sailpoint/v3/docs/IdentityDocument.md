# IdentityDocument

Identity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | 
**name** | **str** | The human readable name of the referenced object. | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**display_name** | **str** | Identity&#39;s display name. | [optional] 
**first_name** | **str** | Identity&#39;s first name. | [optional] 
**last_name** | **str** | Identity&#39;s last name. | [optional] 
**email** | **str** | Identity&#39;s primary email address. | [optional] 
**created** | **datetime** | ISO-8601 date-time referring to the time when the object was created. | [optional] 
**modified** | **datetime** | ISO-8601 date-time referring to the time when the object was last modified. | [optional] 
**phone** | **str** | Identity&#39;s phone number. | [optional] 
**synced** | **str** | ISO-8601 date-time referring to the date-time when object was queued to be synced into search database for use in the search API.   This date-time changes anytime there is an update to the object, which triggers a synchronization event being sent to the search database.  There may be some delay between the &#x60;synced&#x60; time and the time when the updated data is actually available in the search API.  | [optional] 
**inactive** | **bool** | Indicates whether the identity is inactive. | [optional] [default to False]
**protected** | **bool** | Indicates whether the identity is protected. | [optional] [default to False]
**status** | **str** | Identity&#39;s status in SailPoint. | [optional] 
**employee_number** | **str** | Identity&#39;s employee number. | [optional] 
**manager** | [**IdentityDocumentAllOfManager**](IdentityDocumentAllOfManager.md) |  | [optional] 
**is_manager** | **bool** | Indicates whether the identity is a manager of other identities. | [optional] 
**identity_profile** | [**IdentityDocumentAllOfIdentityProfile**](IdentityDocumentAllOfIdentityProfile.md) |  | [optional] 
**source** | [**IdentityDocumentAllOfSource**](IdentityDocumentAllOfSource.md) |  | [optional] 
**attributes** | **Dict[str, object]** | Map or dictionary of key/value pairs. | [optional] 
**processing_state** | **str** | Identity&#39;s processing state. | [optional] 
**processing_details** | [**ProcessingDetails**](ProcessingDetails.md) |  | [optional] 
**accounts** | [**List[BaseAccount]**](BaseAccount.md) | List of accounts associated with the identity. | [optional] 
**account_count** | **int** | Number of accounts associated with the identity. | [optional] 
**apps** | [**List[App]**](App.md) | List of applications the identity has access to. | [optional] 
**app_count** | **int** | Number of applications the identity has access to. | [optional] 
**access** | [**List[IdentityAccess]**](IdentityAccess.md) | List of access items assigned to the identity. | [optional] 
**access_count** | **int** | Number of access items assigned to the identity. | [optional] 
**entitlement_count** | **int** | Number of entitlements assigned to the identity. | [optional] 
**role_count** | **int** | Number of roles assigned to the identity. | [optional] 
**access_profile_count** | **int** | Number of access profiles assigned to the identity. | [optional] 
**owns** | [**List[Owns]**](Owns.md) | Access items the identity owns. | [optional] 
**owns_count** | **int** | Number of access items the identity owns. | [optional] 
**tags** | **List[str]** | Tags that have been applied to the object. | [optional] 

## Example

```python
from sailpoint.v3.models.identity_document import IdentityDocument

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDocument from a JSON string
identity_document_instance = IdentityDocument.from_json(json)
# print the JSON string representation of the object
print(IdentityDocument.to_json())

# convert the object into a dict
identity_document_dict = identity_document_instance.to_dict()
# create an instance of IdentityDocument from a dict
identity_document_from_dict = IdentityDocument.from_dict(identity_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


