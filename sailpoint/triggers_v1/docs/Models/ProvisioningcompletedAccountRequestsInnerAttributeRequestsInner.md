---
id: provisioningcompleted-account-requests-inner-attribute-requests-inner
title: ProvisioningcompletedAccountRequestsInnerAttributeRequestsInner
pagination_label: ProvisioningcompletedAccountRequestsInnerAttributeRequestsInner
sidebar_label: ProvisioningcompletedAccountRequestsInnerAttributeRequestsInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProvisioningcompletedAccountRequestsInnerAttributeRequestsInner', 'ProvisioningcompletedAccountRequestsInnerAttributeRequestsInner'] 
slug: /tools/sdk/python/v1/models/provisioningcompleted-account-requests-inner-attribute-requests-inner
tags: ['SDK', 'Software Development Kit', 'ProvisioningcompletedAccountRequestsInnerAttributeRequestsInner', 'ProvisioningcompletedAccountRequestsInnerAttributeRequestsInner']
---

# ProvisioningcompletedAccountRequestsInnerAttributeRequestsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The name of the attribute being provisioned. | [required]
**attribute_value** | **str** | The value of the attribute being provisioned. | [optional] 
**operation** |  **Enum** [  'Add',    'Set',    'Remove' ] | The operation to handle the attribute. | [required]
}

## Example

```python
from sailpoint.triggers_v1.models.provisioningcompleted_account_requests_inner_attribute_requests_inner import ProvisioningcompletedAccountRequestsInnerAttributeRequestsInner

provisioningcompleted_account_requests_inner_attribute_requests_inner = ProvisioningcompletedAccountRequestsInnerAttributeRequestsInner(
attribute_name='memberOf',
attribute_value='CN=jedi,DC=starwars,DC=com',
operation='Add'
)

```
[[Back to top]](#) 

