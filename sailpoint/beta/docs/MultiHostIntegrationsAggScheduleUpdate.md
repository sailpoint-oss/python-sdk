# MultiHostIntegrationsAggScheduleUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multihost_id** | **str** | Multi-Host Integration ID. The ID must be unique | 
**aggregation_grp_id** | **str** | Multi-Host Integration aggregation group ID | 
**aggregation_grp_name** | **str** | Multi-Host Integration name | 
**aggregation_cron_schedule** | **str** | Cron expression to schedule aggregation | 
**enable_schedule** | **bool** | Boolean value for Multi-Host Integration aggregation schedule.  This specifies if scheduled aggregation is enabled or disabled. | [default to False]
**source_id_list** | **List[str]** | Source IDs of the Multi-Host Integration | 
**created** | **datetime** | Created date of Multi-Host Integration aggregation schedule | [optional] 
**modified** | **datetime** | Modified date of Multi-Host Integration aggregation schedule | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_integrations_agg_schedule_update import MultiHostIntegrationsAggScheduleUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostIntegrationsAggScheduleUpdate from a JSON string
multi_host_integrations_agg_schedule_update_instance = MultiHostIntegrationsAggScheduleUpdate.from_json(json)
# print the JSON string representation of the object
print(MultiHostIntegrationsAggScheduleUpdate.to_json())

# convert the object into a dict
multi_host_integrations_agg_schedule_update_dict = multi_host_integrations_agg_schedule_update_instance.to_dict()
# create an instance of MultiHostIntegrationsAggScheduleUpdate from a dict
multi_host_integrations_agg_schedule_update_from_dict = MultiHostIntegrationsAggScheduleUpdate.from_dict(multi_host_integrations_agg_schedule_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


