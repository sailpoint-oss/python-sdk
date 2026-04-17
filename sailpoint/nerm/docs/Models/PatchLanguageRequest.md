---
id: patch-language-request
title: PatchLanguageRequest
pagination_label: PatchLanguageRequest
sidebar_label: PatchLanguageRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PatchLanguageRequest', 'PatchLanguageRequest'] 
slug: /tools/sdk/python//models/patch-language-request
tags: ['SDK', 'Software Development Kit', 'PatchLanguageRequest', 'PatchLanguageRequest']
---

# PatchLanguageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**Language**](language) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.patch_language_request import PatchLanguageRequest

patch_language_request = PatchLanguageRequest(
language=sailpoint.nerm.models.language.Language(
                    default = True, 
                    enabled = True, 
                    locale = 'es', )
)

```
[[Back to top]](#) 

