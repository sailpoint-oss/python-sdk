---
id: deliveryresponse
title: Deliveryresponse
pagination_label: Deliveryresponse
sidebar_label: Deliveryresponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Deliveryresponse', 'Deliveryresponse'] 
slug: /tools/sdk/python/v1/models/deliveryresponse
tags: ['SDK', 'Software Development Kit', 'Deliveryresponse', 'Deliveryresponse']
---

# Deliveryresponse

Delivery configuration returned in stream responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Delivery method. | [optional] 
**endpoint_url** | **str** | Receiver endpoint URL. | [optional] 
}

## Example

```python
from sailpoint.shared_signals_framework_ssf_v1.models.deliveryresponse import Deliveryresponse

deliveryresponse = Deliveryresponse(
method='urn:ietf:rfc:8935',
endpoint_url='https://receiver.example.com/ssf/events'
)

```
[[Back to top]](#) 

