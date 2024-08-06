# Entitlement1ManuallyUpdatedFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **bool** | True if the entitlements name was updated manually via entitlement import csv or patch endpoint.  False means that property value has not been change after first entitlement aggregation. Field refers to [Entitlement response schema](https://developer.sailpoint.com/idn/api/beta/get-entitlement) &gt; &#x60;name&#x60; property. | [optional] [default to False]
**description** | **bool** | True if the entitlement description was updated manually via entitlement import csv or patch endpoint.  False means that property value has not been change after first entitlement aggregation. Field refers to [Entitlement response schema](https://developer.sailpoint.com/idn/api/beta/get-entitlement) &gt; &#x60;description&#x60; property. | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.entitlement1_manually_updated_fields import Entitlement1ManuallyUpdatedFields

# TODO update the JSON string below
json = "{}"
# create an instance of Entitlement1ManuallyUpdatedFields from a JSON string
entitlement1_manually_updated_fields_instance = Entitlement1ManuallyUpdatedFields.from_json(json)
# print the JSON string representation of the object
print Entitlement1ManuallyUpdatedFields.to_json()

# convert the object into a dict
entitlement1_manually_updated_fields_dict = entitlement1_manually_updated_fields_instance.to_dict()
# create an instance of Entitlement1ManuallyUpdatedFields from a dict
entitlement1_manually_updated_fields_form_dict = entitlement1_manually_updated_fields.from_dict(entitlement1_manually_updated_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


