---
id: intelidentityaccesshistorybody
title: Intelidentityaccesshistorybody
pagination_label: Intelidentityaccesshistorybody
sidebar_label: Intelidentityaccesshistorybody
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelidentityaccesshistorybody', 'Intelidentityaccesshistorybody'] 
slug: /tools/sdk/python/v1/models/intelidentityaccesshistorybody
tags: ['SDK', 'Software Development Kit', 'Intelidentityaccesshistorybody', 'Intelidentityaccesshistorybody']
---

# Intelidentityaccesshistorybody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **[]Dict[str, object]** | Each event is relayed from identity-history. Schema varies by event type; consumers should treat unknown fields as opaque using additionalProperties.  | [required]
}

## Example

```python
from sailpoint.intelligence_package_v1.models.intelidentityaccesshistorybody import Intelidentityaccesshistorybody

intelidentityaccesshistorybody = Intelidentityaccesshistorybody(
events=[{"id":"evt-001","type":"LOGIN","dateTime":"2024-05-01T12:00:00Z"}]
)

```
[[Back to top]](#) 

