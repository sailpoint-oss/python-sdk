---
id: v2025-load-uncorrelated-accounts-task-task-messages-inner
title: LoadUncorrelatedAccountsTaskTaskMessagesInner
pagination_label: LoadUncorrelatedAccountsTaskTaskMessagesInner
sidebar_label: LoadUncorrelatedAccountsTaskTaskMessagesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'LoadUncorrelatedAccountsTaskTaskMessagesInner', 'V2025LoadUncorrelatedAccountsTaskTaskMessagesInner'] 
slug: /tools/sdk/python/v2025/models/load-uncorrelated-accounts-task-task-messages-inner
tags: ['SDK', 'Software Development Kit', 'LoadUncorrelatedAccountsTaskTaskMessagesInner', 'V2025LoadUncorrelatedAccountsTaskTaskMessagesInner']
---

# LoadUncorrelatedAccountsTaskTaskMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'INFO',    'WARN',    'ERROR' ] | Type of the message. | [optional] 
**error** | **bool** | Flag whether message is an error. | [optional] [default to False]
**warning** | **bool** | Flag whether message is a warning. | [optional] [default to False]
**key** | **str** | Message string identifier. | [optional] 
**localized_text** | **str** | Message context with the locale based language. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.load_uncorrelated_accounts_task_task_messages_inner import LoadUncorrelatedAccountsTaskTaskMessagesInner

load_uncorrelated_accounts_task_task_messages_inner = LoadUncorrelatedAccountsTaskTaskMessagesInner(
type='WARN',
error=False,
warning=True,
key='This correlation failed because the currently running correlation must complete before the next one can start.',
localized_text='This correlation failed because the currently running correlation must complete before the next one can start.'
)

```
[[Back to top]](#) 

