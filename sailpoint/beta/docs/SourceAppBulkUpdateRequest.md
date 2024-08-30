# SourceAppBulkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_ids** | **List[str]** | List of source app ids to update | 
**json_patch** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | The JSONPatch payload used to update the source app. | 

## Example

```python
from sailpoint.beta.models.source_app_bulk_update_request import SourceAppBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SourceAppBulkUpdateRequest from a JSON string
source_app_bulk_update_request_instance = SourceAppBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SourceAppBulkUpdateRequest.to_json())

# convert the object into a dict
source_app_bulk_update_request_dict = source_app_bulk_update_request_instance.to_dict()
# create an instance of SourceAppBulkUpdateRequest from a dict
source_app_bulk_update_request_from_dict = SourceAppBulkUpdateRequest.from_dict(source_app_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


