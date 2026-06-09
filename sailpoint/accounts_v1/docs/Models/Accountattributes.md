---
id: accountattributes
title: Accountattributes
pagination_label: Accountattributes
sidebar_label: Accountattributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Accountattributes', 'Accountattributes'] 
slug: /tools/sdk/python/v1/models/accountattributes
tags: ['SDK', 'Software Development Kit', 'Accountattributes', 'Accountattributes']
---

# Accountattributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **map[string]object** | The schema attribute values for the account | [required]
}

## Example

```python
from sailpoint.accounts_v1.models.accountattributes import Accountattributes

accountattributes = Accountattributes(
attributes={"city":"Austin","displayName":"John Doe","userName":"jdoe","sAMAccountName":"jDoe","mail":"john.doe@sailpoint.com"}
)

```
[[Back to top]](#) 

