---
id: accessprofilemetadatabulkupdatebyidrequest
title: Accessprofilemetadatabulkupdatebyidrequest
pagination_label: Accessprofilemetadatabulkupdatebyidrequest
sidebar_label: Accessprofilemetadatabulkupdatebyidrequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Accessprofilemetadatabulkupdatebyidrequest', 'Accessprofilemetadatabulkupdatebyidrequest'] 
slug: /tools/sdk/python/access-profiles/models/accessprofilemetadatabulkupdatebyidrequest
tags: ['SDK', 'Software Development Kit', 'Accessprofilemetadatabulkupdatebyidrequest', 'Accessprofilemetadatabulkupdatebyidrequest']
---

# Accessprofilemetadatabulkupdatebyidrequest

Request to bulk update Access Model Metadata on a list of access profiles identified by ID. The maximum access profile count in a single request is 3000. A single access profile cannot be assigned more than 25 metadata values. Adding or replacing custom metadata requires a suite license.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_profiles** | **[]str** | The IDs of the access profiles to update. | [required]
**operation** |  **Enum** [  'ADD',    'REMOVE',    'REPLACE' ] | The operation to be performed | [required]
**replace_scope** |  **Enum** [  'ALL',    'ATTRIBUTE' ] | The choice of update scope. **ATTRIBUTE** replaces only the values of the attributes named in `values`, and **ALL** replaces every metadata attribute on the access profile. | [required]
**values** | [**[]AccessprofilemetadatabulkupdatebyidrequestValuesInner**](accessprofilemetadatabulkupdatebyidrequest-values-inner) | The metadata to be updated, including attribute key and value. | [required]
}

## Example

```python
from sailpoint.access_profiles.models.accessprofilemetadatabulkupdatebyidrequest import Accessprofilemetadatabulkupdatebyidrequest

accessprofilemetadatabulkupdatebyidrequest = Accessprofilemetadatabulkupdatebyidrequest(
access_profiles=["b1db89554cfa431cb8b9921ea38d9367"],
operation='REPLACE',
replace_scope='ATTRIBUTE',
values=[{"attribute":"iscFederalClassifications","values":["topSecret"]}]
)

```
[[Back to top]](#) 

