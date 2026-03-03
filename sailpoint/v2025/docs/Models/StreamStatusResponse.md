---
id: v2025-stream-status-response
title: StreamStatusResponse
pagination_label: StreamStatusResponse
sidebar_label: StreamStatusResponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'StreamStatusResponse', 'V2025StreamStatusResponse'] 
slug: /tools/sdk/python/v2025/models/stream-status-response
tags: ['SDK', 'Software Development Kit', 'StreamStatusResponse', 'V2025StreamStatusResponse']
---

# StreamStatusResponse

Stream status returned by GET/POST /ssf/streams/status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream_id** | **str** | Stream identifier. | [optional] 
**status** |  **Enum** [  'enabled',    'paused',    'disabled' ] | Operational status of the stream (enabled, paused, or disabled). | [optional] 
**reason** | **str** | Optional reason for the current status (e.g. set when status is updated). | [optional] 
}

## Example

```python
from sailpoint.v2025.models.stream_status_response import StreamStatusResponse

stream_status_response = StreamStatusResponse(
stream_id='550e8400-e29b-41d4-a716-446655440000',
status='enabled',
reason=''
)

```
[[Back to top]](#) 

