---
id: campaign-reference-reviewer
title: CampaignReferenceReviewer
pagination_label: CampaignReferenceReviewer
sidebar_label: CampaignReferenceReviewer
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CampaignReferenceReviewer', 'CampaignReferenceReviewer'] 
slug: /tools/sdk/python/gov-certification/models/campaign-reference-reviewer
tags: ['SDK', 'Software Development Kit', 'CampaignReferenceReviewer', 'CampaignReferenceReviewer']
---

# CampaignReferenceReviewer

The specified target will be the reviewer for all certifications in this campaign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **CampaignReviewerType** |  | [optional] 
}

## Example

```python
from sailpoint.gov_certification.models.campaign_reference_reviewer import CampaignReferenceReviewer

campaign_reference_reviewer = CampaignReferenceReviewer(
type='IDENTITY'
)

```
[[Back to top]](#) 

