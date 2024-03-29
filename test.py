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
        self.path_first_task = self.path + '/1'
        self.path_last_task = self.path + '/3'
        self.path_fake_task = self.path + '/100'
        self.data = {
            'title': 'title', 'description': 'description',
            'deadline': '2024-12-12 23:59:59'
        }
        self.data_to_update = {'title': 'Nuevo titulo'}

    def test_one_equals_one(self):
        self.assertEqual(1, 1)

    def test_get_all_tasks(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)

    def get_task_id(self, response):
        data = json.loads(response.data.decode('utf-8'))
        return data['data']['id']

    def test_get_first_task(self):
        response = self.client.get(path=self.path_first_task, content_type=self.content_type)

        self.assertEqual(response.status_code, 200)

        task_id = self.get_task_id(response)

        self.assertEqual(task_id, 1)

    def test_not_found(self):
        response = self.client.get(path=self.path_fake_task, content_type=self.content_type)

        self.assertEqual(response.status_code, 404)

    def test_create_task(self):
        response = self.client.post(path=self.path, data=json.dumps(self.data),
                                    content_type=self.content_type)

        self.assertEqual(response.status_code, 200)
        task_id = self.get_task_id(response)

        self.assertEqual(task_id, 3)

    def test_update_task(self):
        response = self.client.put(path=self.path_first_task, data=json.dumps(self.data_to_update),
                                   content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode('utf-8'))
        title = data['data']['title']

        self.assertEqual(title, self.data_to_update['title'])

    def test_delete_task(self):
        response = self.client.delete(path=self.path_last_task, content_type=self.content_type)

        self.assertEqual(response.status_code, 200)

        response = self.client.get(path=self.path_last_task, content_type=self.content_type)
        self.assertEqual(response.status_code, 404)

    def test_length_tasks(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(data['data']), 2)


if __name__ == '__main__':
    unittest.main()
