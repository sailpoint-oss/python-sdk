---
id: v2025-get-stream200-response
title: GetStream200Response
pagination_label: GetStream200Response
sidebar_label: GetStream200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetStream200Response', 'V2025GetStream200Response'] 
slug: /tools/sdk/python/v2025/models/get-stream200-response
tags: ['SDK', 'Software Development Kit', 'GetStream200Response', 'V2025GetStream200Response']
---

# GetStream200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream_id** | **str** | Unique stream identifier. | [optional] 
**iss** | **str** | Issuer (transmitter) URL. | [optional] 
**aud** | **str** | Audience for the stream. | [optional] 
**delivery** | [**DeliveryResponse**](delivery-response) |  | [optional] 
**events_supported** | **[]str** | Event types supported by the transmitter. Use CAEP event-type URIs in the form: `https://schemas.openid.net/secevent/caep/event-type/{event-type}` (e.g. session-revoked).  | [optional] 
**events_requested** | **[]str** | Event types requested by the receiver. Use CAEP event-type URIs in the form: `https://schemas.openid.net/secevent/caep/event-type/{event-type}` (e.g. session revoke).  | [optional] 
**events_delivered** | **[]str** | Event types currently being delivered (intersection of supported and requested). | [optional] 
**description** | **str** | Optional stream description. | [optional] 
**inactivity_timeout** | **int** | Inactivity timeout in seconds (optional). | [optional] 
**min_verification_interval** | **int** | Minimum verification interval in seconds (optional). | [optional] 
}

## Example

```python
from sailpoint.v2025.models.get_stream200_response import GetStream200Response

get_stream200_response = GetStream200Response(
stream_id='550e8400-e29b-41d4-a716-446655440000',
iss='https://tenant.sailpoint.com',
aud='https://receiver.example.com',
delivery=sailpoint.v2025.models.delivery_response.DeliveryResponse(
                    method = 'urn:ietf:rfc:8935', 
                    endpoint_url = 'https://receiver.example.com/ssf/events', ),
events_supported=[https://schemas.openid.net/secevent/caep/event-type/{event-type}],
events_requested=[https://schemas.openid.net/secevent/caep/event-type/{event-type}],
events_delivered=[https://schemas.openid.net/secevent/caep/event-type/{event-type}],
description='Production event stream',
inactivity_timeout=3600,
min_verification_interval=300
)

```
[[Back to top]](#) 

