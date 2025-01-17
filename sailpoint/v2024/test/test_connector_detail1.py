# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.models.connector_detail1 import ConnectorDetail1

class TestConnectorDetail1(unittest.TestCase):
    """ConnectorDetail1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectorDetail1:
        """Test ConnectorDetail1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectorDetail1`
        """
        model = ConnectorDetail1()
        if include_optional:
            return ConnectorDetail1(
                name = 'JDBC',
                source_config_xml = '<Form connectorName='Active Directory - Direct' directConnect='true' name='Active Directory' status='released' type='SourceConfig' xmlns='http://www.sailpoint.com/xsd/sailpoint_form_1_0.xsd'>
	<Field defaultValue='true' hidden='true' name='cloudAuthEnabled' type='boolean' value='true'> </Field> </Form>',
                source_config = '{Form={Field={_defaultValue=true, _hidden=true, _name=cloudAuthEnabled, _type=boolean, _value=true}, _xmlns=http://www.sailpoint.com/xsd/sailpoint_form_1_0.xsd, _connectorName=Active Directory - Direct, _directConnect=true, _name=Active Directory, _status=released, _type=SourceConfig, __text=\n\t}}',
                direct_connect = True,
                file_upload = False,
                uploaded_files = '[]',
                connector_metadata = {supportedUI=EXTJS}
            )
        else:
            return ConnectorDetail1(
        )
        """

    def testConnectorDetail1(self):
        """Test ConnectorDetail1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
