# RequestedItemStatusProvisioningDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ordered_sub_phase_references** | **str** | Ordered CSV of sub phase references to objects that contain more information about provisioning. For example, this can contain \&quot;manualWorkItemDetails\&quot; which indicate that there is further information in that object for this phase. | [optional] 

## Example

```python
from sailpoint.beta.models.requested_item_status_provisioning_details import RequestedItemStatusProvisioningDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemStatusProvisioningDetails from a JSON string
requested_item_status_provisioning_details_instance = RequestedItemStatusProvisioningDetails.from_json(json)
# print the JSON string representation of the object
print(RequestedItemStatusProvisioningDetails.to_json())

# convert the object into a dict
requested_item_status_provisioning_details_dict = requested_item_status_provisioning_details_instance.to_dict()
# create an instance of RequestedItemStatusProvisioningDetails from a dict
requested_item_status_provisioning_details_from_dict = RequestedItemStatusProvisioningDetails.from_dict(requested_item_status_provisioning_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


