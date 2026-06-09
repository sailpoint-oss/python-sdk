---
id: intelmachine
title: Intelmachine
pagination_label: Intelmachine
sidebar_label: Intelmachine
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelmachine', 'Intelmachine'] 
slug: /tools/sdk/python/v1/models/intelmachine
tags: ['SDK', 'Software Development Kit', 'Intelmachine', 'Intelmachine']
---

# Intelmachine

MACHINE-specific block; subtype is only on the top-level IntelIdentityResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_application** | **str** | Business application name associated with the non-human identity. | [optional] 
**native_identity** | **str** | Native identifier value on the authoritative source for the machine identity. | [optional] 
**uuid** | **str** | Optional globally unique identifier for the machine identity when assigned. | [optional] 
**source_id** | **str** | Identifier of the correlated source for this machine identity. | [optional] 
**source** | [**Intelmachinesource**](intelmachinesource) | Correlated source summary for the machine identity when available. | [optional] 
**dataset_id** | **str** | Dataset identifier used by machine identity correlation logic. | [optional] 
**exists_on_source** | **bool** | True when a matching account still exists on the connected source. | [optional] [default to False]
**manually_created** | **bool** | True when the machine identity was created through a manual administrative action. | [optional] [default to False]
**manually_edited** | **bool** | True when the machine identity attributes were manually edited after creation. | [optional] [default to False]
**owners** | **object** | Structured owner references for the machine identity when populated by the service. | [optional] 
**user_entitlements** | **[]object** | Entitlements or fine-grained rights linked to the machine identity when available. | [optional] 
}

## Example

```python
from sailpoint.intelligence_package_v1.models.intelmachine import Intelmachine

intelmachine = Intelmachine(
business_application='Payroll Bot',
native_identity='DEMO_AGENT1',
uuid='3fa85f64-5717-4562-b3fc-2c963f66afa6',
source_id='8433902684054f09ae024c06cf5091c1',
source=sailpoint.intelligence_package_v1.models.intelmachinesource.intelmachinesource(
                    id = '2c9180835d2e5168015d32f890301e89', 
                    name = 'Active Directory', 
                    type = 'LDAP', ),
dataset_id='dataset-001',
exists_on_source=True,
manually_created=False,
manually_edited=False,
owners={},
user_entitlements=[
                    {}
                    ]
)

```
[[Back to top]](#) 

