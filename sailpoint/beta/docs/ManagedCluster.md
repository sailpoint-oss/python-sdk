# ManagedCluster

Managed Cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ManagedCluster ID | 
**name** | **str** | ManagedCluster name | [optional] 
**pod** | **str** | ManagedCluster pod | [optional] 
**org** | **str** | ManagedCluster org | [optional] 
**type** | [**ManagedClusterTypes**](ManagedClusterTypes.md) |  | [optional] 
**configuration** | **Dict[str, Optional[str]]** | ManagedProcess configuration map | [optional] 
**key_pair** | [**ManagedClusterKeyPair**](ManagedClusterKeyPair.md) |  | [optional] 
**attributes** | [**ManagedClusterAttributes**](ManagedClusterAttributes.md) |  | [optional] 
**description** | **str** | ManagedCluster description | [optional] 
**redis** | [**ManagedClusterRedis**](ManagedClusterRedis.md) |  | [optional] 
**client_type** | [**ManagedClientType**](ManagedClientType.md) |  | 
**ccg_version** | **str** | CCG version used by the ManagedCluster | 
**pinned_config** | **bool** | boolean flag indiacting whether or not the cluster configuration is pinned | [optional] [default to False]
**log_configuration** | [**ClientLogConfiguration**](ClientLogConfiguration.md) |  | [optional] 
**operational** | **bool** | Whether or not the cluster is operational or not | [optional] [default to False]
**status** | **str** | Cluster status | [optional] 
**public_key_certificate** | **str** | Public key certificate | [optional] 
**public_key_thumbprint** | **str** | Public key thumbprint | [optional] 
**public_key** | **str** | Public key | [optional] 
**alert_key** | **str** | Key describing any immediate cluster alerts | [optional] 
**client_ids** | **List[str]** | List of clients in a cluster | [optional] 
**service_count** | **int** | Number of services bound to a cluster | [optional] [default to 0]
**cc_id** | **str** | CC ID only used in calling CC, will be removed without notice when Migration to CEGS is finished | [optional] [default to '0']
**created_at** | **datetime** | The date/time this cluster was created | [optional] 
**updated_at** | **datetime** | The date/time this cluster was last updated | [optional] 

## Example

```python
from sailpoint.beta.models.managed_cluster import ManagedCluster

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedCluster from a JSON string
managed_cluster_instance = ManagedCluster.from_json(json)
# print the JSON string representation of the object
print(ManagedCluster.to_json())

# convert the object into a dict
managed_cluster_dict = managed_cluster_instance.to_dict()
# create an instance of ManagedCluster from a dict
managed_cluster_from_dict = ManagedCluster.from_dict(managed_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


