import unittest
import os

from unittest import TestCase
from unittest.mock import patch

from utills import file_management, add, search, Cache, modify, delete


class Test(TestCase):
    def test_step_1_create_db(self):
        os.remove('db.json')
        Cache.all_books = []
        self.assertEqual([], file_management('r'))

    @patch('builtins.input', side_effect=['First_title', 'First_author', '1999'])
    def test_step_2_add(self, mock_input):
        result = add()
        self.assertEqual(
            result.__dict__,
            {
                'id': 1,
                'title': 'First_title',
                'author': 'First_author',
                'year': 1999,
                'status': 'в наличии'
            }
        )

    @patch('builtins.input', side_effect=['Second_title', 'Second_author', '-1'])
    def test_step_3_add_error_year(self, mock_input):
        result = add()
        self.assertEqual(result, None)

    @patch('builtins.input', side_effect=['1', 'First_title'])
    def test_step_4_search(self, mock_input):
        result = search()
        self.assertEqual(
            result[0].__dict__,
            {
                'id': 1,
                'title': 'First_title',
                'author': 'First_author',
                'year': 1999,
                'status': 'в наличии'

            }
        )

    @patch('builtins.input', side_effect=['1', '2'])
    def test_step_5_modify(self, mock_input):
        result = modify()
        self.assertEqual(result.status, 'выдана')

    @patch('builtins.input', side_effect=['1', '2'])
    def test_step_6_delete(self, mock_input):
        result = delete()
        self.assertEqual(
            result.__dict__,
            {
                'id': 1,
                'title': 'First_title',
                'author': 'First_author',
                'year': 1999,
                'status': 'выдана'

            }
        )


if __name__ == "main":
    unittest.main()
