# AccessRequestPhases

Provides additional details about this access request phase.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started** | **datetime** | The time that this phase started. | [optional] 
**finished** | **datetime** | The time that this phase finished. | [optional] 
**name** | **str** | The name of this phase. | [optional] 
**state** | **str** | The state of this phase. | [optional] 
**result** | **str** | The state of this phase. | [optional] 
**phase_reference** | **str** | A reference to another object on the RequestedItemStatus that contains more details about the phase. Note that for the Provisioning phase, this will be empty if there are no manual work items. | [optional] 

## Example

```python
from sailpoint.v3.models.access_request_phases import AccessRequestPhases

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestPhases from a JSON string
access_request_phases_instance = AccessRequestPhases.from_json(json)
# print the JSON string representation of the object
print(AccessRequestPhases.to_json())

# convert the object into a dict
access_request_phases_dict = access_request_phases_instance.to_dict()
# create an instance of AccessRequestPhases from a dict
access_request_phases_from_dict = AccessRequestPhases.from_dict(access_request_phases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


