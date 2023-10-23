# MultiPolicyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filtered_policy_list** | **List[str]** | Multi-policy report will be run for this list of ids | [optional] 

## Example

```python
from v3.models.multi_policy_request import MultiPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MultiPolicyRequest from a JSON string
multi_policy_request_instance = MultiPolicyRequest.from_json(json)
# print the JSON string representation of the object
print MultiPolicyRequest.to_json()

# convert the object into a dict
multi_policy_request_dict = multi_policy_request_instance.to_dict()
# create an instance of MultiPolicyRequest from a dict
multi_policy_request_form_dict = multi_policy_request.from_dict(multi_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


