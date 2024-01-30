# SodExemptCriteria

Details of the Entitlement criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing** | **bool** | If the entitlement already belonged to the user or not. | [optional] 
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | Entitlement ID | [optional] 
**name** | **str** | Entitlement name | [optional] 

## Example

```python
from sailpoint.beta.models.sod_exempt_criteria import SodExemptCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of SodExemptCriteria from a JSON string
sod_exempt_criteria_instance = SodExemptCriteria.from_json(json)
# print the JSON string representation of the object
print SodExemptCriteria.to_json()

# convert the object into a dict
sod_exempt_criteria_dict = sod_exempt_criteria_instance.to_dict()
# create an instance of SodExemptCriteria from a dict
sod_exempt_criteria_form_dict = sod_exempt_criteria.from_dict(sod_exempt_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


