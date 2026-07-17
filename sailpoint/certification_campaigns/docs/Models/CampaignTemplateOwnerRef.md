---
id: campaign-template-owner-ref
title: CampaignTemplateOwnerRef
pagination_label: CampaignTemplateOwnerRef
sidebar_label: CampaignTemplateOwnerRef
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CampaignTemplateOwnerRef', 'CampaignTemplateOwnerRef'] 
slug: /tools/sdk/python/certification-campaigns/models/campaign-template-owner-ref
tags: ['SDK', 'Software Development Kit', 'CampaignTemplateOwnerRef', 'CampaignTemplateOwnerRef']
---

# CampaignTemplateOwnerRef

The owner of this template, and the owner of campaigns generated from this template via a schedule. This field is automatically populated at creation time with the current user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the owner | [optional] 
**type** |  **Enum** [  'IDENTITY' ] | Type of the owner | [optional] 
**name** | **str** | Name of the owner | [optional] 
**email** | **str** | Email of the owner | [optional] 
}

## Example

```python
from sailpoint.certification_campaigns.models.campaign_template_owner_ref import CampaignTemplateOwnerRef

campaign_template_owner_ref = CampaignTemplateOwnerRef(
id='2c918086676d3e0601677611dbde220f',
type='IDENTITY',
name='Mister Manager',
email='mr.manager@example.com'
)

```
[[Back to top]](#) 

