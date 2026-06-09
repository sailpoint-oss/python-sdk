---
id: entitlementrequestconfig
title: Entitlementrequestconfig
pagination_label: Entitlementrequestconfig
sidebar_label: Entitlementrequestconfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Entitlementrequestconfig', 'Entitlementrequestconfig'] 
slug: /tools/sdk/python/v1/models/entitlementrequestconfig
tags: ['SDK', 'Software Development Kit', 'Entitlementrequestconfig', 'Entitlementrequestconfig']
---

# Entitlementrequestconfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_config** | [**Entitlementaccessrequestconfig**](entitlementaccessrequestconfig) |  | [optional] 
**revocation_request_config** | [**Entitlementrevocationrequestconfig**](entitlementrevocationrequestconfig) |  | [optional] 
}

## Example

```python
from sailpoint.access_requests_v1.models.entitlementrequestconfig import Entitlementrequestconfig

entitlementrequestconfig = Entitlementrequestconfig(
access_request_config=sailpoint.access_requests_v1.models.entitlement_access_request_config.Entitlement Access Request Config(
                    approval_schemes = [
                        sailpoint.access_requests_v1.models.entitlement_approval_scheme.Entitlement Approval Scheme(
                            approver_type = 'GOVERNANCE_GROUP', 
                            approver_id = 'e3eab852-8315-467f-9de7-70eda97f63c8', )
                        ], 
                    request_comment_required = True, 
                    denial_comment_required = False, 
                    reauthorization_required = False, 
                    require_end_date = True, 
                    max_permitted_access_duration = sailpoint.access_requests_v1.models.entitlementaccessrequestconfig_max_permitted_access_duration.entitlementaccessrequestconfig_maxPermittedAccessDuration(
                        value = 5, 
                        time_unit = 'DAYS', ), ),
revocation_request_config=sailpoint.access_requests_v1.models.entitlement_revocation_request_config.Entitlement Revocation Request Config(
                    approval_schemes = [
                        sailpoint.access_requests_v1.models.entitlement_approval_scheme.Entitlement Approval Scheme(
                            approver_type = 'GOVERNANCE_GROUP', 
                            approver_id = 'e3eab852-8315-467f-9de7-70eda97f63c8', )
                        ], )
)

```
[[Back to top]](#) 

