# SodViolationCheck

An object referencing an SOD violation check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The id of the original request | 
**created** | **datetime** | The date-time when this request was created. | [optional] [readonly] 

## Example

```python
from sailpoint.v3.models.sod_violation_check import SodViolationCheck

# TODO update the JSON string below
json = "{}"
# create an instance of SodViolationCheck from a JSON string
sod_violation_check_instance = SodViolationCheck.from_json(json)
# print the JSON string representation of the object
print SodViolationCheck.to_json()

# convert the object into a dict
sod_violation_check_dict = sod_violation_check_instance.to_dict()
# create an instance of SodViolationCheck from a dict
sod_violation_check_form_dict = sod_violation_check.from_dict(sod_violation_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


