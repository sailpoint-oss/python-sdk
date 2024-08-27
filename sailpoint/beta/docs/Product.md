# Product


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_name** | **str** | Name of the Product | [optional] 
**url** | **str** | URL of the Product | [optional] 
**product_tenant_id** | **str** | An identifier for a specific product-tenant combination | [optional] 
**product_region** | **str** | Product region | [optional] 
**product_right** | **str** | Right needed for the Product | [optional] 
**api_url** | **str** | API URL of the Product | [optional] 
**licenses** | [**List[License]**](License.md) |  | [optional] 
**attributes** | **Dict[str, object]** | Additional attributes for a product | [optional] 
**zone** | **str** | Zone | [optional] 
**status** | **str** | Status of the product | [optional] 
**status_date_time** | **datetime** | Status datetime | [optional] 
**reason** | **str** | If there&#39;s a tenant provisioning failure then reason will have the description of error | [optional] 
**notes** | **str** | Product could have additional notes added during tenant provisioning. | [optional] 
**date_created** | **datetime** | Date when the product was created | [optional] 
**last_updated** | **datetime** | Date when the product was last updated | [optional] 
**org_type** | **str** | Type of org | [optional] 

## Example

```python
from sailpoint.beta.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print(Product.to_json())

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_from_dict = Product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


