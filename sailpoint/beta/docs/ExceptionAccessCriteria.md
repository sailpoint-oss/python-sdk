# ExceptionAccessCriteria


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_criteria** | [**ExceptionCriteria**](ExceptionCriteria.md) |  | [optional] 
**right_criteria** | [**ExceptionCriteria**](ExceptionCriteria.md) |  | [optional] 

## Example

```python
from beta.models.exception_access_criteria import ExceptionAccessCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ExceptionAccessCriteria from a JSON string
exception_access_criteria_instance = ExceptionAccessCriteria.from_json(json)
# print the JSON string representation of the object
print ExceptionAccessCriteria.to_json()

# convert the object into a dict
exception_access_criteria_dict = exception_access_criteria_instance.to_dict()
# create an instance of ExceptionAccessCriteria from a dict
exception_access_criteria_form_dict = exception_access_criteria.from_dict(exception_access_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


