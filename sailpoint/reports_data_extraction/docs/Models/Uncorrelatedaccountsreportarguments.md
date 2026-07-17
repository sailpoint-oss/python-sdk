---
id: uncorrelatedaccountsreportarguments
title: Uncorrelatedaccountsreportarguments
pagination_label: Uncorrelatedaccountsreportarguments
sidebar_label: Uncorrelatedaccountsreportarguments
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Uncorrelatedaccountsreportarguments', 'Uncorrelatedaccountsreportarguments'] 
slug: /tools/sdk/python/reports-data-extraction/models/uncorrelatedaccountsreportarguments
tags: ['SDK', 'Software Development Kit', 'Uncorrelatedaccountsreportarguments', 'Uncorrelatedaccountsreportarguments']
---

# Uncorrelatedaccountsreportarguments

Arguments for Uncorrelated Accounts report (UNCORRELATED_ACCOUNTS)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_formats** | **[]str** | Output report file formats. These are formats for calling GET endpoint as query parameter 'fileFormat'.  In case report won't have this argument there will be ['CSV', 'PDF'] as default. | [optional] 
}

## Example

```python
from sailpoint.reports_data_extraction.models.uncorrelatedaccountsreportarguments import Uncorrelatedaccountsreportarguments

uncorrelatedaccountsreportarguments = Uncorrelatedaccountsreportarguments(
selected_formats=["CSV"]
)

```
[[Back to top]](#) 

