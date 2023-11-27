# IdentitySyncPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Payload type. | 
**data_json** | **str** | Payload type. | 

## Example

```python
from sailpoint.beta.models.identity_sync_payload import IdentitySyncPayload

# TODO update the JSON string below
json = "{}"
# create an instance of IdentitySyncPayload from a JSON string
identity_sync_payload_instance = IdentitySyncPayload.from_json(json)
# print the JSON string representation of the object
print IdentitySyncPayload.to_json()

# convert the object into a dict
identity_sync_payload_dict = identity_sync_payload_instance.to_dict()
# create an instance of IdentitySyncPayload from a dict
identity_sync_payload_form_dict = identity_sync_payload.from_dict(identity_sync_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


