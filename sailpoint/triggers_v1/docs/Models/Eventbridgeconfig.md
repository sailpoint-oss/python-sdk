---
id: eventbridgeconfig
title: Eventbridgeconfig
pagination_label: Eventbridgeconfig
sidebar_label: Eventbridgeconfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Eventbridgeconfig', 'Eventbridgeconfig'] 
slug: /tools/sdk/python/v1/models/eventbridgeconfig
tags: ['SDK', 'Software Development Kit', 'Eventbridgeconfig', 'Eventbridgeconfig']
---

# Eventbridgeconfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_account** | **str** | AWS Account Number (12-digit number) that has the EventBridge Partner Event Source Resource. | [required]
**aws_region** | **str** | AWS Region that has the EventBridge Partner Event Source Resource. See https://docs.aws.amazon.com/general/latest/gr/rande.html for a full list of available values. | [required]
}

## Example

```python
from sailpoint.triggers_v1.models.eventbridgeconfig import Eventbridgeconfig

eventbridgeconfig = Eventbridgeconfig(
aws_account='123456789012',
aws_region='us-west-1'
)

```
[[Back to top]](#) 

