# ManagedClusterAttributes

Managed Cluster Attributes for Cluster Configuration. Supported Cluster Types [sqsCluster, spConnectCluster]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue** | [**ManagedClusterQueue**](ManagedClusterQueue.md) |  | [optional] 
**keystore** | **str** | ManagedCluster keystore for spConnectCluster type | [optional] 

## Example

```python
from sailpoint.v3.models.managed_cluster_attributes import ManagedClusterAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedClusterAttributes from a JSON string
managed_cluster_attributes_instance = ManagedClusterAttributes.from_json(json)
# print the JSON string representation of the object
print ManagedClusterAttributes.to_json()

# convert the object into a dict
managed_cluster_attributes_dict = managed_cluster_attributes_instance.to_dict()
# create an instance of ManagedClusterAttributes from a dict
managed_cluster_attributes_form_dict = managed_cluster_attributes.from_dict(managed_cluster_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


