# EntitlementDocumentAllOfSource

Entitlement's source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of entitlement&#39;s source. | [optional] 
**name** | **str** | Display name of entitlement&#39;s source. | [optional] 

## Example

```python
from sailpoint.v2024.models.entitlement_document_all_of_source import EntitlementDocumentAllOfSource

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementDocumentAllOfSource from a JSON string
entitlement_document_all_of_source_instance = EntitlementDocumentAllOfSource.from_json(json)
# print the JSON string representation of the object
print EntitlementDocumentAllOfSource.to_json()

# convert the object into a dict
entitlement_document_all_of_source_dict = entitlement_document_all_of_source_instance.to_dict()
# create an instance of EntitlementDocumentAllOfSource from a dict
entitlement_document_all_of_source_form_dict = entitlement_document_all_of_source.from_dict(entitlement_document_all_of_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


