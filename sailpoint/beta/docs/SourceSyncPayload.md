# SourceSyncPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Payload type. | 
**data_json** | **str** | Payload type. | 

## Example

```python
from beta.models.source_sync_payload import SourceSyncPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SourceSyncPayload from a JSON string
source_sync_payload_instance = SourceSyncPayload.from_json(json)
# print the JSON string representation of the object
print SourceSyncPayload.to_json()

# convert the object into a dict
source_sync_payload_dict = source_sync_payload_instance.to_dict()
# create an instance of SourceSyncPayload from a dict
source_sync_payload_form_dict = source_sync_payload.from_dict(source_sync_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


