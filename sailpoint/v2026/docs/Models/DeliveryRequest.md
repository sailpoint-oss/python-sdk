---
id: v2026-delivery-request
title: DeliveryRequest
pagination_label: DeliveryRequest
sidebar_label: DeliveryRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DeliveryRequest', 'V2026DeliveryRequest'] 
slug: /tools/sdk/python/v2026/models/delivery-request
tags: ['SDK', 'Software Development Kit', 'DeliveryRequest', 'V2026DeliveryRequest']
---

# DeliveryRequest

Delivery configuration for PATCH /ssf/streams (partial update). All fields are optional; only provided fields are updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Delivery method (optional for PATCH). | [optional] 
**endpoint_url** | **str** | Receiver endpoint URL (optional for PATCH). | [optional] 
**authorization_header** | **str** | Optional authorization header value. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.delivery_request import DeliveryRequest

delivery_request = DeliveryRequest(
method='urn:ietf:rfc:8935',
endpoint_url='https://receiver.example.com/ssf/events',
authorization_header='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'
)

```
[[Back to top]](#) 

