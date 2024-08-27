# RequestedItemStatusRequesterComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment content. | [optional] 
**created** | **datetime** | Date and time comment was created. | [optional] 
**author** | [**CommentDtoAuthor**](CommentDtoAuthor.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.requested_item_status_requester_comment import RequestedItemStatusRequesterComment

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemStatusRequesterComment from a JSON string
requested_item_status_requester_comment_instance = RequestedItemStatusRequesterComment.from_json(json)
# print the JSON string representation of the object
print(RequestedItemStatusRequesterComment.to_json())

# convert the object into a dict
requested_item_status_requester_comment_dict = requested_item_status_requester_comment_instance.to_dict()
# create an instance of RequestedItemStatusRequesterComment from a dict
requested_item_status_requester_comment_from_dict = RequestedItemStatusRequesterComment.from_dict(requested_item_status_requester_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


