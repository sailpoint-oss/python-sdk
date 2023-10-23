# ManagedClient

Managed Client

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ManagedClient ID | [optional] [readonly] 
**alert_key** | **str** | ManagedClient alert key | [optional] [readonly] 
**api_gateway_base_url** | **str** | ManagedClient gateway base url | [optional] [readonly] 
**cc_id** | **int** | Previous CC ID to be used in data migration. (This field will be deleted after CC migration!) | [optional] 
**client_id** | **str** | The client ID used in API management | 
**cluster_id** | **str** | Cluster ID that the ManagedClient is linked to | 
**cookbook** | **str** | VA cookbook | [optional] [readonly] 
**description** | **str** | ManagedClient description | 
**ip_address** | **str** | The public IP address of the ManagedClient | [optional] [readonly] 
**last_seen** | **datetime** | When the ManagedClient was last seen by the server | [optional] [readonly] 
**name** | **str** | ManagedClient name | [optional] 
**since_last_seen** | **str** | Milliseconds since the ManagedClient has polled the server | [optional] [readonly] 
**status** | [**ManagedClientStatusEnum**](ManagedClientStatusEnum.md) |  | [optional] [readonly] 
**type** | **str** | Type of the ManagedClient (VA, CCG) | 
**va_download_url** | **str** | ManagedClient VA download URL | [optional] [readonly] 
**va_version** | **str** | Version that the ManagedClient&#39;s VA is running | [optional] [readonly] 
**secret** | **str** | Client&#39;s apiKey | [optional] 

## Example

```python
from beta.models.managed_client import ManagedClient

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedClient from a JSON string
managed_client_instance = ManagedClient.from_json(json)
# print the JSON string representation of the object
print ManagedClient.to_json()

# convert the object into a dict
managed_client_dict = managed_client_instance.to_dict()
# create an instance of ManagedClient from a dict
managed_client_form_dict = managed_client.from_dict(managed_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


