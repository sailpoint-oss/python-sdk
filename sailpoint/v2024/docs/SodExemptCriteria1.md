# SodExemptCriteria1

Details of the Entitlement criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing** | **bool** | If the entitlement already belonged to the user or not. | [optional] [default to False]
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | Entitlement ID | [optional] 
**name** | **str** | Entitlement name | [optional] 

## Example

```python
from sailpoint.v2024.models.sod_exempt_criteria1 import SodExemptCriteria1

# TODO update the JSON string below
json = "{}"
# create an instance of SodExemptCriteria1 from a JSON string
sod_exempt_criteria1_instance = SodExemptCriteria1.from_json(json)
# print the JSON string representation of the object
print(SodExemptCriteria1.to_json())

# convert the object into a dict
sod_exempt_criteria1_dict = sod_exempt_criteria1_instance.to_dict()
# create an instance of SodExemptCriteria1 from a dict
sod_exempt_criteria1_from_dict = SodExemptCriteria1.from_dict(sod_exempt_criteria1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


