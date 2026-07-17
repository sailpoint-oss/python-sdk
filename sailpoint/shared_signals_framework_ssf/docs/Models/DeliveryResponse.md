---
id: delivery-response
title: DeliveryResponse
pagination_label: DeliveryResponse
sidebar_label: DeliveryResponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DeliveryResponse', 'DeliveryResponse'] 
slug: /tools/sdk/python/shared-signals-framework-ssf/models/delivery-response
tags: ['SDK', 'Software Development Kit', 'DeliveryResponse', 'DeliveryResponse']
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
from sailpoint.shared_signals_framework_ssf.models.delivery_response import DeliveryResponse

delivery_response = DeliveryResponse(
method='urn:ietf:rfc:8935',
endpoint_url='https://receiver.example.com/ssf/events'
)

```
[[Back to top]](#) 

