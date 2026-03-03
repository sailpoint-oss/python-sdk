---
id: v2025-update-stream-status-request
title: UpdateStreamStatusRequest
pagination_label: UpdateStreamStatusRequest
sidebar_label: UpdateStreamStatusRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UpdateStreamStatusRequest', 'V2025UpdateStreamStatusRequest'] 
slug: /tools/sdk/python/v2025/models/update-stream-status-request
tags: ['SDK', 'Software Development Kit', 'UpdateStreamStatusRequest', 'V2025UpdateStreamStatusRequest']
---

# UpdateStreamStatusRequest

Request body for POST /ssf/streams/status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream_id** | **str** | ID of the stream whose status to update. | [required]
**status** |  **Enum** [  'enabled',    'paused',    'disabled' ] | Desired stream status. | [required]
**reason** | **str** | Optional reason for the status change. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.update_stream_status_request import UpdateStreamStatusRequest

update_stream_status_request = UpdateStreamStatusRequest(
stream_id='550e8400-e29b-41d4-a716-446655440000',
status='paused',
reason='manually paused'
)

```
[[Back to top]](#) 

