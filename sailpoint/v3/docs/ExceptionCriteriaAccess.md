# ExceptionCriteriaAccess

Access reference with addition of boolean existing flag to indicate whether the access was extant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
**existing** | **bool** | Whether the subject identity already had that access or not | [optional] [default to False]

## Example

```python
from sailpoint.v3.models.exception_criteria_access import ExceptionCriteriaAccess

# TODO update the JSON string below
json = "{}"
# create an instance of ExceptionCriteriaAccess from a JSON string
exception_criteria_access_instance = ExceptionCriteriaAccess.from_json(json)
# print the JSON string representation of the object
print ExceptionCriteriaAccess.to_json()

# convert the object into a dict
exception_criteria_access_dict = exception_criteria_access_instance.to_dict()
# create an instance of ExceptionCriteriaAccess from a dict
exception_criteria_access_form_dict = exception_criteria_access.from_dict(exception_criteria_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


