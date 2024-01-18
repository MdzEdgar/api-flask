import json
import unittest

from app import db
from app import create_app
from config import config


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestAPI, cls).setUpClass()
        environment = config['test']
        cls.app = create_app(environment)

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()

    def setUp(self):
        self.app = TestAPI.app
        self.client = self.app.test_client()

        self.content_type = 'application/json'
        self.path = 'http://127.0.0.1:5000/api/v1/tasks'

    def test_one_equals_one(self):
        self.assertEqual(1, 1)

    def test_get_all_tasks(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)

    def test_get_first_task(self):
        new_path = self.path + '/1'

        response = self.client.get(path=new_path, content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode('utf-8'))
        task_id = data['data']['id']

        self.assertEqual(task_id, 1)

    def test_not_found(self):
        new_path = self.path + '100'
        response = self.client.get(path=new_path, content_type=self.content_type)

        self.assertEqual(response.status_code, 404)

    def test_create_task(self):
        data = {
            'title': 'title', 'description': 'description',
            'deadline': '2024-12-12 23:59:59'
        }

        response = self.client.post(path=self.path, data=json.dumps(data),
                                    content_type=self.content_type)

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        task_id = data['data']['id']

        self.assertEqual(task_id, 3)

    def test_length_tasks(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(data['data']), 3)


if __name__ == '__main__':
    unittest.main()
