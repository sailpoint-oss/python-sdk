# VAClusterStatusChangeEventPreviousHealthCheckResult

The results of the last health check.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Detailed message of the result of the health check. | 
**result_type** | **str** | The type of the health check result. | 
**status** | **object** | The status of the health check. | 

## Example

```python
from sailpoint.beta.models.va_cluster_status_change_event_previous_health_check_result import VAClusterStatusChangeEventPreviousHealthCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of VAClusterStatusChangeEventPreviousHealthCheckResult from a JSON string
va_cluster_status_change_event_previous_health_check_result_instance = VAClusterStatusChangeEventPreviousHealthCheckResult.from_json(json)
# print the JSON string representation of the object
print(VAClusterStatusChangeEventPreviousHealthCheckResult.to_json())

# convert the object into a dict
va_cluster_status_change_event_previous_health_check_result_dict = va_cluster_status_change_event_previous_health_check_result_instance.to_dict()
# create an instance of VAClusterStatusChangeEventPreviousHealthCheckResult from a dict
va_cluster_status_change_event_previous_health_check_result_from_dict = VAClusterStatusChangeEventPreviousHealthCheckResult.from_dict(va_cluster_status_change_event_previous_health_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


