---
id: soap-api-action
title: SoapApiAction
pagination_label: SoapApiAction
sidebar_label: SoapApiAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SoapApiAction', 'SoapApiAction'] 
slug: /tools/sdk/python//models/soap-api-action
tags: ['SDK', 'Software Development Kit', 'SoapApiAction', 'SoapApiAction']
---

# SoapApiAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.soap_api_action import SoapApiAction

soap_api_action = SoapApiAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Makes a request to a SOAP API.',
archived=False
)

```
[[Back to top]](#) 

