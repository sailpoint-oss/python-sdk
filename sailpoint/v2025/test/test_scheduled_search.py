# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.scheduled_search import ScheduledSearch

class TestScheduledSearch(unittest.TestCase):
    """ScheduledSearch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduledSearch:
        """Test ScheduledSearch
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduledSearch`
        """
        model = ScheduledSearch()
        if include_optional:
            return ScheduledSearch(
                name = 'Daily disabled accounts',
                description = 'Daily disabled accounts',
                saved_search_id = '554f1511-f0a1-4744-ab14-599514d3e57c',
                created = '2018-06-25T20:22:28.104Z',
                modified = '2018-06-25T20:22:28.104Z',
                schedule = sailpoint.v2025.models.schedule_2.Schedule_2(
                    type = 'WEEKLY', 
                    months = null, 
                    days = null, 
                    hours = null, 
                    expiration = '2018-06-25T20:22:28.104Z', 
                    time_zone_id = 'America/Chicago', ),
                recipients = [
                    sailpoint.v2025.models.search_schedule_recipients_inner.SearchSchedule_recipients_inner(
                        type = 'IDENTITY', 
                        id = '2c9180867624cbd7017642d8c8c81f67', )
                    ],
                enabled = False,
                email_empty_results = False,
                display_query_details = False,
                id = '0de46054-fe90-434a-b84e-c6b3359d0c64',
                owner = sailpoint.v2025.models.scheduled_search_all_of_owner.ScheduledSearch_allOf_owner(
                    type = 'IDENTITY', 
                    id = '2c9180867624cbd7017642d8c8c81f67', ),
                owner_id = '2c9180867624cbd7017642d8c8c81f67'
            )
        else:
            return ScheduledSearch(
                saved_search_id = '554f1511-f0a1-4744-ab14-599514d3e57c',
                schedule = sailpoint.v2025.models.schedule_2.Schedule_2(
                    type = 'WEEKLY', 
                    months = null, 
                    days = null, 
                    hours = null, 
                    expiration = '2018-06-25T20:22:28.104Z', 
                    time_zone_id = 'America/Chicago', ),
                recipients = [
                    sailpoint.v2025.models.search_schedule_recipients_inner.SearchSchedule_recipients_inner(
                        type = 'IDENTITY', 
                        id = '2c9180867624cbd7017642d8c8c81f67', )
                    ],
                id = '0de46054-fe90-434a-b84e-c6b3359d0c64',
                owner = sailpoint.v2025.models.scheduled_search_all_of_owner.ScheduledSearch_allOf_owner(
                    type = 'IDENTITY', 
                    id = '2c9180867624cbd7017642d8c8c81f67', ),
                owner_id = '2c9180867624cbd7017642d8c8c81f67',
        )
        """

    def testScheduledSearch(self):
        """Test ScheduledSearch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
