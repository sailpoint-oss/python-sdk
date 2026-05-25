---
id: v2026-error-body
title: ErrorBody
pagination_label: ErrorBody
sidebar_label: ErrorBody
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ErrorBody', 'V2026ErrorBody'] 
slug: /tools/sdk/python/v2026/models/error-body
tags: ['SDK', 'Software Development Kit', 'ErrorBody', 'V2026ErrorBody']
---

# ErrorBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_code** | **str** | Machine-readable error code returned by the Intelligence Package service. | [optional] 
**message** | **str** | Human-readable explanation of the error suitable for client logging. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.error_body import ErrorBody

error_body = ErrorBody(
detail_code='IDC_BAD_REQUEST',
message='The filters query parameter is required and cannot be empty.'
)

```
[[Back to top]](#) 

