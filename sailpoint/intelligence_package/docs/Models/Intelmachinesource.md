---
id: intelmachinesource
title: Intelmachinesource
pagination_label: Intelmachinesource
sidebar_label: Intelmachinesource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelmachinesource', 'Intelmachinesource'] 
slug: /tools/sdk/python/intelligence-package/models/intelmachinesource
tags: ['SDK', 'Software Development Kit', 'Intelmachinesource', 'Intelmachinesource']
---

# Intelmachinesource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the correlated source in Identity Security Cloud. | [optional] 
**name** | **str** | Display name of the source as configured in Identity Security Cloud. | [optional] 
**type** | **str** | Connector or source type classification for the backing system. | [optional] 
}

## Example

```python
from sailpoint.intelligence_package.models.intelmachinesource import Intelmachinesource

intelmachinesource = Intelmachinesource(
id='2c9180835d2e5168015d32f890301e89',
name='Example Directory',
type='LDAP'
)

```
[[Back to top]](#) 

