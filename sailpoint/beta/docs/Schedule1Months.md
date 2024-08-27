# Schedule1Months


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SelectorType**](SelectorType.md) |  | 
**values** | **List[str]** | The selected values.  | 
**interval** | **int** | The selected interval for RANGE selectors.  | [optional] 

## Example

```python
from sailpoint.beta.models.schedule1_months import Schedule1Months

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule1Months from a JSON string
schedule1_months_instance = Schedule1Months.from_json(json)
# print the JSON string representation of the object
print(Schedule1Months.to_json())

# convert the object into a dict
schedule1_months_dict = schedule1_months_instance.to_dict()
# create an instance of Schedule1Months from a dict
schedule1_months_from_dict = Schedule1Months.from_dict(schedule1_months_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


