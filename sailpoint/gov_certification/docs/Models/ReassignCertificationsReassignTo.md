---
id: reassign-certifications-reassign-to
title: ReassignCertificationsReassignTo
pagination_label: ReassignCertificationsReassignTo
sidebar_label: ReassignCertificationsReassignTo
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ReassignCertificationsReassignTo', 'ReassignCertificationsReassignTo'] 
slug: /tools/sdk/python/gov-certification/models/reassign-certifications-reassign-to
tags: ['SDK', 'Software Development Kit', 'ReassignCertificationsReassignTo', 'ReassignCertificationsReassignTo']
---

# ReassignCertificationsReassignTo

Reviewer to which the certification is reassigned

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identity ID to which the review is being assigned. | [optional] 
**type** |  **Enum** [  'IDENTITY' ] | The type of the ID provided | [optional] 
}

## Example

```python
from sailpoint.gov_certification.models.reassign_certifications_reassign_to import ReassignCertificationsReassignTo

reassign_certifications_reassign_to = ReassignCertificationsReassignTo(
id='0fbe863c-063c-4c88-a35f-d7f17e8a3df5',
type='IDENTITY'
)

```
[[Back to top]](#) 

