# MultiHostIntegrationsManagementWorkgroup

Reference to management workgroup for the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Management workgroup ID. | [optional] 
**name** | **str** | Management workgroup&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_integrations_management_workgroup import MultiHostIntegrationsManagementWorkgroup

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostIntegrationsManagementWorkgroup from a JSON string
multi_host_integrations_management_workgroup_instance = MultiHostIntegrationsManagementWorkgroup.from_json(json)
# print the JSON string representation of the object
print(MultiHostIntegrationsManagementWorkgroup.to_json())

# convert the object into a dict
multi_host_integrations_management_workgroup_dict = multi_host_integrations_management_workgroup_instance.to_dict()
# create an instance of MultiHostIntegrationsManagementWorkgroup from a dict
multi_host_integrations_management_workgroup_from_dict = MultiHostIntegrationsManagementWorkgroup.from_dict(multi_host_integrations_management_workgroup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


