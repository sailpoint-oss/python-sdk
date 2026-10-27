---
id: mcp-connected-agent-source
title: MCPConnectedAgentSource
pagination_label: MCPConnectedAgentSource
sidebar_label: MCPConnectedAgentSource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MCPConnectedAgentSource', 'MCPConnectedAgentSource'] 
slug: /tools/sdk/python/business-applications/models/mcp-connected-agent-source
tags: ['SDK', 'Software Development Kit', 'MCPConnectedAgentSource', 'MCPConnectedAgentSource']
---

# MCPConnectedAgentSource

Source the AI agent was aggregated from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.business_applications.models.mcp_connected_agent_source import MCPConnectedAgentSource

mcp_connected_agent_source = MCPConnectedAgentSource(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

