---
id: v2026-update-stream-configuration-request
title: UpdateStreamConfigurationRequest
pagination_label: UpdateStreamConfigurationRequest
sidebar_label: UpdateStreamConfigurationRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UpdateStreamConfigurationRequest', 'V2026UpdateStreamConfigurationRequest'] 
slug: /tools/sdk/python/v2026/models/update-stream-configuration-request
tags: ['SDK', 'Software Development Kit', 'UpdateStreamConfigurationRequest', 'V2026UpdateStreamConfigurationRequest']
---

# UpdateStreamConfigurationRequest

Request body for PATCH /ssf/streams (partial update).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream_id** | **str** | ID of the stream to update. | [required]
**delivery** | [**DeliveryRequest**](delivery-request) |  | [optional] 
**events_requested** | **[]str** | Event types the receiver wants. Use CAEP event-type URIs. | [optional] 
**description** | **str** | Optional human-readable description of the stream. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.update_stream_configuration_request import UpdateStreamConfigurationRequest

update_stream_configuration_request = UpdateStreamConfigurationRequest(
stream_id='550e8400-e29b-41d4-a716-446655440000',
delivery=sailpoint.v2026.models.delivery_request.DeliveryRequest(
                    method = 'urn:ietf:rfc:8935', 
                    endpoint_url = 'https://receiver.example.com/ssf/events', 
                    authorization_header = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...', ),
events_requested=[https://schemas.openid.net/secevent/caep/event-type/session-revoked],
description='Updated production event stream configuration'
)

```
[[Back to top]](#) 

