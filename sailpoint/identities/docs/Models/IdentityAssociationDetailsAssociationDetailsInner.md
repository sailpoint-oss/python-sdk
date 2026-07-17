---
id: identity-association-details-association-details-inner
title: IdentityAssociationDetailsAssociationDetailsInner
pagination_label: IdentityAssociationDetailsAssociationDetailsInner
sidebar_label: IdentityAssociationDetailsAssociationDetailsInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IdentityAssociationDetailsAssociationDetailsInner', 'IdentityAssociationDetailsAssociationDetailsInner'] 
slug: /tools/sdk/python/identities/models/identity-association-details-association-details-inner
tags: ['SDK', 'Software Development Kit', 'IdentityAssociationDetailsAssociationDetailsInner', 'IdentityAssociationDetailsAssociationDetailsInner']
---

# IdentityAssociationDetailsAssociationDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_type** | **str** | association type with the identity | [optional] 
**entities** | [**[]IdentityEntities**](identity-entities) | the specific resource this identity has ownership on | [optional] 
}

## Example

```python
from sailpoint.identities.models.identity_association_details_association_details_inner import IdentityAssociationDetailsAssociationDetailsInner

identity_association_details_association_details_inner = IdentityAssociationDetailsAssociationDetailsInner(
association_type='CAMPAIGN_OWNER',
entities={"id":"b660a232f05b4e04812ca974b3011e0f","name":"Gaston.800ddf9640a","type":"CAMPAIGN_CAMPAIGNER"}
)

```
[[Back to top]](#) 

