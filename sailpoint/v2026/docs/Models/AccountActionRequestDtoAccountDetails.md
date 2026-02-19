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
**account_id** | **str** | ID of account | [optional] 
**account_name** | **str** | Account name | [optional] 
**account_native_identity** | **str** | Native identity of account | [optional] 
**account_uuid** | **str** | UUID associated with account | [optional] 
**account_type** | **str** | Type of account | [optional] 
**account_subtype_id** | **str** | Sub Type ID of account | [optional] 
**account_subtype** | **str** | Subtype of account | [optional] 
**description** | **str** | Account Description | [optional] 
**source_id** | **str** | ID of source | [optional] 
**source_name** | **str** | Name of source | [optional] 
**has_entitlements** | **bool** | Indicates entitlements assigned to identity or not | [optional] [default to False]
**disabled** | **bool** | Indicates account is enabled/disabled | [optional] [default to False]
**locked** | **bool** | Indicates account locked/unlocked | [optional] [default to False]
**owner_identity** | [**AccountDetailsOwnerIdentity**](account-details-owner-identity) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.account_action_request_dto_account_details import AccountActionRequestDtoAccountDetails

account_action_request_dto_account_details = AccountActionRequestDtoAccountDetails(
account_id='15e169acf21f4ae28e8a06198ce7f699',
account_name='walter.white',
account_native_identity='CN=Walter White,OU=BB,OU=org-data-service,DC=TestAutomationAD,DC=local',
account_uuid='{3bbeb846-e168-47d2-9e5d-bd46506c9280=null}',
account_type='HUMAN',
account_subtype_id='',
account_subtype='',
description='This is human account for identity walter.white',
source_id='ee03924d95034cd088cbd5af068f1772',
source_name='BB AD',
has_entitlements=True,
disabled=False,
locked=False,
owner_identity=
)

```
[[Back to top]](#) 

