# AccessRequestPreApproval1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **bool** | Whether or not to approve the access request. | 
**comment** | **str** | A comment about the decision to approve or deny the request. | 
**approver** | **str** | The name of the entity that approved or denied the request. | 

## Example

```python
from sailpoint.beta.models.access_request_pre_approval1 import AccessRequestPreApproval1

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestPreApproval1 from a JSON string
access_request_pre_approval1_instance = AccessRequestPreApproval1.from_json(json)
# print the JSON string representation of the object
print AccessRequestPreApproval1.to_json()

# convert the object into a dict
access_request_pre_approval1_dict = access_request_pre_approval1_instance.to_dict()
# create an instance of AccessRequestPreApproval1 from a dict
access_request_pre_approval1_form_dict = access_request_pre_approval1.from_dict(access_request_pre_approval1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


