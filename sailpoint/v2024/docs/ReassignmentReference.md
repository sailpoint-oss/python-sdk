# ReassignmentReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of item or identity being reassigned. | 
**type** | **str** | The type of item or identity being reassigned. | 

## Example

```python
from sailpoint.v2024.models.reassignment_reference import ReassignmentReference

# TODO update the JSON string below
json = "{}"
# create an instance of ReassignmentReference from a JSON string
reassignment_reference_instance = ReassignmentReference.from_json(json)
# print the JSON string representation of the object
print(ReassignmentReference.to_json())

# convert the object into a dict
reassignment_reference_dict = reassignment_reference_instance.to_dict()
# create an instance of ReassignmentReference from a dict
reassignment_reference_from_dict = ReassignmentReference.from_dict(reassignment_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


