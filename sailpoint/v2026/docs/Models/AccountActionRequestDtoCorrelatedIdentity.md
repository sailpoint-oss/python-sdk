---
id: v2026-account-action-request-dto-correlated-identity
title: AccountActionRequestDtoCorrelatedIdentity
pagination_label: AccountActionRequestDtoCorrelatedIdentity
sidebar_label: AccountActionRequestDtoCorrelatedIdentity
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountActionRequestDtoCorrelatedIdentity', 'V2026AccountActionRequestDtoCorrelatedIdentity'] 
slug: /tools/sdk/python/v2026/models/account-action-request-dto-correlated-identity
tags: ['SDK', 'Software Development Kit', 'AccountActionRequestDtoCorrelatedIdentity', 'V2026AccountActionRequestDtoCorrelatedIdentity']
---

# AccountActionRequestDtoCorrelatedIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of identity | [optional] 
**name** | **str** | Name of Identity | [optional] 
**email** | **str** | mail id of identity | [optional] 
**status** | **str** | status of identity UNREGISTERED/REGISTERED | [optional] 
}

## Example

```python
from sailpoint.v2026.models.account_action_request_dto_correlated_identity import AccountActionRequestDtoCorrelatedIdentity

account_action_request_dto_correlated_identity = AccountActionRequestDtoCorrelatedIdentity(
id='117e169acf21f4ae28e8a06198ce7f69',
name='Alfred',
email='alfred@testmail.identitysoon.com',
status='UNREGISTERED'
)

```
[[Back to top]](#) 

