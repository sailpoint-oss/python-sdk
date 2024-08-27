# SourceManagementWorkgroup

Reference to management workgroup for the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Management workgroup ID. | [optional] 
**name** | **str** | Management workgroup&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.v3.models.source_management_workgroup import SourceManagementWorkgroup

# TODO update the JSON string below
json = "{}"
# create an instance of SourceManagementWorkgroup from a JSON string
source_management_workgroup_instance = SourceManagementWorkgroup.from_json(json)
# print the JSON string representation of the object
print(SourceManagementWorkgroup.to_json())

# convert the object into a dict
source_management_workgroup_dict = source_management_workgroup_instance.to_dict()
# create an instance of SourceManagementWorkgroup from a dict
source_management_workgroup_from_dict = SourceManagementWorkgroup.from_dict(source_management_workgroup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


