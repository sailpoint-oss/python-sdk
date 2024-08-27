# OrgConfig

DTO class for OrgConfig data accessible by customer external org admin (\"ORG_ADMIN\") users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_name** | **str** | The name of the org. | [optional] 
**time_zone** | **str** | The selected time zone which is to be used for the org.  This directly affects when scheduled tasks are executed.  Valid options can be found at /beta/org-config/valid-time-zones | [optional] 
**lcs_change_honors_source_enable_feature** | **bool** | Flag to determine whether the LCS_CHANGE_HONORS_SOURCE_ENABLE_FEATURE flag is enabled for the current org. | [optional] 
**arm_customer_id** | **str** | ARM Customer ID | [optional] 
**arm_sap_system_id_mappings** | **str** | A list of IDN::sourceId to ARM::systemId mappings. | [optional] 
**arm_auth** | **str** | ARM authentication string | [optional] 
**arm_db** | **str** | ARM database name | [optional] 
**arm_sso_url** | **str** | ARM SSO URL | [optional] 
**iai_enable_certification_recommendations** | **bool** | Flag to determine whether IAI Certification Recommendations are enabled for the current org | [optional] 
**sod_report_configs** | [**List[ReportConfigDTO]**](ReportConfigDTO.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.org_config import OrgConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OrgConfig from a JSON string
org_config_instance = OrgConfig.from_json(json)
# print the JSON string representation of the object
print(OrgConfig.to_json())

# convert the object into a dict
org_config_dict = org_config_instance.to_dict()
# create an instance of OrgConfig from a dict
org_config_from_dict = OrgConfig.from_dict(org_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


