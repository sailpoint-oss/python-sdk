# ViolationPrediction

An object containing a listing of the SOD violation reasons detected by this check.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**violation_contexts** | [**List[ViolationContext]**](ViolationContext.md) | List of Violation Contexts | [optional] 

## Example

```python
from sailpoint.v3.models.violation_prediction import ViolationPrediction

# TODO update the JSON string below
json = "{}"
# create an instance of ViolationPrediction from a JSON string
violation_prediction_instance = ViolationPrediction.from_json(json)
# print the JSON string representation of the object
print ViolationPrediction.to_json()

# convert the object into a dict
violation_prediction_dict = violation_prediction_instance.to_dict()
# create an instance of ViolationPrediction from a dict
violation_prediction_form_dict = violation_prediction.from_dict(violation_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


