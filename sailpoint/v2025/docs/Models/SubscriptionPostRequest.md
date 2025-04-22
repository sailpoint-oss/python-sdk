---
id: v2025-subscription-post-request
title: SubscriptionPostRequest
pagination_label: SubscriptionPostRequest
sidebar_label: SubscriptionPostRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubscriptionPostRequest', 'V2025SubscriptionPostRequest'] 
slug: /tools/sdk/python/v2025/models/subscription-post-request
tags: ['SDK', 'Software Development Kit', 'SubscriptionPostRequest', 'V2025SubscriptionPostRequest']
---

# SubscriptionPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Subscription name. | [required]
**description** | **str** | Subscription description. | [optional] 
**trigger_id** | **str** | ID of trigger subscribed to. | [required]
**type** | [**SubscriptionType**](subscription-type) |  | [required]
**response_deadline** | **str** | Deadline for completing REQUEST_RESPONSE trigger invocation, represented in ISO-8601 duration format. | [optional] [default to 'PT1H']
**http_config** | [**HttpConfig**](http-config) |  | [optional] 
**event_bridge_config** | [**EventBridgeConfig**](event-bridge-config) |  | [optional] 
**enabled** | **bool** | Whether subscription should receive real-time trigger invocations or not.  Test trigger invocations are always enabled regardless of this option. | [optional] [default to True]
**filter** | **str** | JSONPath filter to conditionally invoke trigger when expression evaluates to true. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.subscription_post_request import SubscriptionPostRequest

subscription_post_request = SubscriptionPostRequest(
name='Access request subscription',
description='Access requested to site xyz',
trigger_id='idn:access-requested',
type='HTTP',
response_deadline='PT1H',
http_config=sailpoint.v2025.models.http_config.HttpConfig(
                    url = 'https://www.example.com', 
                    http_dispatch_mode = 'SYNC', 
                    http_authentication_type = 'NO_AUTH', 
                    basic_auth_config = sailpoint.v2025.models.basic_auth_config.BasicAuthConfig(
                        user_name = 'user@example.com', 
                        password = '', ), 
                    bearer_token_auth_config = sailpoint.v2025.models.bearer_token_auth_config.BearerTokenAuthConfig(
                        bearer_token = '', ), ),
event_bridge_config=sailpoint.v2025.models.event_bridge_config.EventBridgeConfig(
                    aws_account = '123456789012', 
                    aws_region = 'us-west-1', ),
enabled=True,
filter='$[?($.identityId == "201327fda1c44704ac01181e963d463c")]'
)

```
[[Back to top]](#) 

