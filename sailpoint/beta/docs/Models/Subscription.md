---
id: beta-subscription
title: Subscription
pagination_label: Subscription
sidebar_label: Subscription
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Subscription', 'BetaSubscription'] 
slug: /tools/sdk/python/beta/models/subscription
tags: ['SDK', 'Software Development Kit', 'Subscription', 'BetaSubscription']
---

# Subscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subscription ID. | [required]
**name** | **str** | Subscription name. | [required]
**description** | **str** | Subscription description. | [optional] 
**trigger_id** | **str** | ID of trigger subscribed to. | [required]
**trigger_name** | **str** | Trigger name of trigger subscribed to. | [required]
**type** | [**SubscriptionType**](subscription-type) |  | [required]
**response_deadline** | **str** | Deadline for completing REQUEST_RESPONSE trigger invocation, represented in ISO-8601 duration format. | [optional] [default to 'PT1H']
**http_config** | [**HttpConfig**](http-config) |  | [optional] 
**event_bridge_config** | [**EventBridgeConfig**](event-bridge-config) |  | [optional] 
**enabled** | **bool** | Whether subscription should receive real-time trigger invocations or not. Test trigger invocations are always enabled regardless of this option. | [required][default to True]
**filter** | **str** | JSONPath filter to conditionally invoke trigger when expression evaluates to true. | [optional] 
}

## Example

```python
from sailpoint.beta.models.subscription import Subscription

subscription = Subscription(
id='0f11f2a4-7c94-4bf3-a2bd-742580fe3bde',
name='Access request subscription',
description='Access requested to site xyz',
trigger_id='idn:access-request-post-approval',
trigger_name='Access Requested',
type='HTTP',
response_deadline='PT1H',
http_config=sailpoint.beta.models.http_config.HttpConfig(
                    url = 'https://www.example.com', 
                    http_dispatch_mode = 'SYNC', 
                    http_authentication_type = 'NO_AUTH', 
                    basic_auth_config = sailpoint.beta.models.basic_auth_config.BasicAuthConfig(
                        user_name = 'user@example.com', 
                        password = '', ), 
                    bearer_token_auth_config = sailpoint.beta.models.bearer_token_auth_config.BearerTokenAuthConfig(
                        bearer_token = '', ), ),
event_bridge_config=sailpoint.beta.models.event_bridge_config.EventBridgeConfig(
                    aws_account = '123456789012', 
                    aws_region = 'us-west-1', ),
enabled=True,
filter='$[?($.identityId == "201327fda1c44704ac01181e963d463c")]'
)

```
[[Back to top]](#) 

