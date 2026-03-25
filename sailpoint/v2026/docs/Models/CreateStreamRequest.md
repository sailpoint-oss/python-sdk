---
id: v2026-create-stream-request
title: CreateStreamRequest
pagination_label: CreateStreamRequest
sidebar_label: CreateStreamRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateStreamRequest', 'V2026CreateStreamRequest'] 
slug: /tools/sdk/python/v2026/models/create-stream-request
tags: ['SDK', 'Software Development Kit', 'CreateStreamRequest', 'V2026CreateStreamRequest']
---

# CreateStreamRequest

Request body for POST /ssf/streams (create stream).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery** | [**CreateStreamDeliveryRequest**](create-stream-delivery-request) |  | [required]
**events_requested** | **[]str** | Optional list of event types the receiver wants. Use CAEP event-type URIs in the form: `https://schemas.openid.net/secevent/caep/event-type/{event-type}` (e.g. session revoke).  | [optional] 
**description** | **str** | Optional human-readable description of the stream. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.create_stream_request import CreateStreamRequest

create_stream_request = CreateStreamRequest(
delivery=sailpoint.v2026.models.create_stream_delivery_request.CreateStreamDeliveryRequest(
                    method = 'urn:ietf:rfc:8935', 
                    endpoint_url = 'https://receiver.example.com/ssf/events', 
                    authorization_header = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...', ),
events_requested=[https://schemas.openid.net/secevent/caep/event-type/session-revoked],
description='Production event stream'
)

```
[[Back to top]](#) 

