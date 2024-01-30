# LookupStep

The definition of an Identity according to the Reassignment Configuration service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reassigned_to_id** | **str** | The ID of the Identity who work is reassigned to | [optional] 
**reassigned_from_id** | **str** | The ID of the Identity who work is reassigned from | [optional] 
**reassignment_type** | [**ReassignmentTypeEnum**](ReassignmentTypeEnum.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.lookup_step import LookupStep

# TODO update the JSON string below
json = "{}"
# create an instance of LookupStep from a JSON string
lookup_step_instance = LookupStep.from_json(json)
# print the JSON string representation of the object
print LookupStep.to_json()

# convert the object into a dict
lookup_step_dict = lookup_step_instance.to_dict()
# create an instance of LookupStep from a dict
lookup_step_form_dict = lookup_step.from_dict(lookup_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


