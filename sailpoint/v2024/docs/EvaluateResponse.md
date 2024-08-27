# EvaluateResponse

The response body for Evaluate Reassignment Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reassign_to_id** | **str** | The Identity ID which should be the recipient of any work items sent to a specific identity &amp; work type | [optional] 
**lookup_trail** | [**List[LookupStep]**](LookupStep.md) | List of Reassignments found by looking up the next &#x60;TargetIdentity&#x60; in a ReassignmentConfiguration | [optional] 

## Example

```python
from sailpoint.v2024.models.evaluate_response import EvaluateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluateResponse from a JSON string
evaluate_response_instance = EvaluateResponse.from_json(json)
# print the JSON string representation of the object
print(EvaluateResponse.to_json())

# convert the object into a dict
evaluate_response_dict = evaluate_response_instance.to_dict()
# create an instance of EvaluateResponse from a dict
evaluate_response_from_dict = EvaluateResponse.from_dict(evaluate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


