# SedAssignment

Sed Assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**SedAssignee**](SedAssignee.md) |  | [optional] 
**items** | **List[str]** | List of SED id&#39;s | [optional] 

## Example

```python
from sailpoint.v2024.models.sed_assignment import SedAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of SedAssignment from a JSON string
sed_assignment_instance = SedAssignment.from_json(json)
# print the JSON string representation of the object
print SedAssignment.to_json()

# convert the object into a dict
sed_assignment_dict = sed_assignment_instance.to_dict()
# create an instance of SedAssignment from a dict
sed_assignment_form_dict = sed_assignment.from_dict(sed_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


