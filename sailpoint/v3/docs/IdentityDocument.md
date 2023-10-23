# IdentityDocument

Identity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | 
**name** | **str** | The human readable name of the referenced object. | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**display_name** | **str** | The display name of the identity | [optional] 
**first_name** | **str** | The first name of the identity | [optional] 
**last_name** | **str** | The last name of the identity | [optional] 
**email** | **str** | The identity&#39;s primary email address | [optional] 
**created** | **datetime** | A date-time in ISO-8601 format | [optional] 
**modified** | **datetime** | A date-time in ISO-8601 format | [optional] 
**synced** | **datetime** | A date-time in ISO-8601 format | [optional] 
**phone** | **str** | The phone number of the identity | [optional] 
**inactive** | **bool** | Indicates if the identity is inactive | [optional] 
**protected** | **bool** |  | [optional] 
**status** | **str** | The identity&#39;s status in SailPoint | [optional] 
**employee_number** | **str** |  | [optional] 
**manager** | [**DisplayReference**](DisplayReference.md) |  | [optional] 
**is_manager** | **bool** | Indicates if this identity is a manager of other identities | [optional] 
**identity_profile** | [**Reference**](Reference.md) |  | [optional] 
**source** | [**Reference**](Reference.md) |  | [optional] 
**attributes** | **Dict[str, object]** | a map or dictionary of key/value pairs | [optional] 
**processing_state** | **str** |  | [optional] 
**processing_details** | [**ProcessingDetails**](ProcessingDetails.md) |  | [optional] 
**accounts** | [**List[BaseAccount]**](BaseAccount.md) | List of accounts associated with the identity | [optional] 
**account_count** | **int** | Number of accounts associated with the identity | [optional] 
**apps** | [**List[App]**](App.md) | The list of applications the identity has access to | [optional] 
**app_count** | **int** | The number of applications the identity has access to | [optional] 
**access** | [**List[IdentityAccess]**](IdentityAccess.md) | The list of access items assigned to the identity | [optional] 
**access_count** | **int** | The number of access items assigned to the identity | [optional] 
**access_profile_count** | **int** | The number of access profiles assigned to the identity | [optional] 
**entitlement_count** | **int** | The number of entitlements assigned to the identity | [optional] 
**role_count** | **int** | The number of roles assigned to the identity | [optional] 
**owns** | [**Owns**](Owns.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from v3.models.identity_document import IdentityDocument

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDocument from a JSON string
identity_document_instance = IdentityDocument.from_json(json)
# print the JSON string representation of the object
print IdentityDocument.to_json()

# convert the object into a dict
identity_document_dict = identity_document_instance.to_dict()
# create an instance of IdentityDocument from a dict
identity_document_form_dict = identity_document.from_dict(identity_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


