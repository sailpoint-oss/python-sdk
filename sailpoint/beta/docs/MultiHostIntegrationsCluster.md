# MultiHostIntegrationsCluster

Reference to the source's associated cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | 
**id** | **str** | Cluster ID. | 
**name** | **str** | Cluster&#39;s human-readable display name. | 

## Example

```python
from sailpoint.beta.models.multi_host_integrations_cluster import MultiHostIntegrationsCluster

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostIntegrationsCluster from a JSON string
multi_host_integrations_cluster_instance = MultiHostIntegrationsCluster.from_json(json)
# print the JSON string representation of the object
print(MultiHostIntegrationsCluster.to_json())

# convert the object into a dict
multi_host_integrations_cluster_dict = multi_host_integrations_cluster_instance.to_dict()
# create an instance of MultiHostIntegrationsCluster from a dict
multi_host_integrations_cluster_from_dict = MultiHostIntegrationsCluster.from_dict(multi_host_integrations_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


