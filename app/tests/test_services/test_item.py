from app.tests.test_app import BaseTests

from app.business_logic.services import (
    get_item,
    get_all,
    create_item,
    update_item,
    delete_item
)
from app.business_logic.dto import ItemDTO


class ItemTests(BaseTests):
    def setUp(self) -> None:
        super().setUp()
        self.redis.set(
            name='key2',
            value='value2'
        )

    def test_get_item_successfully(self) -> None:
        data = ItemDTO(key='key2')
        result = get_item(data=data)
        self.assertIsInstance(result, dict)
        self.assertEqual(
            result,
            {'key': 'key2', 'value': 'value2'}
        )

    def test_get_item_not_exists(self) -> None:
        data = ItemDTO(key='key3')
        result = get_item(data=data)
        self.assertEqual(result, None)

    def test_get_all_items(self) -> None:
        result = get_all()
        self.assertEqual(
            result,
            [{'key': 'key2', 'value': 'value2'}]
        )

    def test_get_all_items_empty(self) -> None:
        self.redis.flushall()
        result = get_all()
        self.assertEqual(result, [])

    def test_create_item_successfully(self) -> None:
        data = ItemDTO(key='key3', value='value3')
        result = create_item(data=data)
        self.assertIsInstance(result, ItemDTO)
        self.assertEqual(result, data)
        self.assertEqual(
            self.redis.get('key3'),
            b'value3'
        )

    def test_create_item_exist(self) -> None:
        data = ItemDTO(key='key2', value='value2')
        result = create_item(data=data)
        self.assertEqual(result, None)

    def test_update_item_successfully(self) -> None:
        data = ItemDTO(key='key2', value='new_value')
        result = update_item(data=data)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, True)
        self.assertEqual(self.redis.get('key2'), b'new_value')

    def test_update_item_not_exists(self) -> None:
        data = ItemDTO(key='key3', value='new_value')
        result = update_item(data=data)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, False)

    def test_delete_item_successfully(self) -> None:
        data = ItemDTO(key='key2')
        result = delete_item(data=data)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, True)
        self.assertEqual(self.redis.exists('key2'), False)

    def test_delete_item_not_exists(self) -> None:
        data = ItemDTO(key='key3')
        result = delete_item(data=data)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, False)
