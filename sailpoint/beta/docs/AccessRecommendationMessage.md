# AccessRecommendationMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interpretation** | **str** | Information about why the access item was recommended. | [optional] 

## Example

```python
from sailpoint.beta.models.access_recommendation_message import AccessRecommendationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRecommendationMessage from a JSON string
access_recommendation_message_instance = AccessRecommendationMessage.from_json(json)
# print the JSON string representation of the object
print AccessRecommendationMessage.to_json()

# convert the object into a dict
access_recommendation_message_dict = access_recommendation_message_instance.to_dict()
# create an instance of AccessRecommendationMessage from a dict
access_recommendation_message_form_dict = access_recommendation_message.from_dict(access_recommendation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


