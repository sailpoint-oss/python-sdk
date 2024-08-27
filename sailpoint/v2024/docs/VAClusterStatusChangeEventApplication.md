# VAClusterStatusChangeEventApplication

Details about the `CLUSTER` or `SOURCE` that initiated this event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The GUID of the application | 
**name** | **str** | The name of the application | 
**attributes** | **Dict[str, object]** | Custom map of attributes for a source.  This will only be populated if type is &#x60;SOURCE&#x60; and the source has a proxy. | 

## Example

```python
from sailpoint.v2024.models.va_cluster_status_change_event_application import VAClusterStatusChangeEventApplication

# TODO update the JSON string below
json = "{}"
# create an instance of VAClusterStatusChangeEventApplication from a JSON string
va_cluster_status_change_event_application_instance = VAClusterStatusChangeEventApplication.from_json(json)
# print the JSON string representation of the object
print(VAClusterStatusChangeEventApplication.to_json())

# convert the object into a dict
va_cluster_status_change_event_application_dict = va_cluster_status_change_event_application_instance.to_dict()
# create an instance of VAClusterStatusChangeEventApplication from a dict
va_cluster_status_change_event_application_from_dict = VAClusterStatusChangeEventApplication.from_dict(va_cluster_status_change_event_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


