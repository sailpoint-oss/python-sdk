---
id: correlation-rule-action
title: CorrelationRuleAction
pagination_label: CorrelationRuleAction
sidebar_label: CorrelationRuleAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CorrelationRuleAction', 'CorrelationRuleAction'] 
slug: /tools/sdk/python/machine-identities/models/correlation-rule-action
tags: ['SDK', 'Software Development Kit', 'CorrelationRuleAction', 'CorrelationRuleAction']
---

# CorrelationRuleAction

The action applied when a correlation rule matches.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'IDENTITY',    'ACCOUNT',    'GOVERNANCE_GROUP' ] | The target owner type resolved by this action. | [required]
**payload** | **map[string]object** | Action-specific payload. | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.correlation_rule_action import CorrelationRuleAction

correlation_rule_action = CorrelationRuleAction(
type='IDENTITY',
payload={"identityId":"2c9180858082150f0180893dbaf44201"}
)

```
[[Back to top]](#) 

