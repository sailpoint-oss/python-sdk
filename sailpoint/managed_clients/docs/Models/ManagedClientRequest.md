---
id: managed-client-request
title: ManagedClientRequest
pagination_label: ManagedClientRequest
sidebar_label: ManagedClientRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ManagedClientRequest', 'ManagedClientRequest'] 
slug: /tools/sdk/python/managed-clients/models/managed-client-request
tags: ['SDK', 'Software Development Kit', 'ManagedClientRequest', 'ManagedClientRequest']
---

# ManagedClientRequest

Managed Client Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Cluster ID that the ManagedClient is linked to | [required]
**description** | **str** | description for the ManagedClient to create | [optional] 
**name** | **str** | name for the ManagedClient to create | [optional] 
**type** | **str** | Type of the ManagedClient (VA, CCG) to create | [optional] 
}

## Example

```python
from sailpoint.managed_clients.models.managed_client_request import ManagedClientRequest

managed_client_request = ManagedClientRequest(
cluster_id='aClusterId',
description='A short description of the ManagedClient',
name='aName',
type='VA'
)

```
[[Back to top]](#) 

