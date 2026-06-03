---
id: v2026-app-access-profile-selector-account-match-config-match-expression
title: AppAccessProfileSelectorAccountMatchConfigMatchExpression
pagination_label: AppAccessProfileSelectorAccountMatchConfigMatchExpression
sidebar_label: AppAccessProfileSelectorAccountMatchConfigMatchExpression
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AppAccessProfileSelectorAccountMatchConfigMatchExpression', 'V2026AppAccessProfileSelectorAccountMatchConfigMatchExpression'] 
slug: /tools/sdk/python/v2026/models/app-access-profile-selector-account-match-config-match-expression
tags: ['SDK', 'Software Development Kit', 'AppAccessProfileSelectorAccountMatchConfigMatchExpression', 'V2026AppAccessProfileSelectorAccountMatchConfigMatchExpression']
---

# AppAccessProfileSelectorAccountMatchConfigMatchExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_terms** | [**[]MatchTerm**](match-term) |  | [optional] 
**var_and** | **bool** | If it is AND operators for match terms | [optional] [default to True]
}

## Example

```python
from sailpoint.v2026.models.app_access_profile_selector_account_match_config_match_expression import AppAccessProfileSelectorAccountMatchConfigMatchExpression

app_access_profile_selector_account_match_config_match_expression = AppAccessProfileSelectorAccountMatchConfigMatchExpression(
match_terms=[{name=, value=, op=null, container=true, and=false, children=[{name=businessCategory, value=Service, op=eq, container=false, and=false, children=null}]}],
var_and=True
)

```
[[Back to top]](#) 

