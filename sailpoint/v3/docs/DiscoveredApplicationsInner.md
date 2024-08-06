# DiscoveredApplicationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the discovered application. | [optional] 
**name** | **str** | Name of the discovered application. | [optional] 
**discovery_source** | **str** | Source from which the application was discovered. | [optional] 
**discovered_vendor** | **str** | The vendor associated with the discovered application. | [optional] 
**description** | **str** | A brief description of the discovered application. | [optional] 
**recommended_connectors** | **List[str]** | List of recommended connectors for the application. | [optional] 
**discovered_timestamp** | **datetime** | The timestamp when the application was discovered, in ISO 8601 format. | [optional] 

## Example

```python
from sailpoint.v3.models.discovered_applications_inner import DiscoveredApplicationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveredApplicationsInner from a JSON string
discovered_applications_inner_instance = DiscoveredApplicationsInner.from_json(json)
# print the JSON string representation of the object
print DiscoveredApplicationsInner.to_json()

# convert the object into a dict
discovered_applications_inner_dict = discovered_applications_inner_instance.to_dict()
# create an instance of DiscoveredApplicationsInner from a dict
discovered_applications_inner_form_dict = discovered_applications_inner.from_dict(discovered_applications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


