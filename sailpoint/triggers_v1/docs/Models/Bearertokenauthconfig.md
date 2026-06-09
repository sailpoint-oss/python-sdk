---
id: bearertokenauthconfig
title: Bearertokenauthconfig
pagination_label: Bearertokenauthconfig
sidebar_label: Bearertokenauthconfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Bearertokenauthconfig', 'Bearertokenauthconfig'] 
slug: /tools/sdk/python/v1/models/bearertokenauthconfig
tags: ['SDK', 'Software Development Kit', 'Bearertokenauthconfig', 'Bearertokenauthconfig']
---

# Bearertokenauthconfig

Config required if BEARER_TOKEN authentication is used. On response, this field is set to null as to not return secrets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bearer_token** | **str** | Bearer token | [optional] 
}

## Example

```python
from sailpoint.triggers_v1.models.bearertokenauthconfig import Bearertokenauthconfig

bearertokenauthconfig = Bearertokenauthconfig(
bearer_token=''
)

```
[[Back to top]](#) 

