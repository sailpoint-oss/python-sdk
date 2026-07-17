---
id: identity-ownership-association-details-association-details-inner
title: IdentityOwnershipAssociationDetailsAssociationDetailsInner
pagination_label: IdentityOwnershipAssociationDetailsAssociationDetailsInner
sidebar_label: IdentityOwnershipAssociationDetailsAssociationDetailsInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IdentityOwnershipAssociationDetailsAssociationDetailsInner', 'IdentityOwnershipAssociationDetailsAssociationDetailsInner'] 
slug: /tools/sdk/python/identities/models/identity-ownership-association-details-association-details-inner
tags: ['SDK', 'Software Development Kit', 'IdentityOwnershipAssociationDetailsAssociationDetailsInner', 'IdentityOwnershipAssociationDetailsAssociationDetailsInner']
---

# IdentityOwnershipAssociationDetailsAssociationDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_type** | **str** | association type with the identity | [optional] 
**entities** | [**[]IdentityEntities**](identity-entities) | the specific resource this identity has ownership on | [optional] 
}

## Example

```python
from sailpoint.identities.models.identity_ownership_association_details_association_details_inner import IdentityOwnershipAssociationDetailsAssociationDetailsInner

identity_ownership_association_details_association_details_inner = IdentityOwnershipAssociationDetailsAssociationDetailsInner(
association_type='ROLE_OWNER',
entities={"id":"b660a232f05b4e04812ca974b3011e0f","name":"Gaston.800ddf9640a","type":"ROLE"}
)

```
[[Back to top]](#) 

