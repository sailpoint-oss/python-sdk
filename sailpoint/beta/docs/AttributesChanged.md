# AttributesChanged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[AttributeChange]**](AttributeChange.md) |  | [optional] 
**event_type** | **str** | the event type | [optional] 
**identity_id** | **str** | the identity id | [optional] 
**dt** | **str** | the date of event | [optional] 

## Example

```python
from sailpoint.beta.models.attributes_changed import AttributesChanged

# TODO update the JSON string below
json = "{}"
# create an instance of AttributesChanged from a JSON string
attributes_changed_instance = AttributesChanged.from_json(json)
# print the JSON string representation of the object
print AttributesChanged.to_json()

# convert the object into a dict
attributes_changed_dict = attributes_changed_instance.to_dict()
# create an instance of AttributesChanged from a dict
attributes_changed_form_dict = attributes_changed.from_dict(attributes_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


