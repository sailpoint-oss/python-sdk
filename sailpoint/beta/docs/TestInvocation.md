# TestInvocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_id** | **str** | Trigger ID | 
**input** | **object** | Mock input to use for test invocation.  This must adhere to the input schema defined in the trigger being invoked.  If this property is omitted, then the default trigger sample payload will be sent. | [optional] 
**content_json** | **object** | JSON map of invocation metadata. | 
**subscription_ids** | **List[str]** | Only send the test event to the subscription IDs listed.  If omitted, the test event will be sent to all subscribers. | [optional] 

## Example

```python
from sailpoint.beta.models.test_invocation import TestInvocation

# TODO update the JSON string below
json = "{}"
# create an instance of TestInvocation from a JSON string
test_invocation_instance = TestInvocation.from_json(json)
# print the JSON string representation of the object
print(TestInvocation.to_json())

# convert the object into a dict
test_invocation_dict = test_invocation_instance.to_dict()
# create an instance of TestInvocation from a dict
test_invocation_from_dict = TestInvocation.from_dict(test_invocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


