---
id: account-delete-request-input
title: AccountDeleteRequestInput
pagination_label: AccountDeleteRequestInput
sidebar_label: AccountDeleteRequestInput
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountDeleteRequestInput', 'AccountDeleteRequestInput'] 
slug: /tools/sdk/python/account-deletion-requests/models/account-delete-request-input
tags: ['SDK', 'Software Development Kit', 'AccountDeleteRequestInput', 'AccountDeleteRequestInput']
---

# AccountDeleteRequestInput

Contains the required information for processing a user-initiated account deletion request, including the reason for deletion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Reason for deleting the account. | [optional] 
}

## Example

```python
from sailpoint.account_deletion_requests.models.account_delete_request_input import AccountDeleteRequestInput

account_delete_request_input = AccountDeleteRequestInput(
comments='Requesting account deletion request'
)

```
[[Back to top]](#) 

