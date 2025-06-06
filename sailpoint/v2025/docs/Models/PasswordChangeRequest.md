---
id: v2025-password-change-request
title: PasswordChangeRequest
pagination_label: PasswordChangeRequest
sidebar_label: PasswordChangeRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PasswordChangeRequest', 'V2025PasswordChangeRequest'] 
slug: /tools/sdk/python/v2025/models/password-change-request
tags: ['SDK', 'Software Development Kit', 'PasswordChangeRequest', 'V2025PasswordChangeRequest']
---

# PasswordChangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | The identity ID that requested the password change | [optional] 
**encrypted_password** | **str** | The RSA encrypted password | [optional] 
**public_key_id** | **str** | The encryption key ID | [optional] 
**account_id** | **str** | Account ID of the account This is specified per account schema in the source configuration. It is used to distinguish accounts. More info can be found here https://community.sailpoint.com/t5/IdentityNow-Connectors/How-do-I-designate-an-account-attribute-as-the-Account-ID-for-a/ta-p/80350 | [optional] 
**source_id** | **str** | The ID of the source for which identity is requesting the password change | [optional] 
}

## Example

```python
from sailpoint.v2025.models.password_change_request import PasswordChangeRequest

password_change_request = PasswordChangeRequest(
identity_id='8a807d4c73c545510173c545f0a002ff',
encrypted_password='XzN+YwKgr2C+InkMYFMBG3UtjMEw5ZIql/XFlXo8cJNeslmkplx6vn4kd4/43IF9STBk5RnzR6XmjpEO+FwHDoiBwYZAkAZK/Iswxk4OdybG6Y4MStJCOCiK8osKr35IMMSV/mbO4wAeltoCk7daTWzTGLiI6UaT5tf+F2EgdjJZ7YqM8W8r7aUWsm3p2Xt01Y46ZRx0QaM91QruiIx2rECFT2pUO0wr+7oQ77jypATyGWRtADsu3YcvCk/6U5MqCnXMzKBcRas7NnZdSL/d5H1GglVGz3VLPMaivG4/oL4chOMmFCRl/zVsGxZ9RhN8rxsRGFFKn+rhExTi+bax3A==',
public_key_id='YWQ2NjQ4MTItZjY0NC00MWExLWFjMjktOGNmMzU3Y2VlNjk2',
account_id='CN=Abby Smith,OU=Austin,OU=Americas,OU=Demo,DC=seri,DC=acme,DC=com',
source_id='8a807d4c73c545510173c545d4b60246'
)

```
[[Back to top]](#) 

