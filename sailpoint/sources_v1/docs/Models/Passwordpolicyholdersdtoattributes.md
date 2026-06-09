---
id: passwordpolicyholdersdtoattributes
title: Passwordpolicyholdersdtoattributes
pagination_label: Passwordpolicyholdersdtoattributes
sidebar_label: Passwordpolicyholdersdtoattributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Passwordpolicyholdersdtoattributes', 'Passwordpolicyholdersdtoattributes'] 
slug: /tools/sdk/python/v1/models/passwordpolicyholdersdtoattributes
tags: ['SDK', 'Software Development Kit', 'Passwordpolicyholdersdtoattributes', 'Passwordpolicyholdersdtoattributes']
---

# Passwordpolicyholdersdtoattributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_attr** | [**[]PasswordpolicyholdersdtoattributesIdentityAttrInner**](passwordpolicyholdersdtoattributes-identity-attr-inner) | Attributes of PasswordPolicyHoldersDto | [optional] 
}

## Example

```python
from sailpoint.sources_v1.models.passwordpolicyholdersdtoattributes import Passwordpolicyholdersdtoattributes

passwordpolicyholdersdtoattributes = Passwordpolicyholdersdtoattributes(
identity_attr=[
                    sailpoint.sources_v1.models.passwordpolicyholdersdtoattributes_identity_attr_inner.passwordpolicyholdersdtoattributes_identityAttr_inner(
                        name = 'Country', 
                        value = 'Canada', )
                    ]
)

```
[[Back to top]](#) 

