import json
import unittest
import app
import os


class TestFunc(unittest.TestCase):
    def test(self):
        self.assertEqual(app.add_new_doc('2207 876234'), 'Василий Гупкин')

    def test_add_new_doc(self):
        self.assertEqual(app.add_new_doc('7311', 'pass', 'Shamil', 2), 2)

    def test_delete_doc(self):
        self.assertTrue(app.delete_doc('10006'))
