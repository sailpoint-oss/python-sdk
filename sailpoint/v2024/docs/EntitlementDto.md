# EntitlementDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | 
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 
**attribute** | **str** | Name of the entitlement attribute | [optional] 
**value** | **str** | Raw value of the entitlement | [optional] 
**description** | **str** | Entitlment description | [optional] 
**attributes** | **Dict[str, object]** | Entitlement attributes | [optional] 
**source_schema_object_type** | **str** | Schema objectType on the given application that maps to an Account Group | [optional] 
**privileged** | **bool** | Determines if this Entitlement is privileged. | [optional] 
**cloud_governed** | **bool** | Determines if this Entitlement is goverened in the cloud. | [optional] 
**source** | [**EntitlementSource**](EntitlementSource.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.entitlement_dto import EntitlementDto

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementDto from a JSON string
entitlement_dto_instance = EntitlementDto.from_json(json)
# print the JSON string representation of the object
print(EntitlementDto.to_json())

# convert the object into a dict
entitlement_dto_dict = entitlement_dto_instance.to_dict()
# create an instance of EntitlementDto from a dict
entitlement_dto_from_dict = EntitlementDto.from_dict(entitlement_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


