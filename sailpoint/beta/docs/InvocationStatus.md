# InvocationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Invocation ID | 
**trigger_id** | **str** | Trigger ID | 
**subscription_name** | **str** | Subscription name | 
**subscription_id** | **str** | Subscription ID | 
**type** | [**InvocationStatusType**](InvocationStatusType.md) |  | 
**created** | **datetime** | Invocation created timestamp. ISO-8601 in UTC. | 
**completed** | **datetime** | Invocation completed timestamp; empty fields imply invocation is in-flight or not completed. ISO-8601 in UTC. | [optional] 
**start_invocation_input** | [**StartInvocationInput**](StartInvocationInput.md) |  | 
**complete_invocation_input** | [**CompleteInvocationInput**](CompleteInvocationInput.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.invocation_status import InvocationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of InvocationStatus from a JSON string
invocation_status_instance = InvocationStatus.from_json(json)
# print the JSON string representation of the object
print(InvocationStatus.to_json())

# convert the object into a dict
invocation_status_dict = invocation_status_instance.to_dict()
# create an instance of InvocationStatus from a dict
invocation_status_from_dict = InvocationStatus.from_dict(invocation_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


