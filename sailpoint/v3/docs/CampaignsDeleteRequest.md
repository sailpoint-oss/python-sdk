# CampaignsDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The ids of the campaigns to delete | [optional] 

## Example

```python
from sailpoint.v3.models.campaigns_delete_request import CampaignsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignsDeleteRequest from a JSON string
campaigns_delete_request_instance = CampaignsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(CampaignsDeleteRequest.to_json())

# convert the object into a dict
campaigns_delete_request_dict = campaigns_delete_request_instance.to_dict()
# create an instance of CampaignsDeleteRequest from a dict
campaigns_delete_request_from_dict = CampaignsDeleteRequest.from_dict(campaigns_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


