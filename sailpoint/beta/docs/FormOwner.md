# FormOwner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is a unique identifier | [optional] 
**type** | **str** | Type is a FormOwnerType value IDENTITY FormOwnerTypeIdentity | [optional] 

## Example

```python
from beta.models.form_owner import FormOwner

# TODO update the JSON string below
json = "{}"
# create an instance of FormOwner from a JSON string
form_owner_instance = FormOwner.from_json(json)
# print the JSON string representation of the object
print FormOwner.to_json()

# convert the object into a dict
form_owner_dict = form_owner_instance.to_dict()
# create an instance of FormOwner from a dict
form_owner_form_dict = form_owner.from_dict(form_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


