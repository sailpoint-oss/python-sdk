# SourceCluster

Reference to the source's associated cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | 
**id** | **str** | Cluster ID. | 
**name** | **str** | Cluster&#39;s human-readable display name. | 

## Example

```python
from sailpoint.v2024.models.source_cluster import SourceCluster

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCluster from a JSON string
source_cluster_instance = SourceCluster.from_json(json)
# print the JSON string representation of the object
print(SourceCluster.to_json())

# convert the object into a dict
source_cluster_dict = source_cluster_instance.to_dict()
# create an instance of SourceCluster from a dict
source_cluster_from_dict = SourceCluster.from_dict(source_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


