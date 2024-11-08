# QueuedCheckConfigDetails

Configuration of maximum number of days and interval for checking Service Desk integration queue status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provisioning_status_check_interval_minutes** | **str** | Interval in minutes between status checks | 
**provisioning_max_status_check_days** | **str** | Maximum number of days to check | 

## Example

```python
from sailpoint.v2024.models.queued_check_config_details import QueuedCheckConfigDetails

# TODO update the JSON string below
json = "{}"
# create an instance of QueuedCheckConfigDetails from a JSON string
queued_check_config_details_instance = QueuedCheckConfigDetails.from_json(json)
# print the JSON string representation of the object
print(QueuedCheckConfigDetails.to_json())

# convert the object into a dict
queued_check_config_details_dict = queued_check_config_details_instance.to_dict()
# create an instance of QueuedCheckConfigDetails from a dict
queued_check_config_details_from_dict = QueuedCheckConfigDetails.from_dict(queued_check_config_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


