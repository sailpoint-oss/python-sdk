# FormOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | FormOwnerType value. IDENTITY FormOwnerTypeIdentity | [optional] 
**id** | **str** | Unique identifier of the form&#39;s owner. | [optional] 
**name** | **str** | Name of the form&#39;s owner. | [optional] 

## Example

```python
from sailpoint.beta.models.form_owner import FormOwner

# TODO update the JSON string below
json = "{}"
# create an instance of FormOwner from a JSON string
form_owner_instance = FormOwner.from_json(json)
# print the JSON string representation of the object
print(FormOwner.to_json())

# convert the object into a dict
form_owner_dict = form_owner_instance.to_dict()
# create an instance of FormOwner from a dict
form_owner_from_dict = FormOwner.from_dict(form_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


