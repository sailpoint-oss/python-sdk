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
**type** | [**DtoType**](dto-type) |  | [optional] 
**id** | **str** | Identity id | [optional] 
**name** | **str** | Human-readable display name of identity. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.account_action_request_dto_correlated_identity import AccountActionRequestDtoCorrelatedIdentity

account_action_request_dto_correlated_identity = AccountActionRequestDtoCorrelatedIdentity(
type='IDENTITY',
id='2c9180a46faadee4016fb4e018c20639',
name='Thomas Edison'
)

```
[[Back to top]](#) 

