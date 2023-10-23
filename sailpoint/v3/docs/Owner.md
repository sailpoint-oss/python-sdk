# Owner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**email** | **str** | The email of the identity | [optional] 

## Example

```python
from v3.models.owner import Owner

# TODO update the JSON string below
json = "{}"
# create an instance of Owner from a JSON string
owner_instance = Owner.from_json(json)
# print the JSON string representation of the object
print Owner.to_json()

# convert the object into a dict
owner_dict = owner_instance.to_dict()
# create an instance of Owner from a dict
owner_form_dict = owner.from_dict(owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


