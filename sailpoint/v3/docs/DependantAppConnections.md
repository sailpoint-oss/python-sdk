# DependantAppConnections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_app_id** | **str** | Id of the connected Application | [optional] 
**description** | **str** | Description of the connected Application | [optional] 
**enabled** | **bool** | Is the Application enabled | [optional] [default to True]
**provision_request_enabled** | **bool** | Is Provisioning enabled for connected Application | [optional] [default to True]
**account_source** | [**DependantAppConnectionsAccountSource**](DependantAppConnectionsAccountSource.md) |  | [optional] 
**launcher_count** | **int** | The amount of launchers for connected Application (long type) | [optional] 
**match_all_account** | **bool** | Is Provisioning enabled for connected Application | [optional] [default to False]
**owner** | [**List[BaseReferenceDto]**](BaseReferenceDto.md) | The owner of the connected Application | [optional] 
**app_center_enabled** | **bool** | Is App Center enabled for connected Application | [optional] [default to False]

## Example

```python
from sailpoint.v3.models.dependant_app_connections import DependantAppConnections

# TODO update the JSON string below
json = "{}"
# create an instance of DependantAppConnections from a JSON string
dependant_app_connections_instance = DependantAppConnections.from_json(json)
# print the JSON string representation of the object
print(DependantAppConnections.to_json())

# convert the object into a dict
dependant_app_connections_dict = dependant_app_connections_instance.to_dict()
# create an instance of DependantAppConnections from a dict
dependant_app_connections_from_dict = DependantAppConnections.from_dict(dependant_app_connections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


