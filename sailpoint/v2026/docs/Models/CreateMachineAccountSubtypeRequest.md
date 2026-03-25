---
id: v2026-create-machine-account-subtype-request
title: CreateMachineAccountSubtypeRequest
pagination_label: CreateMachineAccountSubtypeRequest
sidebar_label: CreateMachineAccountSubtypeRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateMachineAccountSubtypeRequest', 'V2026CreateMachineAccountSubtypeRequest'] 
slug: /tools/sdk/python/v2026/models/create-machine-account-subtype-request
tags: ['SDK', 'Software Development Kit', 'CreateMachineAccountSubtypeRequest', 'V2026CreateMachineAccountSubtypeRequest']
---

# CreateMachineAccountSubtypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technical_name** | **str** | Technical name of the subtype. | [required]
**display_name** | **str** | Display name of the subtype. | [required]
**description** | **str** | Description of the subtype. | [required]
**type** | **str** | Type of the subtype. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.create_machine_account_subtype_request import CreateMachineAccountSubtypeRequest

create_machine_account_subtype_request = CreateMachineAccountSubtypeRequest(
technical_name='foo',
display_name='Mr Foo',
description='fighters',
type='MACHINE'
)

```
[[Back to top]](#) 

