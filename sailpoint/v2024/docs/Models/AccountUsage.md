---
id: v2024-account-usage
title: AccountUsage
pagination_label: AccountUsage
sidebar_label: AccountUsage
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountUsage', 'V2024AccountUsage'] 
slug: /tools/sdk/python/v2024/models/account-usage
tags: ['SDK', 'Software Development Kit', 'AccountUsage', 'V2024AccountUsage']
---

# AccountUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The first day of the month for which activity is aggregated. | [optional] 
**count** | **int** | The number of days within the month that the account was active in a source. | [optional] 
}

## Example

```python
from sailpoint.v2024.models.account_usage import AccountUsage

account_usage = AccountUsage(
var_date='Fri Apr 21 00:00:00 UTC 2023',
count=10
)

```
[[Back to top]](#) 

