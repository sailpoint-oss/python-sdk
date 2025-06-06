# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.api.tagged_objects_api import TaggedObjectsApi


class TestTaggedObjectsApi(unittest.TestCase):
    """TaggedObjectsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TaggedObjectsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_tagged_object(self) -> None:
        """Test case for delete_tagged_object

        Delete object tags
        """
        pass

    def test_delete_tags_to_many_object(self) -> None:
        """Test case for delete_tags_to_many_object

        Remove tags from multiple objects
        """
        pass

    def test_get_tagged_object(self) -> None:
        """Test case for get_tagged_object

        Get tagged object
        """
        pass

    def test_list_tagged_objects(self) -> None:
        """Test case for list_tagged_objects

        List tagged objects
        """
        pass

    def test_list_tagged_objects_by_type(self) -> None:
        """Test case for list_tagged_objects_by_type

        List tagged objects by type
        """
        pass

    def test_put_tagged_object(self) -> None:
        """Test case for put_tagged_object

        Update tagged object
        """
        pass

    def test_set_tag_to_object(self) -> None:
        """Test case for set_tag_to_object

        Add tag to object
        """
        pass

    def test_set_tags_to_many_objects(self) -> None:
        """Test case for set_tags_to_many_objects

        Tag multiple objects
        """
        pass


if __name__ == '__main__':
    unittest.main()
