# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v2024.models.schedule import Schedule

class TestSchedule(unittest.TestCase):
    """Schedule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Schedule:
        """Test Schedule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Schedule`
        """
        model = Schedule()
        if include_optional:
            return Schedule(
                type = 'WEEKLY',
                months = sailpoint.v2024.models.schedule_months.Schedule_months(
                    type = 'LIST', 
                    values = [1], 
                    interval = 2, ),
                days = sailpoint.v2024.models.schedule_days.Schedule_days(
                    type = 'LIST', 
                    values = [1], 
                    interval = 2, ),
                hours = sailpoint.v2024.models.schedule_hours.Schedule_hours(
                    type = 'LIST', 
                    values = [1], 
                    interval = 2, ),
                expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_zone_id = 'CST'
            )
        else:
            return Schedule(
                type = 'WEEKLY',
                hours = sailpoint.v2024.models.schedule_hours.Schedule_hours(
                    type = 'LIST', 
                    values = [1], 
                    interval = 2, ),
        )
        """

    def testSchedule(self):
        """Test Schedule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()