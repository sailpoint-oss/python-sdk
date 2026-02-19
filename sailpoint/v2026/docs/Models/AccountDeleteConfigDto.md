---
id: v2026-account-delete-config-dto
title: AccountDeleteConfigDto
pagination_label: AccountDeleteConfigDto
sidebar_label: AccountDeleteConfigDto
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountDeleteConfigDto', 'V2026AccountDeleteConfigDto'] 
slug: /tools/sdk/python/v2026/models/account-delete-config-dto
tags: ['SDK', 'Software Development Kit', 'AccountDeleteConfigDto', 'V2026AccountDeleteConfigDto']
---

# AccountDeleteConfigDto

detailed information about account delete approval config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_required** | **bool** | Specifies if an account deletion request requires approval. | [optional] [default to False]
**approval_config** | [**ApprovalConfig**](approval-config) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.account_delete_config_dto import AccountDeleteConfigDto

account_delete_config_dto = AccountDeleteConfigDto(
approval_required=True,
approval_config=sailpoint.v2026.models.approval_config.ApprovalConfig(
                    approvers = 'sourceOwner, accountOwner, manager, workgroup:f76ff96a-0815-402a-be1a-18cdc693b79f', 
                    comments = 'REJECTION', )
)

```
[[Back to top]](#) 

