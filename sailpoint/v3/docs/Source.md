# Source


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id of the Source | [optional] [readonly] 
**name** | **str** | Human-readable name of the source | 
**description** | **str** | Human-readable description of the source | [optional] 
**owner** | [**SourceOwner**](SourceOwner.md) |  | 
**cluster** | [**SourceCluster**](SourceCluster.md) |  | [optional] 
**account_correlation_config** | [**SourceAccountCorrelationConfig**](SourceAccountCorrelationConfig.md) |  | [optional] 
**account_correlation_rule** | [**SourceAccountCorrelationRule**](SourceAccountCorrelationRule.md) |  | [optional] 
**manager_correlation_mapping** | [**ManagerCorrelationMapping**](ManagerCorrelationMapping.md) |  | [optional] 
**manager_correlation_rule** | [**SourceManagerCorrelationRule**](SourceManagerCorrelationRule.md) |  | [optional] 
**before_provisioning_rule** | [**SourceBeforeProvisioningRule**](SourceBeforeProvisioningRule.md) |  | [optional] 
**schemas** | [**List[SourceSchemasInner]**](SourceSchemasInner.md) | List of references to Schema objects | [optional] 
**password_policies** | [**List[SourcePasswordPoliciesInner]**](SourcePasswordPoliciesInner.md) | List of references to the associated PasswordPolicy objects. | [optional] 
**features** | [**List[SourceFeature]**](SourceFeature.md) | Optional features that can be supported by a source. | [optional] 
**type** | **str** | Specifies the type of system being managed e.g. Active Directory, Workday, etc.. If you are creating a Delimited File source, you must set the &#x60;provisionasCsv&#x60; query parameter to &#x60;true&#x60;.  | [optional] 
**connector** | **str** | Connector script name. | 
**connector_class** | **str** | The fully qualified name of the Java class that implements the connector interface. | [optional] 
**connector_attributes** | **object** | Connector specific configuration; will differ from type to type. | [optional] 
**delete_threshold** | **int** | Number from 0 to 100 that specifies when to skip the delete phase. | [optional] 
**authoritative** | **bool** | When true indicates the source is referenced by an IdentityProfile. | [optional] [default to False]
**management_workgroup** | [**SourceManagementWorkgroup**](SourceManagementWorkgroup.md) |  | [optional] 
**healthy** | **bool** | When true indicates a healthy source | [optional] [default to False]
**status** | **str** | A status identifier, giving specific information on why a source is healthy or not | [optional] 
**since** | **str** | Timestamp showing when a source health check was last performed | [optional] 
**connector_id** | **str** | The id of connector | [optional] 
**connector_name** | **str** | The name of the connector that was chosen on source creation | [optional] 
**connection_type** | **str** | The type of connection (direct or file) | [optional] 
**connector_implementation_id** | **str** | The connector implementation id | [optional] 

## Example

```python
from v3.models.source import Source

# TODO update the JSON string below
json = "{}"
# create an instance of Source from a JSON string
source_instance = Source.from_json(json)
# print the JSON string representation of the object
print Source.to_json()

# convert the object into a dict
source_dict = source_instance.to_dict()
# create an instance of Source from a dict
source_form_dict = source.from_dict(source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


