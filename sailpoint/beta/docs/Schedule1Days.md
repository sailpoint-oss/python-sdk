# Schedule1Days


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SelectorType**](SelectorType.md) |  | 
**values** | **List[str]** | The selected values.  | 
**interval** | **int** | The selected interval for RANGE selectors.  | [optional] 

## Example

```python
from beta.models.schedule1_days import Schedule1Days

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule1Days from a JSON string
schedule1_days_instance = Schedule1Days.from_json(json)
# print the JSON string representation of the object
print Schedule1Days.to_json()

# convert the object into a dict
schedule1_days_dict = schedule1_days_instance.to_dict()
# create an instance of Schedule1Days from a dict
schedule1_days_form_dict = schedule1_days.from_dict(schedule1_days_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


