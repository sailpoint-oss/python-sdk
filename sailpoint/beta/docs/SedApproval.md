# SedApproval

Sed Approval Request Body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** | List of SED id&#39;s | [optional] 

## Example

```python
from sailpoint.beta.models.sed_approval import SedApproval

# TODO update the JSON string below
json = "{}"
# create an instance of SedApproval from a JSON string
sed_approval_instance = SedApproval.from_json(json)
# print the JSON string representation of the object
print SedApproval.to_json()

# convert the object into a dict
sed_approval_dict = sed_approval_instance.to_dict()
# create an instance of SedApproval from a dict
sed_approval_form_dict = sed_approval.from_dict(sed_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


