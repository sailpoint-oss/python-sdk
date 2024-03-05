# EntitlementDocument

Entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**modified** | **datetime** | ISO-8601 date-time referring to the time when the object was last modified. | [optional] 
**synced** | **str** | ISO-8601 date-time referring to the date-time when object was queued to be synced into search database for use in the search API.   This date-time changes anytime there is an update to the object, which triggers a synchronization event being sent to the search database.  There may be some delay between the &#x60;synced&#x60; time and the time when the updated data is actually available in the search API.  | [optional] 
**display_name** | **str** | Entitlement&#39;s display name. | [optional] 
**source** | [**EntitlementDocumentAllOfSource**](EntitlementDocumentAllOfSource.md) |  | [optional] 
**segments** | [**List[BaseSegment]**](BaseSegment.md) | Segments with the role. | [optional] 
**segment_count** | **int** | Number of segments with the role. | [optional] 
**requestable** | **bool** | Indicates whether the entitlement is requestable. | [optional] [default to False]
**cloud_governed** | **bool** | Indicates whether the entitlement is cloud governed. | [optional] [default to False]
**created** | **datetime** | ISO-8601 date-time referring to the time when the object was created. | [optional] 
**privileged** | **bool** | Indicates whether the entitlement is privileged. | [optional] [default to False]
**identity_count** | **int** | Number of identities who have access to the entitlement. | [optional] 
**tags** | **List[str]** | Tags that have been applied to the object. | [optional] 

## Example

```python
from sailpoint.v3.models.entitlement_document import EntitlementDocument

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementDocument from a JSON string
entitlement_document_instance = EntitlementDocument.from_json(json)
# print the JSON string representation of the object
print EntitlementDocument.to_json()

# convert the object into a dict
entitlement_document_dict = entitlement_document_instance.to_dict()
# create an instance of EntitlementDocument from a dict
entitlement_document_form_dict = entitlement_document.from_dict(entitlement_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


