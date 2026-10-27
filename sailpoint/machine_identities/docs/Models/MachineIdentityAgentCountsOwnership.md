---
id: machine-identity-agent-counts-ownership
title: MachineIdentityAgentCountsOwnership
pagination_label: MachineIdentityAgentCountsOwnership
sidebar_label: MachineIdentityAgentCountsOwnership
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityAgentCountsOwnership', 'MachineIdentityAgentCountsOwnership'] 
slug: /tools/sdk/python/machine-identities/models/machine-identity-agent-counts-ownership
tags: ['SDK', 'Software Development Kit', 'MachineIdentityAgentCountsOwnership', 'MachineIdentityAgentCountsOwnership']
---

# MachineIdentityAgentCountsOwnership

Ownership coverage of AI agents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owned_agents** | **int** | Number of AI agents that have at least one owner. | [optional] 
**owned_percent** | **int** | Percentage of AI agents that have at least one owner. | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.machine_identity_agent_counts_ownership import MachineIdentityAgentCountsOwnership

machine_identity_agent_counts_ownership = MachineIdentityAgentCountsOwnership(
owned_agents=70,
owned_percent=82
)

```
[[Back to top]](#) 

