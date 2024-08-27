# ManagedClusterRequest

Request to create Managed Cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | ManagedCluster name | 
**type** | [**ManagedClusterTypes**](ManagedClusterTypes.md) |  | [optional] 
**configuration** | **Dict[str, str]** | ManagedProcess configuration map | [optional] 
**description** | **str** | ManagedCluster description | [optional] 

## Example

```python
from sailpoint.v2024.models.managed_cluster_request import ManagedClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedClusterRequest from a JSON string
managed_cluster_request_instance = ManagedClusterRequest.from_json(json)
# print the JSON string representation of the object
print(ManagedClusterRequest.to_json())

# convert the object into a dict
managed_cluster_request_dict = managed_cluster_request_instance.to_dict()
# create an instance of ManagedClusterRequest from a dict
managed_cluster_request_from_dict = ManagedClusterRequest.from_dict(managed_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


