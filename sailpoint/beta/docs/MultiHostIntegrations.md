# MultiHostIntegrations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Multi-Host Integration ID. | [readonly] 
**name** | **str** | Multi-Host Integration&#39;s human-readable name. | 
**description** | **str** | Multi-Host Integration&#39;s human-readable description. | 
**owner** | [**MultiHostIntegrationsOwner**](MultiHostIntegrationsOwner.md) |  | 
**cluster** | [**MultiHostIntegrationsCluster**](MultiHostIntegrationsCluster.md) |  | [optional] 
**type** | **str** | Specifies the type of system being managed e.g. Workday, Multi-Host - Microsoft SQL Server, etc.. If you are creating a delimited file source, you must set the &#x60;provisionasCsv&#x60; query parameter to &#x60;true&#x60;.  | [optional] 
**connector** | **str** | Connector script name. | 
**last_source_upload_success_count** | **int** | Last successfully uploaded source count of given Multi-Host Integration. | [optional] 
**max_sources_per_agg_group** | **int** | Maximum sources that can contain in a aggregation group of Multi-Host Integration. | [optional] 
**connector_class** | **str** | Fully qualified name of the Java class that implements the connector interface. | [optional] 
**connector_attributes** | [**MultiHostIntegrationsConnectorAttributes**](MultiHostIntegrationsConnectorAttributes.md) |  | [optional] 
**delete_threshold** | **int** | Number from 0 to 100 that specifies when to skip the delete phase. | [optional] 
**authoritative** | **bool** | When this is true, it indicates that the source is referenced by an identity profile. | [optional] [default to False]
**management_workgroup** | [**MultiHostIntegrationsManagementWorkgroup**](MultiHostIntegrationsManagementWorkgroup.md) |  | [optional] 
**healthy** | **bool** | When this is true, it indicates that the source is healthy. | [optional] [default to False]
**status** | **str** | Status identifier that gives specific information about why a source is or isn&#39;t healthy.  | [optional] 
**since** | **datetime** | Timestamp that shows when a source health check was last performed. | [optional] 
**connector_id** | **str** | Connector ID | [optional] 
**connector_name** | **str** | Name of the connector that was chosen during source creation. | [optional] 
**connection_type** | **str** | Type of connection (direct or file). | [optional] 
**connector_implementation_id** | **str** | Connector implementation ID. | [optional] 
**created** | **datetime** | Date-time when the source was created | [optional] 
**modified** | **datetime** | Date-time when the source was last modified. | [optional] 
**credential_provider_enabled** | **bool** | If this is true, it enables a credential provider for the source. If credentialProvider is turned on,  then the source can use credential provider(s) to fetch credentials. | [optional] [default to False]
**category** | **str** | Source category (e.g. null, CredentialProvider). | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_integrations import MultiHostIntegrations

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostIntegrations from a JSON string
multi_host_integrations_instance = MultiHostIntegrations.from_json(json)
# print the JSON string representation of the object
print(MultiHostIntegrations.to_json())

# convert the object into a dict
multi_host_integrations_dict = multi_host_integrations_instance.to_dict()
# create an instance of MultiHostIntegrations from a dict
multi_host_integrations_from_dict = MultiHostIntegrations.from_dict(multi_host_integrations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


