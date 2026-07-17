---
id: identitiesreportarguments
title: Identitiesreportarguments
pagination_label: Identitiesreportarguments
sidebar_label: Identitiesreportarguments
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Identitiesreportarguments', 'Identitiesreportarguments'] 
slug: /tools/sdk/python/reports-data-extraction/models/identitiesreportarguments
tags: ['SDK', 'Software Development Kit', 'Identitiesreportarguments', 'Identitiesreportarguments']
---

# Identitiesreportarguments

Arguments for Identities report (IDENTITIES)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlated_only** | **bool** | Flag to specify if only correlated identities are included in report. | [optional] [default to False]
}

## Example

```python
from sailpoint.reports_data_extraction.models.identitiesreportarguments import Identitiesreportarguments

identitiesreportarguments = Identitiesreportarguments(
correlated_only=True
)

```
[[Back to top]](#) 

