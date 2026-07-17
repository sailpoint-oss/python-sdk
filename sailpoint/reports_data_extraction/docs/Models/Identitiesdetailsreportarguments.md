---
id: identitiesdetailsreportarguments
title: Identitiesdetailsreportarguments
pagination_label: Identitiesdetailsreportarguments
sidebar_label: Identitiesdetailsreportarguments
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Identitiesdetailsreportarguments', 'Identitiesdetailsreportarguments'] 
slug: /tools/sdk/python/reports-data-extraction/models/identitiesdetailsreportarguments
tags: ['SDK', 'Software Development Kit', 'Identitiesdetailsreportarguments', 'Identitiesdetailsreportarguments']
---

# Identitiesdetailsreportarguments

Arguments for Identities Details report (IDENTITIES_DETAILS)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlated_only** | **bool** | Flag to specify if only correlated identities are included in report. | [required][default to False]
}

## Example

```python
from sailpoint.reports_data_extraction.models.identitiesdetailsreportarguments import Identitiesdetailsreportarguments

identitiesdetailsreportarguments = Identitiesdetailsreportarguments(
correlated_only=True
)

```
[[Back to top]](#) 

