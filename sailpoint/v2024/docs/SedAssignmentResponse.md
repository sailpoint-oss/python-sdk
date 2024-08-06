# SedAssignmentResponse

Sed Assignment Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | BatchId that groups all the ids together | [optional] 

## Example

```python
from sailpoint.v2024.models.sed_assignment_response import SedAssignmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SedAssignmentResponse from a JSON string
sed_assignment_response_instance = SedAssignmentResponse.from_json(json)
# print the JSON string representation of the object
print SedAssignmentResponse.to_json()

# convert the object into a dict
sed_assignment_response_dict = sed_assignment_response_instance.to_dict()
# create an instance of SedAssignmentResponse from a dict
sed_assignment_response_form_dict = sed_assignment_response.from_dict(sed_assignment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


