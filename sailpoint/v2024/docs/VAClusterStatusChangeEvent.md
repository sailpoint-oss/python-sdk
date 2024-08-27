# VAClusterStatusChangeEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The date and time the status change occurred. | 
**type** | **object** | The type of the object that initiated this event. | 
**application** | [**VAClusterStatusChangeEventApplication**](VAClusterStatusChangeEventApplication.md) |  | 
**health_check_result** | [**VAClusterStatusChangeEventHealthCheckResult**](VAClusterStatusChangeEventHealthCheckResult.md) |  | 
**previous_health_check_result** | [**VAClusterStatusChangeEventPreviousHealthCheckResult**](VAClusterStatusChangeEventPreviousHealthCheckResult.md) |  | 

## Example

```python
from sailpoint.v2024.models.va_cluster_status_change_event import VAClusterStatusChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VAClusterStatusChangeEvent from a JSON string
va_cluster_status_change_event_instance = VAClusterStatusChangeEvent.from_json(json)
# print the JSON string representation of the object
print(VAClusterStatusChangeEvent.to_json())

# convert the object into a dict
va_cluster_status_change_event_dict = va_cluster_status_change_event_instance.to_dict()
# create an instance of VAClusterStatusChangeEvent from a dict
va_cluster_status_change_event_from_dict = VAClusterStatusChangeEvent.from_dict(va_cluster_status_change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


