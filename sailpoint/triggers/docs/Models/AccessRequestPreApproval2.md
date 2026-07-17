---
id: access-request-pre-approval2
title: AccessRequestPreApproval2
pagination_label: AccessRequestPreApproval2
sidebar_label: AccessRequestPreApproval2
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccessRequestPreApproval2', 'AccessRequestPreApproval2'] 
slug: /tools/sdk/python/triggers/models/access-request-pre-approval2
tags: ['SDK', 'Software Development Kit', 'AccessRequestPreApproval2', 'AccessRequestPreApproval2']
---

# AccessRequestPreApproval2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **bool** | Whether or not to approve the access request. | [required]
**comment** | **str** | A comment about the decision to approve or deny the request. | [required]
**approver** | **str** | The name of the entity that approved or denied the request. | [required]
}

## Example

```python
from sailpoint.triggers.models.access_request_pre_approval2 import AccessRequestPreApproval2

access_request_pre_approval2 = AccessRequestPreApproval2(
approved=False,
comment='This access should be denied, because this will cause an SOD violation.',
approver='AcmeCorpExternalIntegration'
)

```
[[Back to top]](#) 

