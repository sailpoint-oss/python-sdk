# Schedule2Months


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The application id | [optional] 
**account_match_config** | [**SelectorAccountMatchConfig**](SelectorAccountMatchConfig.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.schedule2_months import Schedule2Months

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule2Months from a JSON string
schedule2_months_instance = Schedule2Months.from_json(json)
# print the JSON string representation of the object
print(Schedule2Months.to_json())

# convert the object into a dict
schedule2_months_dict = schedule2_months_instance.to_dict()
# create an instance of Schedule2Months from a dict
schedule2_months_from_dict = Schedule2Months.from_dict(schedule2_months_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


