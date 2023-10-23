# EntitlementDocument

Entitlement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | 
**name** | **str** | The human readable name of the referenced object. | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**description** | **str** | A description of the entitlement | [optional] 
**attribute** | **str** | The name of the entitlement attribute | [optional] 
**value** | **str** | The value of the entitlement | [optional] 
**modified** | **datetime** | A date-time in ISO-8601 format | [optional] 
**synced** | **datetime** | A date-time in ISO-8601 format | [optional] 
**display_name** | **str** | The display name of the entitlement | [optional] 
**source** | [**Reference**](Reference.md) |  | [optional] 
**privileged** | **bool** |  | [optional] 
**identity_count** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from v3.models.entitlement_document import EntitlementDocument

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


