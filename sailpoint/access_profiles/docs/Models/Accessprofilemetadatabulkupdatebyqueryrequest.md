---
id: accessprofilemetadatabulkupdatebyqueryrequest
title: Accessprofilemetadatabulkupdatebyqueryrequest
pagination_label: Accessprofilemetadatabulkupdatebyqueryrequest
sidebar_label: Accessprofilemetadatabulkupdatebyqueryrequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Accessprofilemetadatabulkupdatebyqueryrequest', 'Accessprofilemetadatabulkupdatebyqueryrequest'] 
slug: /tools/sdk/python/access-profiles/models/accessprofilemetadatabulkupdatebyqueryrequest
tags: ['SDK', 'Software Development Kit', 'Accessprofilemetadatabulkupdatebyqueryrequest', 'Accessprofilemetadatabulkupdatebyqueryrequest']
---

# Accessprofilemetadatabulkupdatebyqueryrequest

Request to bulk update Access Model Metadata on every access profile matching a search query. A single access profile cannot be assigned more than 25 metadata values. Adding or replacing custom metadata requires a suite license.  For more information about the query object, refer to [V3 API Perform Search](https://developer.sailpoint.com/docs/api/v3/search-post).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | The search query selecting the access profiles to update. | [required]
**operation** |  **Enum** [  'ADD',    'REMOVE',    'REPLACE' ] | The operation to be performed | [required]
**replace_scope** |  **Enum** [  'ALL',    'ATTRIBUTE' ] | The choice of update scope. **ATTRIBUTE** replaces only the values of the attributes named in `values`, and **ALL** replaces every metadata attribute on the access profile. | [required]
**values** | [**[]AccessprofilemetadatabulkupdatebyidrequestValuesInner**](accessprofilemetadatabulkupdatebyidrequest-values-inner) | The metadata to be updated, including attribute key and value. | [required]
}

## Example

```python
from sailpoint.access_profiles.models.accessprofilemetadatabulkupdatebyqueryrequest import Accessprofilemetadatabulkupdatebyqueryrequest

accessprofilemetadatabulkupdatebyqueryrequest = Accessprofilemetadatabulkupdatebyqueryrequest(
query={"indices":["accessprofiles"],"queryType":"TEXT","textQuery":{"terms":["test123"],"fields":["id"],"matchAny":false,"contains":true},"includeNested":false},
operation='REPLACE',
replace_scope='ATTRIBUTE',
values=[{"attribute":"iscFederalClassifications","values":["topSecret"]}]
)

```
[[Back to top]](#) 

