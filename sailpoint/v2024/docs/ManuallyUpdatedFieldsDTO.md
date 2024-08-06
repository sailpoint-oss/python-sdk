# ManuallyUpdatedFieldsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **bool** | True if the entitlements name was updated manually via entitlement import csv or patch endpoint.  False means that property value has not been change after first entitlement aggregation. Field refers to [Entitlement response schema](https://developer.sailpoint.com/idn/api/beta/get-entitlement) &gt; &#x60;name&#x60; property. | [optional] [default to False]
**description** | **bool** | True if the entitlement description was updated manually via entitlement import csv or patch endpoint.  False means that property value has not been change after first entitlement aggregation. Field refers to [Entitlement response schema](https://developer.sailpoint.com/idn/api/beta/get-entitlement) &gt; &#x60;description&#x60; property. | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.manually_updated_fields_dto import ManuallyUpdatedFieldsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ManuallyUpdatedFieldsDTO from a JSON string
manually_updated_fields_dto_instance = ManuallyUpdatedFieldsDTO.from_json(json)
# print the JSON string representation of the object
print ManuallyUpdatedFieldsDTO.to_json()

# convert the object into a dict
manually_updated_fields_dto_dict = manually_updated_fields_dto_instance.to_dict()
# create an instance of ManuallyUpdatedFieldsDTO from a dict
manually_updated_fields_dto_form_dict = manually_updated_fields_dto.from_dict(manually_updated_fields_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


