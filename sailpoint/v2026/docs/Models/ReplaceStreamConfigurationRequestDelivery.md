---
id: v2026-replace-stream-configuration-request-delivery
title: ReplaceStreamConfigurationRequestDelivery
pagination_label: ReplaceStreamConfigurationRequestDelivery
sidebar_label: ReplaceStreamConfigurationRequestDelivery
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ReplaceStreamConfigurationRequestDelivery', 'V2026ReplaceStreamConfigurationRequestDelivery'] 
slug: /tools/sdk/python/v2026/models/replace-stream-configuration-request-delivery
tags: ['SDK', 'Software Development Kit', 'ReplaceStreamConfigurationRequestDelivery', 'V2026ReplaceStreamConfigurationRequestDelivery']
---

# ReplaceStreamConfigurationRequestDelivery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Delivery method (only push is supported). | [required]
**endpoint_url** | **str** | Receiver endpoint URL for push delivery. | [required]
**authorization_header** | **str** | Authorization header value for delivery requests. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.replace_stream_configuration_request_delivery import ReplaceStreamConfigurationRequestDelivery

replace_stream_configuration_request_delivery = ReplaceStreamConfigurationRequestDelivery(
method='urn:ietf:rfc:8935',
endpoint_url='https://receiver.example.com/ssf/events',
authorization_header='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'
)

```
[[Back to top]](#) 

