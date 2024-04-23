# ManagedClusterKeyPair

Managed Cluster key pair for Cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** | ManagedCluster publicKey | [optional] 
**public_key_thumbprint** | **str** | ManagedCluster publicKeyThumbprint | [optional] 
**public_key_certificate** | **str** | ManagedCluster publicKeyCertificate | [optional] 

## Example

```python
from sailpoint.v3.models.managed_cluster_key_pair import ManagedClusterKeyPair

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedClusterKeyPair from a JSON string
managed_cluster_key_pair_instance = ManagedClusterKeyPair.from_json(json)
# print the JSON string representation of the object
print ManagedClusterKeyPair.to_json()

# convert the object into a dict
managed_cluster_key_pair_dict = managed_cluster_key_pair_instance.to_dict()
# create an instance of ManagedClusterKeyPair from a dict
managed_cluster_key_pair_form_dict = managed_cluster_key_pair.from_dict(managed_cluster_key_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


