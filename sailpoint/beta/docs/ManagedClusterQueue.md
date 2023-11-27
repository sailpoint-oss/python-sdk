# ManagedClusterQueue

Managed Cluster key pair for Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | ManagedCluster queue name | [optional] 
**region** | **str** | ManagedCluster queue aws region | [optional] 

## Example

```python
from sailpoint.beta.models.managed_cluster_queue import ManagedClusterQueue

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedClusterQueue from a JSON string
managed_cluster_queue_instance = ManagedClusterQueue.from_json(json)
# print the JSON string representation of the object
print ManagedClusterQueue.to_json()

# convert the object into a dict
managed_cluster_queue_dict = managed_cluster_queue_instance.to_dict()
# create an instance of ManagedClusterQueue from a dict
managed_cluster_queue_form_dict = managed_cluster_queue.from_dict(managed_cluster_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


