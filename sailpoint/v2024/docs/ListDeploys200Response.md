# ListDeploys200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeployResponse]**](DeployResponse.md) | list of deployments | [optional] 

## Example

```python
from sailpoint.v2024.models.list_deploys200_response import ListDeploys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDeploys200Response from a JSON string
list_deploys200_response_instance = ListDeploys200Response.from_json(json)
# print the JSON string representation of the object
print(ListDeploys200Response.to_json())

# convert the object into a dict
list_deploys200_response_dict = list_deploys200_response_instance.to_dict()
# create an instance of ListDeploys200Response from a dict
list_deploys200_response_from_dict = ListDeploys200Response.from_dict(list_deploys200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


