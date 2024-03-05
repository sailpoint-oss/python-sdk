# EntitlementManuallyUpdatedFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **bool** | True if the entitlements name was updated manually via entitlement import csv or patch endpoint.  False means that property value has not been change after first entitlement aggregation. Field refers to [Entitlement response schema](https://developer.sailpoint.com/idn/api/beta/get-entitlement) &gt; &#x60;name&#x60; property. | [optional] [default to False]
**description** | **bool** | True if the entitlement description was updated manually via entitlement import csv or patch endpoint.  False means that property value has not been change after first entitlement aggregation. Field refers to [Entitlement response schema](https://developer.sailpoint.com/idn/api/beta/get-entitlement) &gt; &#x60;description&#x60; property. | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.entitlement_manually_updated_fields import EntitlementManuallyUpdatedFields

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementManuallyUpdatedFields from a JSON string
entitlement_manually_updated_fields_instance = EntitlementManuallyUpdatedFields.from_json(json)
# print the JSON string representation of the object
print EntitlementManuallyUpdatedFields.to_json()

# convert the object into a dict
entitlement_manually_updated_fields_dict = entitlement_manually_updated_fields_instance.to_dict()
# create an instance of EntitlementManuallyUpdatedFields from a dict
entitlement_manually_updated_fields_form_dict = entitlement_manually_updated_fields.from_dict(entitlement_manually_updated_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


