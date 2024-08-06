# EntitlementSourceResetBaseReferenceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The DTO type | [optional] 
**id** | **str** | The task ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from sailpoint.v2024.models.entitlement_source_reset_base_reference_dto import EntitlementSourceResetBaseReferenceDto

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementSourceResetBaseReferenceDto from a JSON string
entitlement_source_reset_base_reference_dto_instance = EntitlementSourceResetBaseReferenceDto.from_json(json)
# print the JSON string representation of the object
print EntitlementSourceResetBaseReferenceDto.to_json()

# convert the object into a dict
entitlement_source_reset_base_reference_dto_dict = entitlement_source_reset_base_reference_dto_instance.to_dict()
# create an instance of EntitlementSourceResetBaseReferenceDto from a dict
entitlement_source_reset_base_reference_dto_form_dict = entitlement_source_reset_base_reference_dto.from_dict(entitlement_source_reset_base_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


