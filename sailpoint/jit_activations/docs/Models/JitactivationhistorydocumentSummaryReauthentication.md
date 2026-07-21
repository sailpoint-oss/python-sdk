---
id: jitactivationhistorydocument-summary-reauthentication
title: JitactivationhistorydocumentSummaryReauthentication
pagination_label: JitactivationhistorydocumentSummaryReauthentication
sidebar_label: JitactivationhistorydocumentSummaryReauthentication
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JitactivationhistorydocumentSummaryReauthentication', 'JitactivationhistorydocumentSummaryReauthentication'] 
slug: /tools/sdk/python/jit-activations/models/jitactivationhistorydocument-summary-reauthentication
tags: ['SDK', 'Software Development Kit', 'JitactivationhistorydocumentSummaryReauthentication', 'JitactivationhistorydocumentSummaryReauthentication']
---

# JitactivationhistorydocumentSummaryReauthentication

Reauthentication friction details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **bool** | Whether reauthentication was required for this activation. | [optional] [default to False]
**bypassed** | **bool** | Whether the reauthentication requirement was bypassed. | [optional] [default to False]
}

## Example

```python
from sailpoint.jit_activations.models.jitactivationhistorydocument_summary_reauthentication import JitactivationhistorydocumentSummaryReauthentication

jitactivationhistorydocument_summary_reauthentication = JitactivationhistorydocumentSummaryReauthentication(
required=True,
bypassed=False
)

```
[[Back to top]](#) 

