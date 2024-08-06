# EntitlementBulkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_ids** | **List[str]** | List of entitlement ids to update | 
**json_patch** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) |  | 

## Example

```python
from sailpoint.v2024.models.entitlement_bulk_update_request import EntitlementBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementBulkUpdateRequest from a JSON string
entitlement_bulk_update_request_instance = EntitlementBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print EntitlementBulkUpdateRequest.to_json()

# convert the object into a dict
entitlement_bulk_update_request_dict = entitlement_bulk_update_request_instance.to_dict()
# create an instance of EntitlementBulkUpdateRequest from a dict
entitlement_bulk_update_request_form_dict = entitlement_bulk_update_request.from_dict(entitlement_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


