# MachineIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | 
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 
**business_application** | **str** | The business application that the identity represents | 
**description** | **str** | Description of machine identity | [optional] 
**manually_edited** | **bool** | Indicates if the machine identity has been manually edited | [optional] [default to False]
**attributes** | **object** | A map of custom machine identity attributes | [optional] 

## Example

```python
from sailpoint.v2024.models.machine_identity import MachineIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of MachineIdentity from a JSON string
machine_identity_instance = MachineIdentity.from_json(json)
# print the JSON string representation of the object
print(MachineIdentity.to_json())

# convert the object into a dict
machine_identity_dict = machine_identity_instance.to_dict()
# create an instance of MachineIdentity from a dict
machine_identity_from_dict = MachineIdentity.from_dict(machine_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


