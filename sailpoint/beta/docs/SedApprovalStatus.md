# SedApprovalStatus

SED Approval Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_reason** | **str** | failed reason will be display if status is failed | [optional] 
**id** | **str** | Sed id | [optional] 
**status** | **str** | SUCCESS | FAILED | [optional] 

## Example

```python
from sailpoint.beta.models.sed_approval_status import SedApprovalStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SedApprovalStatus from a JSON string
sed_approval_status_instance = SedApprovalStatus.from_json(json)
# print the JSON string representation of the object
print SedApprovalStatus.to_json()

# convert the object into a dict
sed_approval_status_dict = sed_approval_status_instance.to_dict()
# create an instance of SedApprovalStatus from a dict
sed_approval_status_form_dict = sed_approval_status.from_dict(sed_approval_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


