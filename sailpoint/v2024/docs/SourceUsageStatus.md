# SourceUsageStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Source Usage Status. Acceptable values are:   - COMPLETE       - This status means that an activity data source has been setup and usage insights are available for the source.   - INCOMPLETE       - This status means that an activity data source has not been setup and usage insights are not available for the source. | [optional] 

## Example

```python
from sailpoint.v2024.models.source_usage_status import SourceUsageStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SourceUsageStatus from a JSON string
source_usage_status_instance = SourceUsageStatus.from_json(json)
# print the JSON string representation of the object
print(SourceUsageStatus.to_json())

# convert the object into a dict
source_usage_status_dict = source_usage_status_instance.to_dict()
# create an instance of SourceUsageStatus from a dict
source_usage_status_from_dict = SourceUsageStatus.from_dict(source_usage_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


