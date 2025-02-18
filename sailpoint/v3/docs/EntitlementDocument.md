# EntitlementDocument

Entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referenced object. | 
**name** | **str** | The human readable name of the referenced object. | 
**modified** | **datetime** | ISO-8601 date-time referring to the time when the object was last modified. | [optional] 
**synced** | **str** | ISO-8601 date-time referring to the date-time when object was queued to be synced into search database for use in the search API.   This date-time changes anytime there is an update to the object, which triggers a synchronization event being sent to the search database.  There may be some delay between the &#x60;synced&#x60; time and the time when the updated data is actually available in the search API.  | [optional] 
**display_name** | **str** | Entitlement&#39;s display name. | [optional] 
**source** | [**EntitlementDocumentAllOfSource**](EntitlementDocumentAllOfSource.md) |  | [optional] 
**segments** | [**List[BaseSegment]**](BaseSegment.md) | Segments with the entitlement. | [optional] 
**segment_count** | **int** | Number of segments with the role. | [optional] 
**requestable** | **bool** | Indicates whether the entitlement is requestable. | [optional] [default to False]
**cloud_governed** | **bool** | Indicates whether the entitlement is cloud governed. | [optional] [default to False]
**created** | **datetime** | ISO-8601 date-time referring to the time when the object was created. | [optional] 
**privileged** | **bool** | Indicates whether the entitlement is privileged. | [optional] [default to False]
**tags** | **List[str]** | Tags that have been applied to the object. | [optional] 
**attribute** | **str** | Attribute information for the entitlement. | [optional] 
**value** | **str** | Value of the entitlement. | [optional] 
**source_schema_object_type** | **str** | Source schema object type of the entitlement. | [optional] 
**var_schema** | **str** | Schema type of the entitlement. | [optional] 
**hash** | **str** | Read-only calculated hash value of an entitlement. | [optional] 
**attributes** | **Dict[str, object]** | Attributes of the entitlement. | [optional] 
**truncated_attributes** | **List[str]** | Truncated attributes of the entitlement. | [optional] 
**contains_data_access** | **bool** | Indicates whether the entitlement contains data access. | [optional] [default to False]
**manually_updated_fields** | [**EntitlementDocumentAllOfManuallyUpdatedFields**](EntitlementDocumentAllOfManuallyUpdatedFields.md) |  | [optional] 
**permissions** | [**List[EntitlementDocumentAllOfPermissions]**](EntitlementDocumentAllOfPermissions.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.entitlement_document import EntitlementDocument

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementDocument from a JSON string
entitlement_document_instance = EntitlementDocument.from_json(json)
# print the JSON string representation of the object
print(EntitlementDocument.to_json())

# convert the object into a dict
entitlement_document_dict = entitlement_document_instance.to_dict()
# create an instance of EntitlementDocument from a dict
entitlement_document_from_dict = EntitlementDocument.from_dict(entitlement_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


