---
id: accountaggregationcompleted-source
title: AccountaggregationcompletedSource
pagination_label: AccountaggregationcompletedSource
sidebar_label: AccountaggregationcompletedSource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountaggregationcompletedSource', 'AccountaggregationcompletedSource'] 
slug: /tools/sdk/python/v1/models/accountaggregationcompleted-source
tags: ['SDK', 'Software Development Kit', 'AccountaggregationcompletedSource', 'AccountaggregationcompletedSource']
---

# AccountaggregationcompletedSource

The source the accounts are being aggregated from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'SOURCE' ] | The DTO type of the source the accounts are being aggregated from. | [required]
**id** | **str** | The ID of the source the accounts are being aggregated from. | [required]
**name** | **str** | Display name of the source the accounts are being aggregated from. | [required]
}

## Example

```python
from sailpoint.triggers_v1.models.accountaggregationcompleted_source import AccountaggregationcompletedSource

accountaggregationcompleted_source = AccountaggregationcompletedSource(
type='SOURCE',
id='2c9180835d191a86015d28455b4b232a',
name='HR Active Directory'
)

```
[[Back to top]](#) 

