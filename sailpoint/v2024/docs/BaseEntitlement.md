# BaseEntitlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_permissions** | **bool** | Indicates whether the entitlement has permissions. | [optional] [default to False]
**description** | **str** | Entitlement&#39;s description. | [optional] 
**attribute** | **str** | Entitlement attribute&#39;s name. | [optional] 
**value** | **str** | Entitlement&#39;s value. | [optional] 
**var_schema** | **str** | Entitlement&#39;s schema. | [optional] 
**privileged** | **bool** | Indicates whether the entitlement is privileged. | [optional] [default to False]
**id** | **str** | Entitlement&#39;s ID. | [optional] 
**name** | **str** | Entitlement&#39;s name. | [optional] 

## Example

```python
from sailpoint.v2024.models.base_entitlement import BaseEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of BaseEntitlement from a JSON string
base_entitlement_instance = BaseEntitlement.from_json(json)
# print the JSON string representation of the object
print(BaseEntitlement.to_json())

# convert the object into a dict
base_entitlement_dict = base_entitlement_instance.to_dict()
# create an instance of BaseEntitlement from a dict
base_entitlement_from_dict = BaseEntitlement.from_dict(base_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


