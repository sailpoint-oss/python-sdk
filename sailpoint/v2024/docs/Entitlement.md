# Entitlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The entitlement id | [optional] 
**name** | **str** | The entitlement name | [optional] 
**attribute** | **str** | The entitlement attribute name | [optional] 
**value** | **str** | The value of the entitlement | [optional] 
**source_schema_object_type** | **str** | The object type of the entitlement from the source schema | [optional] 
**description** | **str** | The description of the entitlement | [optional] 
**privileged** | **bool** | True if the entitlement is privileged | [optional] 
**cloud_governed** | **bool** | True if the entitlement is cloud governed | [optional] 
**requestable** | **bool** | True if the entitlement is able to be directly requested | [optional] [default to False]
**owner** | [**EntitlementOwner**](EntitlementOwner.md) |  | [optional] 
**manually_updated_fields** | **Dict[str, object]** | A map of entitlement fields that have been manually updated. The key is the field name in UPPER_SNAKE_CASE format, and the value is true or false to indicate if the field has been updated. | [optional] 
**access_model_metadata** | [**EntitlementAccessModelMetadata**](EntitlementAccessModelMetadata.md) |  | [optional] 
**created** | **datetime** | Time when the entitlement was created | [optional] 
**modified** | **datetime** | Time when the entitlement was last modified | [optional] 
**source** | [**EntitlementSource**](EntitlementSource.md) |  | [optional] 
**attributes** | **Dict[str, object]** | A map of free-form key-value pairs from the source system | [optional] 
**segments** | **List[str]** | List of IDs of segments, if any, to which this Entitlement is assigned. | [optional] 
**direct_permissions** | [**List[PermissionDto]**](PermissionDto.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.entitlement import Entitlement

# TODO update the JSON string below
json = "{}"
# create an instance of Entitlement from a JSON string
entitlement_instance = Entitlement.from_json(json)
# print the JSON string representation of the object
print(Entitlement.to_json())

# convert the object into a dict
entitlement_dict = entitlement_instance.to_dict()
# create an instance of Entitlement from a dict
entitlement_from_dict = Entitlement.from_dict(entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


