---
id: v2025-replace-stream-configuration-request
title: ReplaceStreamConfigurationRequest
pagination_label: ReplaceStreamConfigurationRequest
sidebar_label: ReplaceStreamConfigurationRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ReplaceStreamConfigurationRequest', 'V2025ReplaceStreamConfigurationRequest'] 
slug: /tools/sdk/python/v2025/models/replace-stream-configuration-request
tags: ['SDK', 'Software Development Kit', 'ReplaceStreamConfigurationRequest', 'V2025ReplaceStreamConfigurationRequest']
---

# ReplaceStreamConfigurationRequest

Request body for PUT /ssf/streams (full replace).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream_id** | **str** | ID of the stream to replace. | [required]
**delivery** | [**ReplaceStreamConfigurationRequestDelivery**](replace-stream-configuration-request-delivery) |  | [required]
**events_requested** | **[]str** | Event types the receiver wants. Use CAEP event-type URIs. | [optional] 
**description** | **str** | Optional human-readable description of the stream. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.replace_stream_configuration_request import ReplaceStreamConfigurationRequest

replace_stream_configuration_request = ReplaceStreamConfigurationRequest(
stream_id='550e8400-e29b-41d4-a716-446655440000',
delivery=,
events_requested=[https://schemas.openid.net/secevent/caep/event-type/session-revoked],
description='Production event stream'
)

```
[[Back to top]](#) 

