# ViolationContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**ViolationContextPolicy**](ViolationContextPolicy.md) |  | [optional] 
**conflicting_access_criteria** | [**ExceptionAccessCriteria**](ExceptionAccessCriteria.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.violation_context import ViolationContext

# TODO update the JSON string below
json = "{}"
# create an instance of ViolationContext from a JSON string
violation_context_instance = ViolationContext.from_json(json)
# print the JSON string representation of the object
print(ViolationContext.to_json())

# convert the object into a dict
violation_context_dict = violation_context_instance.to_dict()
# create an instance of ViolationContext from a dict
violation_context_from_dict = ViolationContext.from_dict(violation_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


