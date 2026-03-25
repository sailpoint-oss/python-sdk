---
id: v2026-account-action-request-dto-account-details
title: AccountActionRequestDtoAccountDetails
pagination_label: AccountActionRequestDtoAccountDetails
sidebar_label: AccountActionRequestDtoAccountDetails
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountActionRequestDtoAccountDetails', 'V2026AccountActionRequestDtoAccountDetails'] 
slug: /tools/sdk/python/v2026/models/account-action-request-dto-account-details
tags: ['SDK', 'Software Development Kit', 'AccountActionRequestDtoAccountDetails', 'V2026AccountActionRequestDtoAccountDetails']
---

# AccountActionRequestDtoAccountDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | unique id of this object | [optional] 
**name** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**native_identity** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 
**uncorrelated** | **bool** |  | [optional] 
**system_account** | **bool** |  | [optional] 
**authoritative** | **bool** |  | [optional] 
**supports_password_change** | **bool** |  | [optional] 
**attributes** | **object** |  | [optional] 
**application** | **object** |  | [optional] 
**identity** | **object** |  | [optional] 
**var_schema** | **object** |  | [optional] 
**pending_access_request_ids** | **[]str** |  | [optional] 
**features** | **[]str** |  | [optional] 
**meta** | **object** |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.account_action_request_dto_account_details import AccountActionRequestDtoAccountDetails

account_action_request_dto_account_details = AccountActionRequestDtoAccountDetails(
id='2c91808474683da6017468693c260195',
name='',
account_id='4191808474683da6017468693c260195',
description='',
native_identity='',
uuid='',
display_name='',
disabled=True,
locked=True,
uncorrelated=True,
system_account=True,
authoritative=True,
supports_password_change=True,
attributes=sailpoint.v2026.models.attributes.attributes(),
application=sailpoint.v2026.models.application.application(),
identity=sailpoint.v2026.models.identity.identity(),
var_schema=sailpoint.v2026.models.schema.schema(),
pending_access_request_ids=[
                    ''
                    ],
features=[
                    'AUTHENTICATE'
                    ],
meta=sailpoint.v2026.models.meta.meta()
)

```
[[Back to top]](#) 

