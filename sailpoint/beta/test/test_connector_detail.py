# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.models.connector_detail import ConnectorDetail

class TestConnectorDetail(unittest.TestCase):
    """ConnectorDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectorDetail:
        """Test ConnectorDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectorDetail`
        """
        model = ConnectorDetail()
        if include_optional:
            return ConnectorDetail(
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
            return ConnectorDetail(
        )
        """

    def testConnectorDetail(self):
        """Test ConnectorDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
