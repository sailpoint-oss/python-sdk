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
**manager_correlation_mapping** | [**SourceManagerCorrelationMapping**](SourceManagerCorrelationMapping.md) |  | [optional] 
**manager_correlation_rule** | [**SourceManagerCorrelationRule**](SourceManagerCorrelationRule.md) |  | [optional] 
**before_provisioning_rule** | [**SourceBeforeProvisioningRule**](SourceBeforeProvisioningRule.md) |  | [optional] 
**schemas** | [**List[SourceSchemasInner]**](SourceSchemasInner.md) | List of references to Schema objects | [optional] 
**password_policies** | [**List[SourcePasswordPoliciesInner]**](SourcePasswordPoliciesInner.md) | List of references to the associated PasswordPolicy objects. | [optional] 
**features** | **List[str]** | Optional features that can be supported by a source. Modifying the features array may cause source configuration errors that are unsupportable. It is recommended to not modify this array for SailPoint supported connectors. * AUTHENTICATE: The source supports pass-through authentication. * COMPOSITE: The source supports composite source creation. * DIRECT_PERMISSIONS: The source supports returning DirectPermissions. * DISCOVER_SCHEMA: The source supports discovering schemas for users and groups. * ENABLE The source supports reading if an account is enabled or disabled. * MANAGER_LOOKUP: The source supports looking up managers as they are encountered in a feed. This is the opposite of NO_RANDOM_ACCESS. * NO_RANDOM_ACCESS: The source does not support random access and the getObject() methods should not be called and expected to perform. * PROXY: The source can serve as a proxy for another source. When an source has a proxy, all connector calls made with that source are redirected through the connector for the proxy source. * SEARCH * TEMPLATE * UNLOCK: The source supports reading if an account is locked or unlocked. * UNSTRUCTURED_TARGETS: The source supports returning unstructured Targets. * SHAREPOINT_TARGET: The source supports returning unstructured Target data for SharePoint. It will be typically used by AD, LDAP sources. * PROVISIONING: The source can both read and write accounts. Having this feature implies that the provision() method is implemented. It also means that direct and target permissions can also be provisioned if they can be returned by aggregation. * GROUP_PROVISIONING: The source can both read and write groups. Having this feature implies that the provision() method is implemented. * SYNC_PROVISIONING: The source can provision accounts synchronously. * PASSWORD: The source can provision password changes. Since sources can never read passwords, this is should only be used in conjunction with the PROVISIONING feature. * CURRENT_PASSWORD: Some source types support verification of the current password * ACCOUNT_ONLY_REQUEST: The source supports requesting accounts without entitlements. * ADDITIONAL_ACCOUNT_REQUEST: The source supports requesting additional accounts. * NO_AGGREGATION: A source that does not support aggregation. * GROUPS_HAVE_MEMBERS: The source models group memberships with a member attribute on the group object rather than a groups attribute on the account object. This effects the implementation of delta account aggregation. * NO_PERMISSIONS_PROVISIONING: Indicates that the connector cannot provision direct or target permissions for accounts. When DIRECT_PERMISSIONS and PROVISIONING features are present, it is assumed that the connector can also provision direct permissions. This feature disables that assumption and causes permission request to be converted to work items for accounts. * NO_GROUP_PERMISSIONS_PROVISIONING: Indicates that the connector cannot provision direct or target permissions for groups. When DIRECT_PERMISSIONS and PROVISIONING features are present, it is assumed that the connector can also provision direct permissions. This feature disables that assumption and causes permission request to be converted to work items for groups. * NO_UNSTRUCTURED_TARGETS_PROVISIONING: This string will be replaced by NO_GROUP_PERMISSIONS_PROVISIONING and NO_PERMISSIONS_PROVISIONING. * NO_DIRECT_PERMISSIONS_PROVISIONING: This string will be replaced by NO_GROUP_PERMISSIONS_PROVISIONING and NO_PERMISSIONS_PROVISIONING. * USES_UUID: Connectivity 2.0 flag used to indicate that the connector supports a compound naming structure. * PREFER_UUID: Used in ISC Provisioning AND Aggregation to decide if it should prefer account.uuid to account.nativeIdentity when data is read in through aggregation OR pushed out through provisioning. * ARM_SECURITY_EXTRACT: Indicates the application supports Security extracts for ARM * ARM_UTILIZATION_EXTRACT: Indicates the application supports Utilization extracts for ARM * ARM_CHANGELOG_EXTRACT: Indicates the application supports Change-log extracts for ARM | [optional] 
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
**created** | **datetime** | The date-time when the source was created | [optional] 
**modified** | **datetime** | The date-time when the source was last modified | [optional] 
**credential_provider_enabled** | **bool** | Enables credential provider for this source. If credentialProvider is turned on  then source can use credential provider(s) to fetch credentials. | [optional] [default to False]
**category** | **str** | The category of source (e.g. null, CredentialProvider) | [optional] 

## Example

```python
from sailpoint.v3.models.source import Source

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


