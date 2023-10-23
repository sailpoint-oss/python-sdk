# SourceManagementWorkgroup

Reference to Management Workgroup for this Source

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | [optional] 
**id** | **str** | ID of the management workgroup | [optional] 
**name** | **str** | Human-readable display name of the management workgroup | [optional] 

## Example

```python
from beta.models.source_management_workgroup import SourceManagementWorkgroup

# TODO update the JSON string below
json = "{}"
# create an instance of SourceManagementWorkgroup from a JSON string
source_management_workgroup_instance = SourceManagementWorkgroup.from_json(json)
# print the JSON string representation of the object
print SourceManagementWorkgroup.to_json()

# convert the object into a dict
source_management_workgroup_dict = source_management_workgroup_instance.to_dict()
# create an instance of SourceManagementWorkgroup from a dict
source_management_workgroup_form_dict = source_management_workgroup.from_dict(source_management_workgroup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


