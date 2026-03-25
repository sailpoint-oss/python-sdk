---
id: v2026-account-action-request-dto-requester
title: AccountActionRequestDtoRequester
pagination_label: AccountActionRequestDtoRequester
sidebar_label: AccountActionRequestDtoRequester
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountActionRequestDtoRequester', 'V2026AccountActionRequestDtoRequester'] 
slug: /tools/sdk/python/v2026/models/account-action-request-dto-requester
tags: ['SDK', 'Software Development Kit', 'AccountActionRequestDtoRequester', 'V2026AccountActionRequestDtoRequester']
---

# AccountActionRequestDtoRequester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](dto-type) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.v2026.models.account_action_request_dto_requester import AccountActionRequestDtoRequester

account_action_request_dto_requester = AccountActionRequestDtoRequester(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

