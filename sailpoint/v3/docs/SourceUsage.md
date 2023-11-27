# SourceUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The first day of the month for which activity is aggregated. | [optional] 
**count** | **float** | The average number of days that accounts were active within this source, for the month. | [optional] 

## Example

```python
from sailpoint.v3.models.source_usage import SourceUsage

# TODO update the JSON string below
json = "{}"
# create an instance of SourceUsage from a JSON string
source_usage_instance = SourceUsage.from_json(json)
# print the JSON string representation of the object
print SourceUsage.to_json()

# convert the object into a dict
source_usage_dict = source_usage_instance.to_dict()
# create an instance of SourceUsage from a dict
source_usage_form_dict = source_usage.from_dict(source_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


