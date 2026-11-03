---
id: account-v2-identity
title: AccountV2Identity
pagination_label: AccountV2Identity
sidebar_label: AccountV2Identity
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountV2Identity', 'AccountV2Identity'] 
slug: /tools/sdk/python/accounts/models/account-v2-identity
tags: ['SDK', 'Software Development Kit', 'AccountV2Identity', 'AccountV2Identity']
---

# AccountV2Identity

An identity reference associated with this account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the identity. | [optional] 
**type** |  **Enum** [  'IDENTITY' ] | The DTO type of the identity. | [optional] 
**name** | **str** | The display name of the identity. | [optional] 
**state** | **str** | The identity state. | [optional] 
}

## Example

```python
from sailpoint.accounts.models.account_v2_identity import AccountV2Identity

account_v2_identity = AccountV2Identity(
id='2c918084660f45d6016617daa9210584',
type='IDENTITY',
name='John Doe',
state='ACTIVE'
)

```
[[Back to top]](#) 

