---
id: campaign-filter-get
title: CampaignFilterGet
pagination_label: CampaignFilterGet
sidebar_label: CampaignFilterGet
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CampaignFilterGet', 'CampaignFilterGet'] 
slug: /tools/sdk/python/gov-certification/models/campaign-filter-get
tags: ['SDK', 'Software Development Kit', 'CampaignFilterGet', 'CampaignFilterGet']
---

# CampaignFilterGet

Campaign Filter Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the campaign filter | [optional] 
**name** | **str** | This is campaign filter's name. | [required]
**description** | **str** | This is campaign filter's description. | [required]
**owner** | **str** | The owner of this filter. This field is automatically populated at creation time with the current user. | [required]
**created** | **datetime** | Creation date of Campaign Filter | [optional] [readonly] 
**modified** | **datetime** | Modification date of Campaign Filter | [optional] [readonly] 
**mode** | **CampaignFilterType** |  | [required]
**criteria_list** | [**[]Criteria**](criteria) | List of criteria. | [optional] 
}

## Example

```python
from sailpoint.gov_certification.models.campaign_filter_get import CampaignFilterGet

campaign_filter_get = CampaignFilterGet(
id='e9f9a139-7b84-2fd5-a658-42087040d3ac',
name='Identity Attribute Campaign Filter',
description='Campaign filter to certify data based on specified property of Identity Attribute.',
owner='SailPoint Support',
created='2020-03-05T22:44:00.364Z',
modified='2020-03-05T22:52:09.969Z',
mode='INCLUSION',
criteria_list=[{"criteriaType":"IDENTITY","criteriaProperty":"DISPLAY_NAME","criteriaValue":"support","operation":"EQUALS"}]
)

```
[[Back to top]](#) 

