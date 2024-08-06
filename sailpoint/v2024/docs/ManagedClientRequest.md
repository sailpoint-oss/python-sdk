# ManagedClientRequest

Managed Client Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Cluster ID that the ManagedClient is linked to | 
**description** | **str** | description for the ManagedClient to create | [optional] 
**name** | **str** | name for the ManagedClient to create | [optional] 
**type** | **str** | Type of the ManagedClient (VA, CCG) to create | [optional] 

## Example

```python
from sailpoint.v2024.models.managed_client_request import ManagedClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedClientRequest from a JSON string
managed_client_request_instance = ManagedClientRequest.from_json(json)
# print the JSON string representation of the object
print ManagedClientRequest.to_json()

# convert the object into a dict
managed_client_request_dict = managed_client_request_instance.to_dict()
# create an instance of ManagedClientRequest from a dict
managed_client_request_form_dict = managed_client_request.from_dict(managed_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


