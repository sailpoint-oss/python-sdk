---
id: v2026-put-connector-correlation-config-request
title: PutConnectorCorrelationConfigRequest
pagination_label: PutConnectorCorrelationConfigRequest
sidebar_label: PutConnectorCorrelationConfigRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PutConnectorCorrelationConfigRequest', 'V2026PutConnectorCorrelationConfigRequest'] 
slug: /tools/sdk/python/v2026/models/put-connector-correlation-config-request
tags: ['SDK', 'Software Development Kit', 'PutConnectorCorrelationConfigRequest', 'V2026PutConnectorCorrelationConfigRequest']
---

# PutConnectorCorrelationConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | connector correlation config xml file | [required]
}

## Example

```python
from sailpoint.v2026.models.put_connector_correlation_config_request import PutConnectorCorrelationConfigRequest

put_connector_correlation_config_request = PutConnectorCorrelationConfigRequest(
file=bytes(b'blah')
)

```
[[Back to top]](#) 

