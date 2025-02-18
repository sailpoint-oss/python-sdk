# RoleSummary

Role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** | Description of access item. | [optional] 
**type** | **str** | Type of the access item. | [optional] 
**owner** | [**DisplayReference**](DisplayReference.md) |  | [optional] 
**disabled** | **bool** |  | [optional] 
**revocable** | **bool** |  | [optional] 

## Example

```python
from sailpoint.v3.models.role_summary import RoleSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RoleSummary from a JSON string
role_summary_instance = RoleSummary.from_json(json)
# print the JSON string representation of the object
print(RoleSummary.to_json())

# convert the object into a dict
role_summary_dict = role_summary_instance.to_dict()
# create an instance of RoleSummary from a dict
role_summary_from_dict = RoleSummary.from_dict(role_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


