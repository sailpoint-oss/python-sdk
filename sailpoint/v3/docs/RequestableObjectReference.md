# RequestableObjectReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the object. | [optional] 
**name** | **str** | Name of the object. | [optional] 
**description** | **str** | Description of the object. | [optional] 
**type** | **str** | Type of the object. | [optional] 

## Example

```python
from sailpoint.v3.models.requestable_object_reference import RequestableObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of RequestableObjectReference from a JSON string
requestable_object_reference_instance = RequestableObjectReference.from_json(json)
# print the JSON string representation of the object
print RequestableObjectReference.to_json()

# convert the object into a dict
requestable_object_reference_dict = requestable_object_reference_instance.to_dict()
# create an instance of RequestableObjectReference from a dict
requestable_object_reference_form_dict = requestable_object_reference.from_dict(requestable_object_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


