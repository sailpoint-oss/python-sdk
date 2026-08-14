---
id: responseactioncontext
title: Responseactioncontext
pagination_label: Responseactioncontext
sidebar_label: Responseactioncontext
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Responseactioncontext', 'Responseactioncontext'] 
slug: /tools/sdk/python/intelligence/models/responseactioncontext
tags: ['SDK', 'Software Development Kit', 'Responseactioncontext', 'Responseactioncontext']
---

# Responseactioncontext

External source metadata captured for audit and traceability.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** |  **Enum** [  'CROWDSTRIKE',    'SENTINEL',    'SPLUNK',    'CUSTOM' ] | External system that initiated the action. | [required]
**external_alert_id** | **str** | External alert or case identifier. | [optional] 
**reason** | **str** | Human-readable reason for the action. | [optional] 
**operator** | **str** | Operator or analyst who initiated the action. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.responseactioncontext import Responseactioncontext

responseactioncontext = Responseactioncontext(
source='CROWDSTRIKE',
external_alert_id='CS-FALCON-12345',
reason='Contain compromised account',
operator='soc-analyst@customer.com'
)

```
[[Back to top]](#) 

