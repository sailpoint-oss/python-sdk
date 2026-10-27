---
id: machine-account-classification-count
title: MachineAccountClassificationCount
pagination_label: MachineAccountClassificationCount
sidebar_label: MachineAccountClassificationCount
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineAccountClassificationCount', 'MachineAccountClassificationCount'] 
slug: /tools/sdk/python/machine-accounts/models/machine-account-classification-count
tags: ['SDK', 'Software Development Kit', 'MachineAccountClassificationCount', 'MachineAccountClassificationCount']
---

# MachineAccountClassificationCount

The number of machine account candidates found by one classification method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification_method** |  **Enum** [  'CRITERIA',    'SOURCE',    'DISCOVERY' ] | The classification method that found the candidates. | [optional] 
**count** | **int** | The number of candidates found by this classification method. | [optional] 
}

## Example

```python
from sailpoint.machine_accounts.models.machine_account_classification_count import MachineAccountClassificationCount

machine_account_classification_count = MachineAccountClassificationCount(
classification_method='CRITERIA',
count=42
)

```
[[Back to top]](#) 

