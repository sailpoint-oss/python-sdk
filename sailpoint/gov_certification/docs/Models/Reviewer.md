---
id: reviewer
title: Reviewer
pagination_label: Reviewer
sidebar_label: Reviewer
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Reviewer', 'Reviewer'] 
slug: /tools/sdk/python/gov-certification/models/reviewer
tags: ['SDK', 'Software Development Kit', 'Reviewer', 'Reviewer']
---

# Reviewer

The specified target will be the reviewer for all certifications in this campaign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Identity or Governance Group | [optional] 
**type** | **CampaignReviewerType** |  | [required]
**name** | **str** | Human-readable display name of the Identity or Governance Group | [optional] 
}

## Example

```python
from sailpoint.gov_certification.models.reviewer import Reviewer

reviewer = Reviewer(
id='0fbe863c063c4c88a35fd7f17e8a3df5',
type='IDENTITY',
name='William Wilson'
)

```
[[Back to top]](#) 

