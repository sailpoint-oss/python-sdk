# ManagedClusterRedis

Managed Cluster Redis Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redis_host** | **str** | ManagedCluster redisHost | [optional] 
**redis_port** | **int** | ManagedCluster redisPort | [optional] 

## Example

```python
from beta.models.managed_cluster_redis import ManagedClusterRedis

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedClusterRedis from a JSON string
managed_cluster_redis_instance = ManagedClusterRedis.from_json(json)
# print the JSON string representation of the object
print ManagedClusterRedis.to_json()

# convert the object into a dict
managed_cluster_redis_dict = managed_cluster_redis_instance.to_dict()
# create an instance of ManagedClusterRedis from a dict
managed_cluster_redis_form_dict = managed_cluster_redis.from_dict(managed_cluster_redis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


