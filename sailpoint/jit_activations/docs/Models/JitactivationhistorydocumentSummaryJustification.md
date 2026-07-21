---
id: jitactivationhistorydocument-summary-justification
title: JitactivationhistorydocumentSummaryJustification
pagination_label: JitactivationhistorydocumentSummaryJustification
sidebar_label: JitactivationhistorydocumentSummaryJustification
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JitactivationhistorydocumentSummaryJustification', 'JitactivationhistorydocumentSummaryJustification'] 
slug: /tools/sdk/python/jit-activations/models/jitactivationhistorydocument-summary-justification
tags: ['SDK', 'Software Development Kit', 'JitactivationhistorydocumentSummaryJustification', 'JitactivationhistorydocumentSummaryJustification']
---

# JitactivationhistorydocumentSummaryJustification

Justification friction details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **bool** | Whether a justification was required for this activation. | [optional] [default to False]
**bypassed** | **bool** | Whether the justification requirement was bypassed. | [optional] [default to False]
}

## Example

```python
from sailpoint.jit_activations.models.jitactivationhistorydocument_summary_justification import JitactivationhistorydocumentSummaryJustification

jitactivationhistorydocument_summary_justification = JitactivationhistorydocumentSummaryJustification(
required=True,
bypassed=False
)

```
[[Back to top]](#) 

