---
id: appaccessprofileselector
title: Appaccessprofileselector
pagination_label: Appaccessprofileselector
sidebar_label: Appaccessprofileselector
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Appaccessprofileselector', 'Appaccessprofileselector'] 
slug: /tools/sdk/python/v1/models/appaccessprofileselector
tags: ['SDK', 'Software Development Kit', 'Appaccessprofileselector', 'Appaccessprofileselector']
---

# Appaccessprofileselector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The application id | [optional] 
**account_match_config** | [**AppaccessprofileselectorAccountMatchConfig**](appaccessprofileselector-account-match-config) |  | [optional] 
}

## Example

```python
from sailpoint.apps_v1.models.appaccessprofileselector import Appaccessprofileselector

appaccessprofileselector = Appaccessprofileselector(
application_id='2c91808874ff91550175097daaec161c"',
account_match_config=sailpoint.apps_v1.models.appaccessprofileselector_account_match_config.appaccessprofileselector_accountMatchConfig(
                    match_expression = sailpoint.apps_v1.models.appaccessprofileselector_account_match_config_match_expression.appaccessprofileselector_accountMatchConfig_matchExpression(
                        match_terms = [{"name":"","value":"","op":null,"container":true,"and":false,"children":[{"name":"businessCategory","value":"Service","op":"eq","container":false,"and":false,"children":null}]}], 
                        and = True, ), )
)

```
[[Back to top]](#) 

