# AssignmentContextDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested** | [**AccessRequestContext**](AccessRequestContext.md) |  | [optional] 
**matched** | [**List[RoleMatchDto]**](RoleMatchDto.md) |  | [optional] 
**computed_date** | **str** | Date that the assignment will was evaluated | [optional] 

## Example

```python
from sailpoint.v2024.models.assignment_context_dto import AssignmentContextDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentContextDto from a JSON string
assignment_context_dto_instance = AssignmentContextDto.from_json(json)
# print the JSON string representation of the object
print(AssignmentContextDto.to_json())

# convert the object into a dict
assignment_context_dto_dict = assignment_context_dto_instance.to_dict()
# create an instance of AssignmentContextDto from a dict
assignment_context_dto_from_dict = AssignmentContextDto.from_dict(assignment_context_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


