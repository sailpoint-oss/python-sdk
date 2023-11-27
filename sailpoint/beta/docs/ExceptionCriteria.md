# ExceptionCriteria


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria_list** | [**List[ExceptionCriteriaCriteriaListInner]**](ExceptionCriteriaCriteriaListInner.md) | List of exception criteria. There is a min of 1 and max of 50 items in the list. | [optional] 

## Example

```python
from sailpoint.beta.models.exception_criteria import ExceptionCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ExceptionCriteria from a JSON string
exception_criteria_instance = ExceptionCriteria.from_json(json)
# print the JSON string representation of the object
print ExceptionCriteria.to_json()

# convert the object into a dict
exception_criteria_dict = exception_criteria_instance.to_dict()
# create an instance of ExceptionCriteria from a dict
exception_criteria_form_dict = exception_criteria.from_dict(exception_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


