# AccessItemReviewedBy

Identity who reviewed the access item request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of identity who reviewed the access item request. | [optional] 
**id** | **str** | ID of identity who reviewed the access item request. | [optional] 
**name** | **str** | Human-readable display name of identity who reviewed the access item request. | [optional] 

## Example

```python
from sailpoint.beta.models.access_item_reviewed_by import AccessItemReviewedBy

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemReviewedBy from a JSON string
access_item_reviewed_by_instance = AccessItemReviewedBy.from_json(json)
# print the JSON string representation of the object
print(AccessItemReviewedBy.to_json())

# convert the object into a dict
access_item_reviewed_by_dict = access_item_reviewed_by_instance.to_dict()
# create an instance of AccessItemReviewedBy from a dict
access_item_reviewed_by_from_dict = AccessItemReviewedBy.from_dict(access_item_reviewed_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


