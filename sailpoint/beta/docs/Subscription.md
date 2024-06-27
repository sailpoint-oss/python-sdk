# Subscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subscription ID. | 
**name** | **str** | Subscription name. | 
**description** | **str** | Subscription description. | [optional] 
**trigger_id** | **str** | ID of trigger subscribed to. | 
**trigger_name** | **str** | Trigger name of trigger subscribed to. | 
**type** | [**SubscriptionType**](SubscriptionType.md) |  | 
**response_deadline** | **str** | Deadline for completing REQUEST_RESPONSE trigger invocation, represented in ISO-8601 duration format. | [optional] [default to 'PT1H']
**http_config** | [**HttpConfig**](HttpConfig.md) |  | [optional] 
**event_bridge_config** | [**EventBridgeConfig**](EventBridgeConfig.md) |  | [optional] 
**enabled** | **bool** | Whether subscription should receive real-time trigger invocations or not. Test trigger invocations are always enabled regardless of this option. | [default to True]
**filter** | **str** | JSONPath filter to conditionally invoke trigger when expression evaluates to true. | [optional] 

## Example

```python
from sailpoint.beta.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print Subscription.to_json()

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_form_dict = subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


