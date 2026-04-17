---
id: languages
title: Languages
pagination_label: languages
sidebar_label: languages
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'languages', 'languages'] 
slug: /tools/sdk/python//methods/languages
tags: ['SDK', 'Software Development Kit', 'languages', 'languages']
---

# sailpoint.nerm.LanguagesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch-language**](#patch-language) | **PATCH** `/languages/{locale}` | Update a language by locale


## patch-language
Update a language by locale
Update a language by locale

[API Spec](https://developer.sailpoint.com/docs/api//patch-language)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | language_locale | **str** | True  | Language locale of the object
 Body  | patch_language_request | [**PatchLanguageRequest**](../models/patch-language-request) | True  | 

### Return type
[**PatchLanguageRequest**](../models/patch-language-request)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | PatchLanguageRequest |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.languages_api import LanguagesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.patch_language_request import PatchLanguageRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    language_locale = 'es' # str | Language locale of the object # str | Language locale of the object
    patch_language_request = '''sailpoint.nerm.PatchLanguageRequest()''' # PatchLanguageRequest | 

    try:
        # Update a language by locale
        new_patch_language_request = PatchLanguageRequest.from_json(patch_language_request)
        results = LanguagesApi(api_client).patch_language(language_locale=language_locale, patch_language_request=new_patch_language_request)
        # Below is a request that includes all optional parameters
        # results = LanguagesApi(api_client).patch_language(language_locale, new_patch_language_request)
        print("The response of LanguagesApi->patch_language:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling LanguagesApi->patch_language: %s\n" % e)
```



[[Back to top]](#) 



