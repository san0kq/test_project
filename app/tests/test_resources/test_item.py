from app.tests.test_app import BaseTests


class ItemTests(BaseTests):
    def setUp(self) -> None:
        super().setUp()
        self.redis.set(
            name='key2',
            value='value2'
        )

    def test_get_all(self) -> None:
        response = self.client.get('/api/v1/item/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            b'[{"key":"key2","value":"value2"}]\n'
        )

    def test_get_all_empty(self) -> None:
        self.redis.flushall()
        response = self.client.get('/api/v1/item/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'[]\n')

    def test_get_item_by_name_successfully(self) -> None:
        response = self.client.get('/api/v1/item/key2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            b'{"key":"key2","value":"value2"}\n'
        )

    def test_get_item_by_name_not_found(self) -> None:
        response = self.client.get('/api/v1/item/key10/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, b'')

    def test_get_item_by_name_invalid_key(self) -> None:
        response = self.client.get('/api/v1/item/12345678910/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'')

    def test_create_item_successfully(self) -> None:
        data = {
            'key': 'key3',
            'value': 'value3'
        }
        response = self.client.post(
            '/api/v1/item/',
            json=data
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data,
            b'{"key":"key3","value":"value3"}\n'
        )

    def test_create_item_invalid_key(self) -> None:
        data = {
            'key': '123456789000',
            'value': 'value3'
        }
        response = self.client.post(
            '/api/v1/item/',
            json=data
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'')

    def test_create_item_exists(self) -> None:
        data = {
            'key': 'key2',
            'value': 'value3'
        }
        response = self.client.post(
            '/api/v1/item/',
            json=data
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data, b'')

    def test_update_item_successfully(self) -> None:
        data = {
            'key': 'key2',
            'value': 'new_value'
        }
        response = self.client.put(
            '/api/v1/item/',
            json=data
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, b'')

    def test_update_item_invalid_key(self) -> None:
        data = {
            'key': 'key020000000222',
            'value': 'new_value'
        }
        response = self.client.put(
            '/api/v1/item/',
            json=data
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'')

    def test_update_item_not_found(self) -> None:
        data = {
            'key': 'key5',
            'value': 'new_value'
        }
        response = self.client.put(
            '/api/v1/item/',
            json=data
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, b'')

    def test_delete_item_successfully(self) -> None:
        response = self.client.delete('/api/v1/item/key2/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, b'')

    def test_delete_item_invalid_key(self) -> None:
        response = self.client.delete('/api/v1/item/key223623712651/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'')

    def test_delete_item_not_found(self) -> None:
        response = self.client.delete('/api/v1/item/key5/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, b'')
