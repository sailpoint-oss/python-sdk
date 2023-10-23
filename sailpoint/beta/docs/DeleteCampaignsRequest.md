# DeleteCampaignsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The ids of the campaigns to delete | [optional] 

## Example

```python
from beta.models.delete_campaigns_request import DeleteCampaignsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCampaignsRequest from a JSON string
delete_campaigns_request_instance = DeleteCampaignsRequest.from_json(json)
# print the JSON string representation of the object
print DeleteCampaignsRequest.to_json()

# convert the object into a dict
delete_campaigns_request_dict = delete_campaigns_request_instance.to_dict()
# create an instance of DeleteCampaignsRequest from a dict
delete_campaigns_request_form_dict = delete_campaigns_request.from_dict(delete_campaigns_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


