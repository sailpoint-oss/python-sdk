# ProvisioningDetails

Provides additional details about provisioning for this request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ordered_sub_phase_references** | **str** | Ordered CSV of sub phase references to objects that contain more information about provisioning. For example, this can contain \&quot;manualWorkItemDetails\&quot; which indicate that there is further information in that object for this phase. | [optional] 

## Example

```python
from sailpoint.v3.models.provisioning_details import ProvisioningDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningDetails from a JSON string
provisioning_details_instance = ProvisioningDetails.from_json(json)
# print the JSON string representation of the object
print ProvisioningDetails.to_json()

# convert the object into a dict
provisioning_details_dict = provisioning_details_instance.to_dict()
# create an instance of ProvisioningDetails from a dict
provisioning_details_form_dict = provisioning_details.from_dict(provisioning_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


