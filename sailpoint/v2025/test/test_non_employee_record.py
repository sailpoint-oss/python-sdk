# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.non_employee_record import NonEmployeeRecord

class TestNonEmployeeRecord(unittest.TestCase):
    """NonEmployeeRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NonEmployeeRecord:
        """Test NonEmployeeRecord
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NonEmployeeRecord`
        """
        model = NonEmployeeRecord()
        if include_optional:
            return NonEmployeeRecord(
                id = 'ef38f94347e94562b5bb8424a56397d8',
                account_name = 'Abby.Smith',
                first_name = 'William',
                last_name = 'Smith',
                email = 'william.smith@example.com',
                phone = '5125555555',
                manager = 'jane.doe',
                source_id = '2c91808568c529c60168cca6f90c1313',
                data = {description=Auditing},
                start_date = '2019-08-23T18:52:59.162Z',
                end_date = '2020-08-23T18:52:59.162Z',
                modified = '2019-08-23T18:52:59.162Z',
                created = '2019-08-23T18:40:35.772Z'
            )
        else:
            return NonEmployeeRecord(
        )
        """

    def testNonEmployeeRecord(self):
        """Test NonEmployeeRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
