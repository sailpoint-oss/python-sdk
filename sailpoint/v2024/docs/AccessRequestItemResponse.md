# AccessRequestItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | the access request item operation | [optional] 
**access_item_type** | **str** | the access item type | [optional] 
**name** | **str** | the name of access request item | [optional] 
**decision** | **str** | the final decision for the access request | [optional] 
**description** | **str** | the description of access request item | [optional] 
**source_id** | **str** | the source id | [optional] 
**source_name** | **str** | the source Name | [optional] 
**approval_infos** | [**List[ApprovalInfoResponse]**](ApprovalInfoResponse.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.access_request_item_response import AccessRequestItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestItemResponse from a JSON string
access_request_item_response_instance = AccessRequestItemResponse.from_json(json)
# print the JSON string representation of the object
print AccessRequestItemResponse.to_json()

# convert the object into a dict
access_request_item_response_dict = access_request_item_response_instance.to_dict()
# create an instance of AccessRequestItemResponse from a dict
access_request_item_response_form_dict = access_request_item_response.from_dict(access_request_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


