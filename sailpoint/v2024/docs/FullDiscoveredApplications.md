# FullDiscoveredApplications

Discovered applications with their respective associated sources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the discovered application. | [optional] 
**name** | **str** | Name of the discovered application. | [optional] 
**discovery_source** | **str** | Source from which the application was discovered. | [optional] 
**discovered_vendor** | **str** | The vendor associated with the discovered application. | [optional] 
**description** | **str** | A brief description of the discovered application. | [optional] 
**recommended_connectors** | **List[str]** | List of recommended connectors for the application. | [optional] 
**discovered_at** | **datetime** | The timestamp when the application was last received via an entitlement aggregation invocation  or a manual csv upload, in ISO 8601 format. | [optional] 
**created_at** | **datetime** | The timestamp when the application was first discovered, in ISO 8601 format. | [optional] 
**status** | **str** | The status of an application within the discovery source.  By default this field is set to \&quot;ACTIVE\&quot; when the application is discovered.  If an application has been deleted from within the discovery source, the status will be set to \&quot;INACTIVE\&quot;. | [optional] 
**associated_sources** | **List[str]** | List of associated sources related to this discovered application. | [optional] 

## Example

```python
from sailpoint.v2024.models.full_discovered_applications import FullDiscoveredApplications

# TODO update the JSON string below
json = "{}"
# create an instance of FullDiscoveredApplications from a JSON string
full_discovered_applications_instance = FullDiscoveredApplications.from_json(json)
# print the JSON string representation of the object
print(FullDiscoveredApplications.to_json())

# convert the object into a dict
full_discovered_applications_dict = full_discovered_applications_instance.to_dict()
# create an instance of FullDiscoveredApplications from a dict
full_discovered_applications_from_dict = FullDiscoveredApplications.from_dict(full_discovered_applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

