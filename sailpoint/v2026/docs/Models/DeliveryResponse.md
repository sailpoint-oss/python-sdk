---
id: v2026-delivery-response
title: DeliveryResponse
pagination_label: DeliveryResponse
sidebar_label: DeliveryResponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DeliveryResponse', 'V2026DeliveryResponse'] 
slug: /tools/sdk/python/v2026/models/delivery-response
tags: ['SDK', 'Software Development Kit', 'DeliveryResponse', 'V2026DeliveryResponse']
---

# DeliveryResponse

Delivery configuration returned in stream responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Delivery method. | [optional] 
**endpoint_url** | **str** | Receiver endpoint URL. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.delivery_response import DeliveryResponse

delivery_response = DeliveryResponse(
method='urn:ietf:rfc:8935',
endpoint_url='https://receiver.example.com/ssf/events'
)

```
[[Back to top]](#) 

