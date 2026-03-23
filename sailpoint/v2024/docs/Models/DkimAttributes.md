---
id: v2024-dkim-attributes
title: DkimAttributes
pagination_label: DkimAttributes
sidebar_label: DkimAttributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DkimAttributes', 'V2024DkimAttributes'] 
slug: /tools/sdk/python/v2024/models/dkim-attributes
tags: ['SDK', 'Software Development Kit', 'DkimAttributes', 'V2024DkimAttributes']
---

# DkimAttributes

DKIM attributes for a domain or identity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID associated with domain to be verified | [optional] 
**address** | **str** | The identity or domain address | [optional] 
**dkim_enabled** | **bool** | Whether or not DKIM has been enabled for this domain / identity | [optional] [default to False]
**dkim_tokens** | **[]str** | The tokens to be added to a DNS for verification | [optional] 
**dkim_verification_status** | **str** | The current status if the domain /identity has been verified. Ie SUCCESS, FAILED, PENDING | [optional] 
**region** | **str** | The AWS SES region the domain is associated with | [optional] 
}

## Example

```python
from sailpoint.v2024.models.dkim_attributes import DkimAttributes

dkim_attributes = DkimAttributes(
id='123b45b0-aaaa-bbbb-a7db-123456a56abc',
address='BobSmith@sailpoint.com',
dkim_enabled=True,
dkim_tokens=[uq1m3jjk25ckd3whl4n7y46c56r5l6aq, u7pm38jky9ckdawhlsn7y4dcj6f5lpgq, uhpm3jjkjjckdkwhlqn7yw6cjer5tpay],
dkim_verification_status='SUCCESS',
region='us-east-1'
)

```
[[Back to top]](#) 

