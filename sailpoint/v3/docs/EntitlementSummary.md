# EntitlementSummary

EntitlementReference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**display_name** | **str** |  | [optional] 
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**description** | **str** |  | [optional] 
**source** | [**Reference**](Reference.md) |  | [optional] 
**privileged** | **bool** |  | [optional] 
**attribute** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**standalone** | **bool** |  | [optional] 

## Example

```python
from sailpoint.v3.models.entitlement_summary import EntitlementSummary

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementSummary from a JSON string
entitlement_summary_instance = EntitlementSummary.from_json(json)
# print the JSON string representation of the object
print EntitlementSummary.to_json()

# convert the object into a dict
entitlement_summary_dict = entitlement_summary_instance.to_dict()
# create an instance of EntitlementSummary from a dict
entitlement_summary_form_dict = entitlement_summary.from_dict(entitlement_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


