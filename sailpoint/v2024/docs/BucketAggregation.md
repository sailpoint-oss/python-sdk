# BucketAggregation

The bucket to group the results of the aggregation query by.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the bucket aggregate to be included in the result. | 
**type** | [**BucketType**](BucketType.md) |  | [optional] [default to BucketType.TERMS]
**var_field** | **str** | The field to bucket on. Prefix the field name with &#39;@&#39; to reference a nested object. | 
**size** | **int** | Maximum number of buckets to include. | [optional] 
**min_doc_count** | **int** | Minimum number of documents a bucket should have. | [optional] 

## Example

```python
from sailpoint.v2024.models.bucket_aggregation import BucketAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of BucketAggregation from a JSON string
bucket_aggregation_instance = BucketAggregation.from_json(json)
# print the JSON string representation of the object
print(BucketAggregation.to_json())

# convert the object into a dict
bucket_aggregation_dict = bucket_aggregation_instance.to_dict()
# create an instance of BucketAggregation from a dict
bucket_aggregation_from_dict = BucketAggregation.from_dict(bucket_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


