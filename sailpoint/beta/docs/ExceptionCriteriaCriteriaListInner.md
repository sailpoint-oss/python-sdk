# ExceptionCriteriaCriteriaListInner

The types of objects supported for SOD violations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
**existing** | **bool** | Whether the subject identity already had that access or not | [optional] 

## Example

```python
from sailpoint.beta.models.exception_criteria_criteria_list_inner import ExceptionCriteriaCriteriaListInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExceptionCriteriaCriteriaListInner from a JSON string
exception_criteria_criteria_list_inner_instance = ExceptionCriteriaCriteriaListInner.from_json(json)
# print the JSON string representation of the object
print ExceptionCriteriaCriteriaListInner.to_json()

# convert the object into a dict
exception_criteria_criteria_list_inner_dict = exception_criteria_criteria_list_inner_instance.to_dict()
# create an instance of ExceptionCriteriaCriteriaListInner from a dict
exception_criteria_criteria_list_inner_form_dict = exception_criteria_criteria_list_inner.from_dict(exception_criteria_criteria_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


