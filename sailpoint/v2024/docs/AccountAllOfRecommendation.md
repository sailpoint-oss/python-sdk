# AccountAllOfRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Recommended type of account. | 
**method** | **str** | Method used to produce the recommendation. DISCOVERY - suggested by AI, SOURCE - the account comes from a source flagged as containing machine accounts, CRITERIA - the account satisfies classification criteria. | 

## Example

```python
from sailpoint.v2024.models.account_all_of_recommendation import AccountAllOfRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAllOfRecommendation from a JSON string
account_all_of_recommendation_instance = AccountAllOfRecommendation.from_json(json)
# print the JSON string representation of the object
print(AccountAllOfRecommendation.to_json())

# convert the object into a dict
account_all_of_recommendation_dict = account_all_of_recommendation_instance.to_dict()
# create an instance of AccountAllOfRecommendation from a dict
account_all_of_recommendation_from_dict = AccountAllOfRecommendation.from_dict(account_all_of_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


