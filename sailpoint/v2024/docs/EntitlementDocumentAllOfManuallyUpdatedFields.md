# EntitlementDocumentAllOfManuallyUpdatedFields

Indicates whether the entitlement's display name and/or description have been manually updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **bool** |  | [optional] [default to False]
**display_name** | **bool** |  | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.entitlement_document_all_of_manually_updated_fields import EntitlementDocumentAllOfManuallyUpdatedFields

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementDocumentAllOfManuallyUpdatedFields from a JSON string
entitlement_document_all_of_manually_updated_fields_instance = EntitlementDocumentAllOfManuallyUpdatedFields.from_json(json)
# print the JSON string representation of the object
print(EntitlementDocumentAllOfManuallyUpdatedFields.to_json())

# convert the object into a dict
entitlement_document_all_of_manually_updated_fields_dict = entitlement_document_all_of_manually_updated_fields_instance.to_dict()
# create an instance of EntitlementDocumentAllOfManuallyUpdatedFields from a dict
entitlement_document_all_of_manually_updated_fields_from_dict = EntitlementDocumentAllOfManuallyUpdatedFields.from_dict(entitlement_document_all_of_manually_updated_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


