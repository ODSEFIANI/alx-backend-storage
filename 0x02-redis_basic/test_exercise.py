#!/usr/bin/env python3
import unittest

from exercise import Cache  # Adjust the import based on your actual module structure

class TestCache(unittest.TestCase):

    def setUp(self):
        # Set up your cache or caching mechanism
        self.cache = Cache()

    def test_store_and_get_without_callable(self):
        key = "foo"
        data_to_store = b"binary_data"
        
        # Store binary data
        stored_key = self.cache.store(data_to_store)

        # Retrieve data without callable
        retrieved_data = self.cache.get(stored_key)

        # Assert that retrieved data matches the stored data
        self.assertEqual(retrieved_data, data_to_store)

        # Additional assertion for the expected output
        self.assertEqual(str(retrieved_data == data_to_store), 'True')
        self.assertEqual(str(type(retrieved_data == data_to_store).__name__), 'bool')

    def test_get_with_callable_raises_value_error(self):
        key = "foo"
        data_to_store = b"binary_data"
        
        # Store binary data
        stored_key = self.cache.store(data_to_store)

        # Attempt to retrieve data with a callable that raises a ValueError
        with self.assertRaises(ValueError) as context:
            retrieved_data = self.cache.get(stored_key, fn=int)

        # Additional assertion for the expected output
        self.assertEqual(str(type(context.exception).__name__), 'ValueError')

if __name__ == "__main__":
    cache = Cache()

