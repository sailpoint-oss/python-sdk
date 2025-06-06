# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.schedule2 import Schedule2

class TestSchedule2(unittest.TestCase):
    """Schedule2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Schedule2:
        """Test Schedule2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Schedule2`
        """
        model = Schedule2()
        if include_optional:
            return Schedule2(
                type = 'WEEKLY',
                months = None,
                days = None,
                hours = None,
                expiration = '2018-06-25T20:22:28.104Z',
                time_zone_id = 'America/Chicago'
            )
        else:
            return Schedule2(
                type = 'WEEKLY',
                hours = None,
        )
        """

    def testSchedule2(self):
        """Test Schedule2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
