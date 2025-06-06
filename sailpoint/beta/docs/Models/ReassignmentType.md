---
id: beta-reassignment-type
title: ReassignmentType
pagination_label: ReassignmentType
sidebar_label: ReassignmentType
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ReassignmentType', 'BetaReassignmentType'] 
slug: /tools/sdk/python/beta/models/reassignment-type
tags: ['SDK', 'Software Development Kit', 'ReassignmentType', 'BetaReassignmentType']
---

# ReassignmentType

The approval reassignment type.  * MANUAL_REASSIGNMENT: An approval with this reassignment type has been specifically reassigned by the approval task's owner, from their queue to someone else's.  * AUTOMATIC_REASSIGNMENT: An approval with this reassignment type has been automatically reassigned from another approver's queue, according to that approver's reassignment configuration. The approver's reassignment configuration may be set up to automatically reassign approval tasks for a defined (or possibly open-ended) period of time. * AUTO_ESCALATION: An approval with this reassignment type has been automatically reassigned from another approver's queue, according to the request's escalation configuration. For more information about escalation configuration, refer to [Setting Global Reminders and Escalation Policies](https://documentation.sailpoint.com/saas/help/requests/config_emails.html). * SELF_REVIEW_DELEGATION: An approval with this reassignment type has been automatically reassigned by the system to prevent self-review. This helps prevent situations like a requester being tasked with approving their own request. For more information about preventing self-review, refer to [Self-review Prevention](https://documentation.sailpoint.com/saas/help/users/work_reassignment.html#self-review-prevention) and [Preventing Self-approval](https://documentation.sailpoint.com/saas/help/requests/config_ap_roles.html#preventing-self-approval).

## Enum

* `MANUAL_REASSIGNMENT` (value: `'MANUAL_REASSIGNMENT'`)

* `AUTOMATIC_REASSIGNMENT` (value: `'AUTOMATIC_REASSIGNMENT'`)

* `AUTO_ESCALATION` (value: `'AUTO_ESCALATION'`)

* `SELF_REVIEW_DELEGATION` (value: `'SELF_REVIEW_DELEGATION'`)

[[Back to top]](#) 

