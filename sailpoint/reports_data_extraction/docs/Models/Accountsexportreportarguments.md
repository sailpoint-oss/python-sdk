---
id: accountsexportreportarguments
title: Accountsexportreportarguments
pagination_label: Accountsexportreportarguments
sidebar_label: Accountsexportreportarguments
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Accountsexportreportarguments', 'Accountsexportreportarguments'] 
slug: /tools/sdk/python/reports-data-extraction/models/accountsexportreportarguments
tags: ['SDK', 'Software Development Kit', 'Accountsexportreportarguments', 'Accountsexportreportarguments']
---

# Accountsexportreportarguments

Arguments for Account Export report (ACCOUNTS)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | Source ID. | [required]
**source_name** | **str** | Source name. | [required]
}

## Example

```python
from sailpoint.reports_data_extraction.models.accountsexportreportarguments import Accountsexportreportarguments

accountsexportreportarguments = Accountsexportreportarguments(
application='2c9180897eSourceIde781782f705b9',
source_name='Active Directory'
)

```
[[Back to top]](#) 

