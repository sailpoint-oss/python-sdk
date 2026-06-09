---
id: commonaccessitemrequest
title: Commonaccessitemrequest
pagination_label: Commonaccessitemrequest
sidebar_label: Commonaccessitemrequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Commonaccessitemrequest', 'Commonaccessitemrequest'] 
slug: /tools/sdk/python/v1/models/commonaccessitemrequest
tags: ['SDK', 'Software Development Kit', 'Commonaccessitemrequest', 'Commonaccessitemrequest']
---

# Commonaccessitemrequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**Commonaccessitemaccess**](commonaccessitemaccess) |  | [optional] 
**status** | [**Commonaccessitemstate**](commonaccessitemstate) |  | [optional] 
}

## Example

```python
from sailpoint.iai_common_access_v1.models.commonaccessitemrequest import Commonaccessitemrequest

commonaccessitemrequest = Commonaccessitemrequest(
access=sailpoint.iai_common_access_v1.models.common_access_item_access.Common Access Item Access(
                    id = '', 
                    type = 'ACCESS_PROFILE', 
                    name = '', 
                    description = '', 
                    owner_name = '', 
                    owner_id = '', ),
status='CONFIRMED'
)

```
[[Back to top]](#) 

