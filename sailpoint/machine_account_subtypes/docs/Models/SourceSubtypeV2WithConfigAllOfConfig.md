---
id: source-subtype-v2-with-config-all-of-config
title: SourceSubtypeV2WithConfigAllOfConfig
pagination_label: SourceSubtypeV2WithConfigAllOfConfig
sidebar_label: SourceSubtypeV2WithConfigAllOfConfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SourceSubtypeV2WithConfigAllOfConfig', 'SourceSubtypeV2WithConfigAllOfConfig'] 
slug: /tools/sdk/python/machine-account-subtypes/models/source-subtype-v2-with-config-all-of-config
tags: ['SDK', 'Software Development Kit', 'SourceSubtypeV2WithConfigAllOfConfig', 'SourceSubtypeV2WithConfigAllOfConfig']
---

# SourceSubtypeV2WithConfigAllOfConfig

Summary of the subtype's machine account creation configuration. `null` when the subtype is not a `MACHINE` subtype or has no machine account creation configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_account_create** | [**SourceSubtypeV2WithConfigAllOfConfigMachineAccountCreate**](source-subtype-v2-with-config-all-of-config-machine-account-create) |  | [optional] 
}

## Example

```python
from sailpoint.machine_account_subtypes.models.source_subtype_v2_with_config_all_of_config import SourceSubtypeV2WithConfigAllOfConfig

source_subtype_v2_with_config_all_of_config = SourceSubtypeV2WithConfigAllOfConfig(
machine_account_create=sailpoint.machine_account_subtypes.models.source_subtype_v2_with_config_all_of_config_machine_account_create.SourceSubtypeV2WithConfig_allOf_config_machineAccountCreate(
                    account_create_enabled = True, )
)

```
[[Back to top]](#) 

