# SubscriptionPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Subscription name. | [optional] 
**description** | **str** | Subscription description. | [optional] 
**type** | [**SubscriptionType**](SubscriptionType.md) |  | [optional] 
**response_deadline** | **str** | Deadline for completing REQUEST_RESPONSE trigger invocation, represented in ISO-8601 duration format. | [optional] [default to 'PT1H']
**http_config** | [**HttpConfig**](HttpConfig.md) |  | [optional] 
**event_bridge_config** | [**EventBridgeConfig**](EventBridgeConfig.md) |  | [optional] 
**enabled** | **bool** | Whether subscription should receive real-time trigger invocations or not.  Test trigger invocations are always enabled regardless of this option. | [optional] [default to True]
**filter** | **str** | JSONPath filter to conditionally invoke trigger when expression evaluates to true. | [optional] 

## Example

```python
from sailpoint.v2024.models.subscription_put_request import SubscriptionPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPutRequest from a JSON string
subscription_put_request_instance = SubscriptionPutRequest.from_json(json)
# print the JSON string representation of the object
print SubscriptionPutRequest.to_json()

# convert the object into a dict
subscription_put_request_dict = subscription_put_request_instance.to_dict()
# create an instance of SubscriptionPutRequest from a dict
subscription_put_request_form_dict = subscription_put_request.from_dict(subscription_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


