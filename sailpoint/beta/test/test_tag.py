# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.models.tag import Tag

class TestTag(unittest.TestCase):
    """Tag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Tag:
        """Test Tag
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Tag`
        """
        model = Tag()
        if include_optional:
            return Tag(
                id = '449ecdc0-d4ff-4341-acf6-92f6f7ce604f',
                name = 'PCI',
                created = '2022-05-04T14:48:49Z',
                modified = '2022-07-14T16:31:11Z',
                tag_category_refs = [
                    sailpoint.beta.models.tag_tag_category_refs_inner.Tag_tagCategoryRefs_inner(
                        type = 'ENTITLEMENT', 
                        id = '2c91809773dee32014e13e122092014e', 
                        name = 'CN=entitlement.490efde5,OU=OrgCo,OU=ServiceDept,DC=HQAD,DC=local', )
                    ]
            )
        else:
            return Tag(
                id = '449ecdc0-d4ff-4341-acf6-92f6f7ce604f',
                name = 'PCI',
                created = '2022-05-04T14:48:49Z',
                modified = '2022-07-14T16:31:11Z',
                tag_category_refs = [
                    sailpoint.beta.models.tag_tag_category_refs_inner.Tag_tagCategoryRefs_inner(
                        type = 'ENTITLEMENT', 
                        id = '2c91809773dee32014e13e122092014e', 
                        name = 'CN=entitlement.490efde5,OU=OrgCo,OU=ServiceDept,DC=HQAD,DC=local', )
                    ],
        )
        """

    def testTag(self):
        """Test Tag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()