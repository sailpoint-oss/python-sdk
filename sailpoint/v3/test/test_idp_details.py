# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.idp_details import IdpDetails

class TestIdpDetails(unittest.TestCase):
    """IdpDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdpDetails:
        """Test IdpDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdpDetails`
        """
        model = IdpDetails()
        if include_optional:
            return IdpDetails(
                role = 'SAML_IDP',
                entity_id = 'http://www.okta.com/exkdaruy8Ln5Ry7C54x6',
                binding = 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST',
                auth_context = 'urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport',
                logout_url = 'https://dev-206445.oktapreview.com/login/signout',
                include_auth_context = False,
                name_id = 'urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress',
                jit_configuration = sailpoint.v3.models.jit_configuration.JITConfiguration(
                    enabled = False, 
                    source_id = '2c9180857377ed2901739c12a2da5ac8', 
                    source_attribute_mappings = {firstName=okta.firstName, lastName=okta.lastName, email=okta.email}, ),
                cert = '-----BEGIN CERTIFICATE-----****-----END CERTIFICATE-----',
                login_url_post = 'https://dev-157216.okta.com/app/sailpointdev157216_cdovsaml_1/exkdaruy8Ln5Ry7C54x6/sso/saml',
                login_url_redirect = 'https://dev-157216.okta.com/app/sailpointdev157216_cdovsaml_1/exkdaruy8Ln5Ry7C54x6/sso/saml',
                mapping_attribute = 'email',
                certificate_expiration_date = 'Fri Mar 08 08:54:24 UTC 2013',
                certificate_name = 'OU=Conext, O=Surfnet, L=Utrecht, ST=Utrecht, C=NL'
            )
        else:
            return IdpDetails(
        )
        """

    def testIdpDetails(self):
        """Test IdpDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()