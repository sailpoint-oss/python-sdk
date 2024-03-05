# AccessItemRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the access item to retrieve the recommendation for. | [optional] 
**type** | **str** | Access item&#39;s type. | [optional] 

## Example

```python
from sailpoint.beta.models.access_item_ref import AccessItemRef

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemRef from a JSON string
access_item_ref_instance = AccessItemRef.from_json(json)
# print the JSON string representation of the object
print AccessItemRef.to_json()

# convert the object into a dict
access_item_ref_dict = access_item_ref_instance.to_dict()
# create an instance of AccessItemRef from a dict
access_item_ref_form_dict = access_item_ref.from_dict(access_item_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


