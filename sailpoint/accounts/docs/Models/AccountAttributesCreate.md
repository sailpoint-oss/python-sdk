---
id: account-attributes-create
title: AccountAttributesCreate
pagination_label: AccountAttributesCreate
sidebar_label: AccountAttributesCreate
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountAttributesCreate', 'AccountAttributesCreate'] 
slug: /tools/sdk/python/accounts/models/account-attributes-create
tags: ['SDK', 'Software Development Kit', 'AccountAttributesCreate', 'AccountAttributesCreate']
---

# AccountAttributesCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **AccountAttributesCreateAttributes** |  | [required]
}

## Example

```python
from sailpoint.accounts.models.account_attributes_create import AccountAttributesCreate

account_attributes_create = AccountAttributesCreate(
attributes={"sourceId":"34bfcbe116c9407464af37acbaf7a4dc","city":"Austin","displayName":"John Doe","userName":"jdoe","sAMAccountName":"jDoe","mail":"john.doe@sailpoint.com"}
)

```
[[Back to top]](#) 

