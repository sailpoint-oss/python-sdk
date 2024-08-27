# Entitlement1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The entitlement id | [optional] 
**name** | **str** | The entitlement name | [optional] 
**created** | **datetime** | Time when the entitlement was created | [optional] 
**modified** | **datetime** | Time when the entitlement was last modified | [optional] 
**attribute** | **str** | The entitlement attribute name | [optional] 
**value** | **str** | The value of the entitlement | [optional] 
**source_schema_object_type** | **str** | The object type of the entitlement from the source schema | [optional] 
**privileged** | **bool** | True if the entitlement is privileged | [optional] [default to False]
**cloud_governed** | **bool** | True if the entitlement is cloud governed | [optional] [default to False]
**description** | **str** | The description of the entitlement | [optional] 
**requestable** | **bool** | True if the entitlement is requestable | [optional] [default to False]
**attributes** | **Dict[str, object]** | A map of free-form key-value pairs from the source system | [optional] 
**source** | [**Entitlement1Source**](Entitlement1Source.md) |  | [optional] 
**owner** | [**Entitlement1Owner**](Entitlement1Owner.md) |  | [optional] 
**direct_permissions** | [**List[PermissionDto]**](PermissionDto.md) |  | [optional] 
**segments** | **List[str]** | List of IDs of segments, if any, to which this Entitlement is assigned. | [optional] 
**manually_updated_fields** | [**Entitlement1ManuallyUpdatedFields**](Entitlement1ManuallyUpdatedFields.md) |  | [optional] 
**access_model_metadata** | [**Entitlement1AccessModelMetadata**](Entitlement1AccessModelMetadata.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.entitlement1 import Entitlement1

# TODO update the JSON string below
json = "{}"
# create an instance of Entitlement1 from a JSON string
entitlement1_instance = Entitlement1.from_json(json)
# print the JSON string representation of the object
print(Entitlement1.to_json())

# convert the object into a dict
entitlement1_dict = entitlement1_instance.to_dict()
# create an instance of Entitlement1 from a dict
entitlement1_from_dict = Entitlement1.from_dict(entitlement1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


