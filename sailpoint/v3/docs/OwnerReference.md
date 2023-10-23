# OwnerReference

The owner of this object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Owner type. This field must be either left null or set to &#39;IDENTITY&#39; on input, otherwise a 400 Bad Request error will result. | [optional] 
**id** | **str** | Identity id | [optional] 
**name** | **str** | Human-readable display name of the owner. It may be left null or omitted in a POST or PATCH. If set, it must match the current value of the owner&#39;s display name, otherwise a 400 Bad Request error will result. | [optional] 

## Example

```python
from v3.models.owner_reference import OwnerReference

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerReference from a JSON string
owner_reference_instance = OwnerReference.from_json(json)
# print the JSON string representation of the object
print OwnerReference.to_json()

# convert the object into a dict
owner_reference_dict = owner_reference_instance.to_dict()
# create an instance of OwnerReference from a dict
owner_reference_form_dict = owner_reference.from_dict(owner_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


