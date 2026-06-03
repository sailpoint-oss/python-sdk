---
id: v2026-app-access-profile-selector-account-match-config
title: AppAccessProfileSelectorAccountMatchConfig
pagination_label: AppAccessProfileSelectorAccountMatchConfig
sidebar_label: AppAccessProfileSelectorAccountMatchConfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AppAccessProfileSelectorAccountMatchConfig', 'V2026AppAccessProfileSelectorAccountMatchConfig'] 
slug: /tools/sdk/python/v2026/models/app-access-profile-selector-account-match-config
tags: ['SDK', 'Software Development Kit', 'AppAccessProfileSelectorAccountMatchConfig', 'V2026AppAccessProfileSelectorAccountMatchConfig']
---

# AppAccessProfileSelectorAccountMatchConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expression** | [**AppAccessProfileSelectorAccountMatchConfigMatchExpression**](app-access-profile-selector-account-match-config-match-expression) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.app_access_profile_selector_account_match_config import AppAccessProfileSelectorAccountMatchConfig

app_access_profile_selector_account_match_config = AppAccessProfileSelectorAccountMatchConfig(
match_expression=sailpoint.v2026.models.app_access_profile_selector_account_match_config_match_expression.AppAccessProfileSelector_accountMatchConfig_matchExpression(
                    match_terms = [{name=, value=, op=null, container=true, and=false, children=[{name=businessCategory, value=Service, op=eq, container=false, and=false, children=null}]}], 
                    and = True, )
)

```
[[Back to top]](#) 

