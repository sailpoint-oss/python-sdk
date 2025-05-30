---
id: beta-requested-item-status-provisioning-details
title: RequestedItemStatusProvisioningDetails
pagination_label: RequestedItemStatusProvisioningDetails
sidebar_label: RequestedItemStatusProvisioningDetails
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RequestedItemStatusProvisioningDetails', 'BetaRequestedItemStatusProvisioningDetails'] 
slug: /tools/sdk/python/beta/models/requested-item-status-provisioning-details
tags: ['SDK', 'Software Development Kit', 'RequestedItemStatusProvisioningDetails', 'BetaRequestedItemStatusProvisioningDetails']
---

# RequestedItemStatusProvisioningDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ordered_sub_phase_references** | **str** | Ordered CSV of sub phase references to objects that contain more information about provisioning. For example, this can contain \"manualWorkItemDetails\" which indicate that there is further information in that object for this phase. | [optional] 
}

## Example

```python
from sailpoint.beta.models.requested_item_status_provisioning_details import RequestedItemStatusProvisioningDetails

requested_item_status_provisioning_details = RequestedItemStatusProvisioningDetails(
ordered_sub_phase_references='manualWorkItemDetails'
)

```
[[Back to top]](#) 

