# ReassignmentTrailDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_owner** | **str** | The ID of previous owner identity. | [optional] 
**new_owner** | **str** | The ID of new owner identity. | [optional] 
**reassignment_type** | **str** | The type of reassignment. | [optional] 

## Example

```python
from sailpoint.v3.models.reassignment_trail_dto import ReassignmentTrailDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ReassignmentTrailDTO from a JSON string
reassignment_trail_dto_instance = ReassignmentTrailDTO.from_json(json)
# print the JSON string representation of the object
print ReassignmentTrailDTO.to_json()

# convert the object into a dict
reassignment_trail_dto_dict = reassignment_trail_dto_instance.to_dict()
# create an instance of ReassignmentTrailDTO from a dict
reassignment_trail_dto_form_dict = reassignment_trail_dto.from_dict(reassignment_trail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


