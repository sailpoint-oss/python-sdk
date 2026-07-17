---
id: app-access-profile-selector
title: AppAccessProfileSelector
pagination_label: AppAccessProfileSelector
sidebar_label: AppAccessProfileSelector
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AppAccessProfileSelector', 'AppAccessProfileSelector'] 
slug: /tools/sdk/python/apps/models/app-access-profile-selector
tags: ['SDK', 'Software Development Kit', 'AppAccessProfileSelector', 'AppAccessProfileSelector']
---

# AppAccessProfileSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The application id | [optional] 
**account_match_config** | [**AppAccessProfileSelectorAccountMatchConfig**](app-access-profile-selector-account-match-config) |  | [optional] 
}

## Example

```python
from sailpoint.apps.models.app_access_profile_selector import AppAccessProfileSelector

app_access_profile_selector = AppAccessProfileSelector(
application_id='2c91808874ff91550175097daaec161c"',
account_match_config=sailpoint.apps.models.app_access_profile_selector_account_match_config.AppAccessProfileSelector_accountMatchConfig(
                    match_expression = sailpoint.apps.models.app_access_profile_selector_account_match_config_match_expression.AppAccessProfileSelector_accountMatchConfig_matchExpression(
                        match_terms = [{"name":"","value":"","op":null,"container":true,"and":false,"children":[{"name":"businessCategory","value":"Service","op":"eq","container":false,"and":false,"children":null}]}], 
                        and = True, ), )
)

```
[[Back to top]](#) 

