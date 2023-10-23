# BaseEntitlement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**description** | **str** | A description of the entitlement | [optional] 
**attribute** | **str** | The name of the entitlement attribute | [optional] 
**value** | **str** | The value of the entitlement | [optional] 

## Example

```python
from v3.models.base_entitlement import BaseEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of BaseEntitlement from a JSON string
base_entitlement_instance = BaseEntitlement.from_json(json)
# print the JSON string representation of the object
print BaseEntitlement.to_json()

# convert the object into a dict
base_entitlement_dict = base_entitlement_instance.to_dict()
# create an instance of BaseEntitlement from a dict
base_entitlement_form_dict = base_entitlement.from_dict(base_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


