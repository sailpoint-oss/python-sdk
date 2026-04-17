---
id: workflow-actions
title: Workflow_actions
pagination_label: workflow_actions
sidebar_label: workflow_actions
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'workflow_actions', 'workflow_actions'] 
slug: /tools/sdk/python//methods/workflow-actions
tags: ['SDK', 'Software Development Kit', 'workflow_actions', 'workflow_actions']
---

# sailpoint.nerm.WorkflowActionsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-approval-action**](#create-approval-action) | **POST** `/workflow_actions/approval_actions` | Create an approval action
[**create-ask-security-question-action**](#create-ask-security-question-action) | **POST** `/workflow_actions/ask_security_question_actions` | Create ask security question action
[**create-auto-assign-action**](#create-auto-assign-action) | **POST** `/workflow_actions/auto_assign_actions` | Create an auto assign action
[**create-batch-update-action**](#create-batch-update-action) | **POST** `/workflow_actions/batch_update_actions` | Create a batch update action
[**create-close-session-action**](#create-close-session-action) | **POST** `/workflow_actions/close_session_actions` | Create a close session action
[**create-contributors-action**](#create-contributors-action) | **POST** `/workflow_actions/contributors_actions` | Create a contributors action
[**create-create-profile-action**](#create-create-profile-action) | **POST** `/workflow_actions/create_profile_actions` | Create a create profile action
[**create-duplicate-prevention-action**](#create-duplicate-prevention-action) | **POST** `/workflow_actions/duplicate_prevention_actions` | Create a duplicate prevention action
[**create-email-verification-action**](#create-email-verification-action) | **POST** `/workflow_actions/email_verification_actions` | Create an email verification action
[**create-fulfillment-action**](#create-fulfillment-action) | **POST** `/workflow_actions/fulfillment_actions` | Create a fulfillment action
[**create-identity-proofing-action**](#create-identity-proofing-action) | **POST** `/workflow_actions/identity_proofing_actions` | Create an identity proofing action
[**create-invitation-action**](#create-invitation-action) | **POST** `/workflow_actions/invitation_actions` | Create an invitation action
[**create-ldap-action**](#create-ldap-action) | **POST** `/workflow_actions/ldap_actions` | Create a ldap action
[**create-notification-action**](#create-notification-action) | **POST** `/workflow_actions/notification_actions` | Create a notification action
[**create-password-reset-action**](#create-password-reset-action) | **POST** `/workflow_actions/password_reset_actions` | Create a password reset action
[**create-profile-check-action**](#create-profile-check-action) | **POST** `/workflow_actions/profile_check_actions` | Create a profile check action
[**create-profile-select-action**](#create-profile-select-action) | **POST** `/workflow_actions/profile_select_actions` | Create a profile select action
[**create-request-action**](#create-request-action) | **POST** `/workflow_actions/request_actions` | Create a request action
[**create-rest-api-action**](#create-rest-api-action) | **POST** `/workflow_actions/rest_api_actions` | Create a REST API action
[**create-review-action**](#create-review-action) | **POST** `/workflow_actions/review_actions` | Create a review action
[**create-run-workflow-action**](#create-run-workflow-action) | **POST** `/workflow_actions/run_workflow_actions` | Create a run workflow action
[**create-set-attributes-action**](#create-set-attributes-action) | **POST** `/workflow_actions/set_attributes_actions` | Create a set attributes action
[**create-set-security-question-action**](#create-set-security-question-action) | **POST** `/workflow_actions/set_security_question_actions` | Create set security question action
[**create-soap-api-action**](#create-soap-api-action) | **POST** `/workflow_actions/soap_api_actions` | Create a SOAP API action
[**create-status-change-action**](#create-status-change-action) | **POST** `/workflow_actions/status_change_actions` | Create a status change action
[**create-unassign-action**](#create-unassign-action) | **POST** `/workflow_actions/unassign_actions` | Create an unassign action
[**create-update-profile-action**](#create-update-profile-action) | **POST** `/workflow_actions/update_profile_actions` | Create an update profile action
[**create-username-password-action**](#create-username-password-action) | **POST** `/workflow_actions/username_password_actions` | Create a username password action
[**get-workflow-actions**](#get-workflow-actions) | **GET** `/workflow_actions` | Get Workflow Actions


## create-approval-action
Create an approval action
Create an approval action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - workflow_action_performers, workflow_action_roles, workflow_action_performer_notification_email, workflow_action_approval_email, workflow_action_rejection_email. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-approval-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_approval_action_request | [**CreateApprovalActionRequest**](../models/create-approval-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_approval_action_request import CreateApprovalActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_approval_action_request = '''sailpoint.nerm.CreateApprovalActionRequest()''' # CreateApprovalActionRequest | 

    try:
        # Create an approval action
        new_create_approval_action_request = CreateApprovalActionRequest.from_json(create_approval_action_request)
        results = WorkflowActionsApi(api_client).create_approval_action(create_approval_action_request=new_create_approval_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_approval_action(new_create_approval_action_request)
        print("The response of WorkflowActionsApi->create_approval_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_approval_action: %s\n" % e)
```



[[Back to top]](#) 

## create-ask-security-question-action
Create ask security question action
Create an ask security question action

[API Spec](https://developer.sailpoint.com/docs/api//create-ask-security-question-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_ask_security_question_action_request | [**CreateAskSecurityQuestionActionRequest**](../models/create-ask-security-question-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_ask_security_question_action_request import CreateAskSecurityQuestionActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_ask_security_question_action_request = '''sailpoint.nerm.CreateAskSecurityQuestionActionRequest()''' # CreateAskSecurityQuestionActionRequest | 

    try:
        # Create ask security question action
        new_create_ask_security_question_action_request = CreateAskSecurityQuestionActionRequest.from_json(create_ask_security_question_action_request)
        results = WorkflowActionsApi(api_client).create_ask_security_question_action(create_ask_security_question_action_request=new_create_ask_security_question_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_ask_security_question_action(new_create_ask_security_question_action_request)
        print("The response of WorkflowActionsApi->create_ask_security_question_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_ask_security_question_action: %s\n" % e)
```



[[Back to top]](#) 

## create-auto-assign-action
Create an auto assign action
Create an auto assign action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - workflow_action_roles. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-auto-assign-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_auto_assign_action_request | [**CreateAutoAssignActionRequest**](../models/create-auto-assign-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_auto_assign_action_request import CreateAutoAssignActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_auto_assign_action_request = '''sailpoint.nerm.CreateAutoAssignActionRequest()''' # CreateAutoAssignActionRequest | 

    try:
        # Create an auto assign action
        new_create_auto_assign_action_request = CreateAutoAssignActionRequest.from_json(create_auto_assign_action_request)
        results = WorkflowActionsApi(api_client).create_auto_assign_action(create_auto_assign_action_request=new_create_auto_assign_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_auto_assign_action(new_create_auto_assign_action_request)
        print("The response of WorkflowActionsApi->create_auto_assign_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_auto_assign_action: %s\n" % e)
```



[[Back to top]](#) 

## create-batch-update-action
Create a batch update action
Create a batch update action

[API Spec](https://developer.sailpoint.com/docs/api//create-batch-update-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_batch_update_action_request | [**CreateBatchUpdateActionRequest**](../models/create-batch-update-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_batch_update_action_request import CreateBatchUpdateActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_batch_update_action_request = '''sailpoint.nerm.CreateBatchUpdateActionRequest()''' # CreateBatchUpdateActionRequest | 

    try:
        # Create a batch update action
        new_create_batch_update_action_request = CreateBatchUpdateActionRequest.from_json(create_batch_update_action_request)
        results = WorkflowActionsApi(api_client).create_batch_update_action(create_batch_update_action_request=new_create_batch_update_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_batch_update_action(new_create_batch_update_action_request)
        print("The response of WorkflowActionsApi->create_batch_update_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_batch_update_action: %s\n" % e)
```



[[Back to top]](#) 

## create-close-session-action
Create a close session action
Create a close session action

[API Spec](https://developer.sailpoint.com/docs/api//create-close-session-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_close_session_action_request | [**CreateCloseSessionActionRequest**](../models/create-close-session-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_close_session_action_request import CreateCloseSessionActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_close_session_action_request = '''sailpoint.nerm.CreateCloseSessionActionRequest()''' # CreateCloseSessionActionRequest | 

    try:
        # Create a close session action
        new_create_close_session_action_request = CreateCloseSessionActionRequest.from_json(create_close_session_action_request)
        results = WorkflowActionsApi(api_client).create_close_session_action(create_close_session_action_request=new_create_close_session_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_close_session_action(new_create_close_session_action_request)
        print("The response of WorkflowActionsApi->create_close_session_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_close_session_action: %s\n" % e)
```



[[Back to top]](#) 

## create-contributors-action
Create a contributors action
Create a contributors action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - workflow_action_performers, workflow_action_roles, workflow_action_performer_notification_email. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-contributors-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_contributors_action_request | [**CreateContributorsActionRequest**](../models/create-contributors-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_contributors_action_request import CreateContributorsActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_contributors_action_request = '''sailpoint.nerm.CreateContributorsActionRequest()''' # CreateContributorsActionRequest | 

    try:
        # Create a contributors action
        new_create_contributors_action_request = CreateContributorsActionRequest.from_json(create_contributors_action_request)
        results = WorkflowActionsApi(api_client).create_contributors_action(create_contributors_action_request=new_create_contributors_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_contributors_action(new_create_contributors_action_request)
        print("The response of WorkflowActionsApi->create_contributors_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_contributors_action: %s\n" % e)
```



[[Back to top]](#) 

## create-create-profile-action
Create a create profile action
Create a create profile action

[API Spec](https://developer.sailpoint.com/docs/api//create-create-profile-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_create_profile_action_request | [**CreateCreateProfileActionRequest**](../models/create-create-profile-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_create_profile_action_request import CreateCreateProfileActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_create_profile_action_request = '''sailpoint.nerm.CreateCreateProfileActionRequest()''' # CreateCreateProfileActionRequest | 

    try:
        # Create a create profile action
        new_create_create_profile_action_request = CreateCreateProfileActionRequest.from_json(create_create_profile_action_request)
        results = WorkflowActionsApi(api_client).create_create_profile_action(create_create_profile_action_request=new_create_create_profile_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_create_profile_action(new_create_create_profile_action_request)
        print("The response of WorkflowActionsApi->create_create_profile_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_create_profile_action: %s\n" % e)
```



[[Back to top]](#) 

## create-duplicate-prevention-action
Create a duplicate prevention action
Create a duplicate prevention action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - duplicatation_prevention_attributes, workflow_action_performers, workflow_action_roles, workflow_action_performer_notification_email. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-duplicate-prevention-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_duplicate_prevention_action_request | [**CreateDuplicatePreventionActionRequest**](../models/create-duplicate-prevention-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_duplicate_prevention_action_request import CreateDuplicatePreventionActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_duplicate_prevention_action_request = '''sailpoint.nerm.CreateDuplicatePreventionActionRequest()''' # CreateDuplicatePreventionActionRequest | 

    try:
        # Create a duplicate prevention action
        new_create_duplicate_prevention_action_request = CreateDuplicatePreventionActionRequest.from_json(create_duplicate_prevention_action_request)
        results = WorkflowActionsApi(api_client).create_duplicate_prevention_action(create_duplicate_prevention_action_request=new_create_duplicate_prevention_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_duplicate_prevention_action(new_create_duplicate_prevention_action_request)
        print("The response of WorkflowActionsApi->create_duplicate_prevention_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_duplicate_prevention_action: %s\n" % e)
```



[[Back to top]](#) 

## create-email-verification-action
Create an email verification action
Create an email verification action

[API Spec](https://developer.sailpoint.com/docs/api//create-email-verification-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_email_verification_action_request | [**CreateEmailVerificationActionRequest**](../models/create-email-verification-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_email_verification_action_request import CreateEmailVerificationActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_email_verification_action_request = '''sailpoint.nerm.CreateEmailVerificationActionRequest()''' # CreateEmailVerificationActionRequest | 

    try:
        # Create an email verification action
        new_create_email_verification_action_request = CreateEmailVerificationActionRequest.from_json(create_email_verification_action_request)
        results = WorkflowActionsApi(api_client).create_email_verification_action(create_email_verification_action_request=new_create_email_verification_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_email_verification_action(new_create_email_verification_action_request)
        print("The response of WorkflowActionsApi->create_email_verification_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_email_verification_action: %s\n" % e)
```



[[Back to top]](#) 

## create-fulfillment-action
Create a fulfillment action
Create a fulfillment action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - workflow_action_performers, workflow_action_roles, workflow_action_performer_notification_email. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-fulfillment-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_fulfillment_action_request | [**CreateFulfillmentActionRequest**](../models/create-fulfillment-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_fulfillment_action_request import CreateFulfillmentActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_fulfillment_action_request = '''sailpoint.nerm.CreateFulfillmentActionRequest()''' # CreateFulfillmentActionRequest | 

    try:
        # Create a fulfillment action
        new_create_fulfillment_action_request = CreateFulfillmentActionRequest.from_json(create_fulfillment_action_request)
        results = WorkflowActionsApi(api_client).create_fulfillment_action(create_fulfillment_action_request=new_create_fulfillment_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_fulfillment_action(new_create_fulfillment_action_request)
        print("The response of WorkflowActionsApi->create_fulfillment_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_fulfillment_action: %s\n" % e)
```



[[Back to top]](#) 

## create-identity-proofing-action
Create an identity proofing action
Create an identity proofing action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - identity_proofing_action_configuration, identity_proofing_action_mappings. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-identity-proofing-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_identity_proofing_action_request | [**CreateIdentityProofingActionRequest**](../models/create-identity-proofing-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_identity_proofing_action_request import CreateIdentityProofingActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_identity_proofing_action_request = '''sailpoint.nerm.CreateIdentityProofingActionRequest()''' # CreateIdentityProofingActionRequest | 

    try:
        # Create an identity proofing action
        new_create_identity_proofing_action_request = CreateIdentityProofingActionRequest.from_json(create_identity_proofing_action_request)
        results = WorkflowActionsApi(api_client).create_identity_proofing_action(create_identity_proofing_action_request=new_create_identity_proofing_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_identity_proofing_action(new_create_identity_proofing_action_request)
        print("The response of WorkflowActionsApi->create_identity_proofing_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_identity_proofing_action: %s\n" % e)
```



[[Back to top]](#) 

## create-invitation-action
Create an invitation action
Create an invitation action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - workflow_action_pause_action. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-invitation-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_invitation_action_request | [**CreateInvitationActionRequest**](../models/create-invitation-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_invitation_action_request import CreateInvitationActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_invitation_action_request = '''sailpoint.nerm.CreateInvitationActionRequest()''' # CreateInvitationActionRequest | 

    try:
        # Create an invitation action
        new_create_invitation_action_request = CreateInvitationActionRequest.from_json(create_invitation_action_request)
        results = WorkflowActionsApi(api_client).create_invitation_action(create_invitation_action_request=new_create_invitation_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_invitation_action(new_create_invitation_action_request)
        print("The response of WorkflowActionsApi->create_invitation_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_invitation_action: %s\n" % e)
```



[[Back to top]](#) 

## create-ldap-action
Create a ldap action
Create a ldap action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - workflow_action_performers, workflow_action_roles. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-ldap-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_ldap_action_request | [**CreateLdapActionRequest**](../models/create-ldap-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_ldap_action_request import CreateLdapActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_ldap_action_request = '''sailpoint.nerm.CreateLdapActionRequest()''' # CreateLdapActionRequest | 

    try:
        # Create a ldap action
        new_create_ldap_action_request = CreateLdapActionRequest.from_json(create_ldap_action_request)
        results = WorkflowActionsApi(api_client).create_ldap_action(create_ldap_action_request=new_create_ldap_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_ldap_action(new_create_ldap_action_request)
        print("The response of WorkflowActionsApi->create_ldap_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_ldap_action: %s\n" % e)
```



[[Back to top]](#) 

## create-notification-action
Create a notification action
Create a notification action

[API Spec](https://developer.sailpoint.com/docs/api//create-notification-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_notification_action_request | [**CreateNotificationActionRequest**](../models/create-notification-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_notification_action_request import CreateNotificationActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_notification_action_request = '''sailpoint.nerm.CreateNotificationActionRequest()''' # CreateNotificationActionRequest | 

    try:
        # Create a notification action
        new_create_notification_action_request = CreateNotificationActionRequest.from_json(create_notification_action_request)
        results = WorkflowActionsApi(api_client).create_notification_action(create_notification_action_request=new_create_notification_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_notification_action(new_create_notification_action_request)
        print("The response of WorkflowActionsApi->create_notification_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_notification_action: %s\n" % e)
```



[[Back to top]](#) 

## create-password-reset-action
Create a password reset action
Create a password reset action

[API Spec](https://developer.sailpoint.com/docs/api//create-password-reset-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_password_reset_action_request | [**CreatePasswordResetActionRequest**](../models/create-password-reset-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_password_reset_action_request import CreatePasswordResetActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_password_reset_action_request = '''sailpoint.nerm.CreatePasswordResetActionRequest()''' # CreatePasswordResetActionRequest | 

    try:
        # Create a password reset action
        new_create_password_reset_action_request = CreatePasswordResetActionRequest.from_json(create_password_reset_action_request)
        results = WorkflowActionsApi(api_client).create_password_reset_action(create_password_reset_action_request=new_create_password_reset_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_password_reset_action(new_create_password_reset_action_request)
        print("The response of WorkflowActionsApi->create_password_reset_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_password_reset_action: %s\n" % e)
```



[[Back to top]](#) 

## create-profile-check-action
Create a profile check action
Create a profile check action

[API Spec](https://developer.sailpoint.com/docs/api//create-profile-check-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_profile_check_action_request | [**CreateProfileCheckActionRequest**](../models/create-profile-check-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_profile_check_action_request import CreateProfileCheckActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_profile_check_action_request = '''sailpoint.nerm.CreateProfileCheckActionRequest()''' # CreateProfileCheckActionRequest | 

    try:
        # Create a profile check action
        new_create_profile_check_action_request = CreateProfileCheckActionRequest.from_json(create_profile_check_action_request)
        results = WorkflowActionsApi(api_client).create_profile_check_action(create_profile_check_action_request=new_create_profile_check_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_profile_check_action(new_create_profile_check_action_request)
        print("The response of WorkflowActionsApi->create_profile_check_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_profile_check_action: %s\n" % e)
```



[[Back to top]](#) 

## create-profile-select-action
Create a profile select action
Create a profile select action

[API Spec](https://developer.sailpoint.com/docs/api//create-profile-select-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_profile_select_action_request | [**CreateProfileSelectActionRequest**](../models/create-profile-select-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_profile_select_action_request import CreateProfileSelectActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_profile_select_action_request = '''sailpoint.nerm.CreateProfileSelectActionRequest()''' # CreateProfileSelectActionRequest | 

    try:
        # Create a profile select action
        new_create_profile_select_action_request = CreateProfileSelectActionRequest.from_json(create_profile_select_action_request)
        results = WorkflowActionsApi(api_client).create_profile_select_action(create_profile_select_action_request=new_create_profile_select_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_profile_select_action(new_create_profile_select_action_request)
        print("The response of WorkflowActionsApi->create_profile_select_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_profile_select_action: %s\n" % e)
```



[[Back to top]](#) 

## create-request-action
Create a request action
Create a request action

[API Spec](https://developer.sailpoint.com/docs/api//create-request-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_request_action_request | [**CreateRequestActionRequest**](../models/create-request-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_request_action_request import CreateRequestActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_request_action_request = '''sailpoint.nerm.CreateRequestActionRequest()''' # CreateRequestActionRequest | 

    try:
        # Create a request action
        new_create_request_action_request = CreateRequestActionRequest.from_json(create_request_action_request)
        results = WorkflowActionsApi(api_client).create_request_action(create_request_action_request=new_create_request_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_request_action(new_create_request_action_request)
        print("The response of WorkflowActionsApi->create_request_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_request_action: %s\n" % e)
```



[[Back to top]](#) 

## create-rest-api-action
Create a REST API action
Create a REST API action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - rest_api_action_configuration, api_configuration_attributes. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-rest-api-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_rest_api_action_request | [**CreateRestApiActionRequest**](../models/create-rest-api-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_rest_api_action_request import CreateRestApiActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_rest_api_action_request = '''sailpoint.nerm.CreateRestApiActionRequest()''' # CreateRestApiActionRequest | 

    try:
        # Create a REST API action
        new_create_rest_api_action_request = CreateRestApiActionRequest.from_json(create_rest_api_action_request)
        results = WorkflowActionsApi(api_client).create_rest_api_action(create_rest_api_action_request=new_create_rest_api_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_rest_api_action(new_create_rest_api_action_request)
        print("The response of WorkflowActionsApi->create_rest_api_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_rest_api_action: %s\n" % e)
```



[[Back to top]](#) 

## create-review-action
Create a review action
Create a review action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - workflow_action_performer_notification_email. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-review-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_review_action_request | [**CreateReviewActionRequest**](../models/create-review-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_review_action_request import CreateReviewActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_review_action_request = '''sailpoint.nerm.CreateReviewActionRequest()''' # CreateReviewActionRequest | 

    try:
        # Create a review action
        new_create_review_action_request = CreateReviewActionRequest.from_json(create_review_action_request)
        results = WorkflowActionsApi(api_client).create_review_action(create_review_action_request=new_create_review_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_review_action(new_create_review_action_request)
        print("The response of WorkflowActionsApi->create_review_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_review_action: %s\n" % e)
```



[[Back to top]](#) 

## create-run-workflow-action
Create a run workflow action
Create a run workflow action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - configuration_profile_attribute. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-run-workflow-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_run_workflow_action_request | [**CreateRunWorkflowActionRequest**](../models/create-run-workflow-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_run_workflow_action_request import CreateRunWorkflowActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_run_workflow_action_request = '''sailpoint.nerm.CreateRunWorkflowActionRequest()''' # CreateRunWorkflowActionRequest | 

    try:
        # Create a run workflow action
        new_create_run_workflow_action_request = CreateRunWorkflowActionRequest.from_json(create_run_workflow_action_request)
        results = WorkflowActionsApi(api_client).create_run_workflow_action(create_run_workflow_action_request=new_create_run_workflow_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_run_workflow_action(new_create_run_workflow_action_request)
        print("The response of WorkflowActionsApi->create_run_workflow_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_run_workflow_action: %s\n" % e)
```



[[Back to top]](#) 

## create-set-attributes-action
Create a set attributes action
Create a set attributes action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - workflow_action_set_attributes. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-set-attributes-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_set_attributes_action_request | [**CreateSetAttributesActionRequest**](../models/create-set-attributes-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_set_attributes_action_request import CreateSetAttributesActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_set_attributes_action_request = '''sailpoint.nerm.CreateSetAttributesActionRequest()''' # CreateSetAttributesActionRequest | 

    try:
        # Create a set attributes action
        new_create_set_attributes_action_request = CreateSetAttributesActionRequest.from_json(create_set_attributes_action_request)
        results = WorkflowActionsApi(api_client).create_set_attributes_action(create_set_attributes_action_request=new_create_set_attributes_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_set_attributes_action(new_create_set_attributes_action_request)
        print("The response of WorkflowActionsApi->create_set_attributes_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_set_attributes_action: %s\n" % e)
```



[[Back to top]](#) 

## create-set-security-question-action
Create set security question action
Create a set security question action

[API Spec](https://developer.sailpoint.com/docs/api//create-set-security-question-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_set_security_question_action_request | [**CreateSetSecurityQuestionActionRequest**](../models/create-set-security-question-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_set_security_question_action_request import CreateSetSecurityQuestionActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_set_security_question_action_request = '''sailpoint.nerm.CreateSetSecurityQuestionActionRequest()''' # CreateSetSecurityQuestionActionRequest | 

    try:
        # Create set security question action
        new_create_set_security_question_action_request = CreateSetSecurityQuestionActionRequest.from_json(create_set_security_question_action_request)
        results = WorkflowActionsApi(api_client).create_set_security_question_action(create_set_security_question_action_request=new_create_set_security_question_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_set_security_question_action(new_create_set_security_question_action_request)
        print("The response of WorkflowActionsApi->create_set_security_question_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_set_security_question_action: %s\n" % e)
```



[[Back to top]](#) 

## create-soap-api-action
Create a SOAP API action
Create a SOAP API action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - soap_api_action_configuration, api_configuration_attributes. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-soap-api-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_soap_api_action_request | [**CreateSoapApiActionRequest**](../models/create-soap-api-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_soap_api_action_request import CreateSoapApiActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_soap_api_action_request = '''sailpoint.nerm.CreateSoapApiActionRequest()''' # CreateSoapApiActionRequest | 

    try:
        # Create a SOAP API action
        new_create_soap_api_action_request = CreateSoapApiActionRequest.from_json(create_soap_api_action_request)
        results = WorkflowActionsApi(api_client).create_soap_api_action(create_soap_api_action_request=new_create_soap_api_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_soap_api_action(new_create_soap_api_action_request)
        print("The response of WorkflowActionsApi->create_soap_api_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_soap_api_action: %s\n" % e)
```



[[Back to top]](#) 

## create-status-change-action
Create a status change action
Create a status change action

[API Spec](https://developer.sailpoint.com/docs/api//create-status-change-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_status_change_action_request | [**CreateStatusChangeActionRequest**](../models/create-status-change-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_status_change_action_request import CreateStatusChangeActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_status_change_action_request = '''sailpoint.nerm.CreateStatusChangeActionRequest()''' # CreateStatusChangeActionRequest | 

    try:
        # Create a status change action
        new_create_status_change_action_request = CreateStatusChangeActionRequest.from_json(create_status_change_action_request)
        results = WorkflowActionsApi(api_client).create_status_change_action(create_status_change_action_request=new_create_status_change_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_status_change_action(new_create_status_change_action_request)
        print("The response of WorkflowActionsApi->create_status_change_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_status_change_action: %s\n" % e)
```



[[Back to top]](#) 

## create-unassign-action
Create an unassign action
Create an unassign action. The following supporting objects will need to be created after this action is created (which are tied together via workflow_action_id) - workflow_action_roles. These supporting objects must be created for this action to be complete (APIs for these supporting objects not yet implemented, use UI).

[API Spec](https://developer.sailpoint.com/docs/api//create-unassign-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_unassign_action_request | [**CreateUnassignActionRequest**](../models/create-unassign-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_unassign_action_request import CreateUnassignActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_unassign_action_request = '''sailpoint.nerm.CreateUnassignActionRequest()''' # CreateUnassignActionRequest | 

    try:
        # Create an unassign action
        new_create_unassign_action_request = CreateUnassignActionRequest.from_json(create_unassign_action_request)
        results = WorkflowActionsApi(api_client).create_unassign_action(create_unassign_action_request=new_create_unassign_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_unassign_action(new_create_unassign_action_request)
        print("The response of WorkflowActionsApi->create_unassign_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_unassign_action: %s\n" % e)
```



[[Back to top]](#) 

## create-update-profile-action
Create an update profile action
Create an update profile action

[API Spec](https://developer.sailpoint.com/docs/api//create-update-profile-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_update_profile_action_request | [**CreateUpdateProfileActionRequest**](../models/create-update-profile-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_update_profile_action_request import CreateUpdateProfileActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_update_profile_action_request = '''sailpoint.nerm.CreateUpdateProfileActionRequest()''' # CreateUpdateProfileActionRequest | 

    try:
        # Create an update profile action
        new_create_update_profile_action_request = CreateUpdateProfileActionRequest.from_json(create_update_profile_action_request)
        results = WorkflowActionsApi(api_client).create_update_profile_action(create_update_profile_action_request=new_create_update_profile_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_update_profile_action(new_create_update_profile_action_request)
        print("The response of WorkflowActionsApi->create_update_profile_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_update_profile_action: %s\n" % e)
```



[[Back to top]](#) 

## create-username-password-action
Create a username password action
Create a username password action

[API Spec](https://developer.sailpoint.com/docs/api//create-username-password-action)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_username_password_action_request | [**CreateUsernamePasswordActionRequest**](../models/create-username-password-action-request) | True  | 

### Return type
[**CreateApprovalAction200Response**](../models/create-approval-action200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateApprovalAction200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response
from sailpoint.nerm.models.create_username_password_action_request import CreateUsernamePasswordActionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_username_password_action_request = '''sailpoint.nerm.CreateUsernamePasswordActionRequest()''' # CreateUsernamePasswordActionRequest | 

    try:
        # Create a username password action
        new_create_username_password_action_request = CreateUsernamePasswordActionRequest.from_json(create_username_password_action_request)
        results = WorkflowActionsApi(api_client).create_username_password_action(create_username_password_action_request=new_create_username_password_action_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).create_username_password_action(new_create_username_password_action_request)
        print("The response of WorkflowActionsApi->create_username_password_action:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->create_username_password_action: %s\n" % e)
```



[[Back to top]](#) 

## get-workflow-actions
Get Workflow Actions
This endpoint can retrieve workflow actions

[API Spec](https://developer.sailpoint.com/docs/api//get-workflow-actions)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | workflow_id | **str** |   (optional) | Workflow ID for filtering

### Return type
[**GetWorkflowActions200Response**](../models/get-workflow-actions200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetWorkflowActions200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_actions_api import WorkflowActionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_workflow_actions200_response import GetWorkflowActions200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    workflow_id = 'bba9cfb2-96c1-4acb-ac79-a21732527265' # str | Workflow ID for filtering (optional) # str | Workflow ID for filtering (optional)

    try:
        # Get Workflow Actions
        
        results = WorkflowActionsApi(api_client).get_workflow_actions()
        # Below is a request that includes all optional parameters
        # results = WorkflowActionsApi(api_client).get_workflow_actions(workflow_id)
        print("The response of WorkflowActionsApi->get_workflow_actions:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->get_workflow_actions: %s\n" % e)
```



[[Back to top]](#) 



