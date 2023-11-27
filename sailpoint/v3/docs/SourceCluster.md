# SourceCluster

Reference to the associated Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | 
**id** | **str** | ID of the cluster | 
**name** | **str** | Human-readable display name of the cluster | 

## Example

```python
from sailpoint.v3.models.source_cluster import SourceCluster

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCluster from a JSON string
source_cluster_instance = SourceCluster.from_json(json)
# print the JSON string representation of the object
print SourceCluster.to_json()

# convert the object into a dict
source_cluster_dict = source_cluster_instance.to_dict()
# create an instance of SourceCluster from a dict
source_cluster_form_dict = source_cluster.from_dict(source_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


