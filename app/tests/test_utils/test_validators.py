from app.tests.test_app import BaseTests

from app.utils.validators import key_validator, value_validator
from app.utils.exceptions import KeyValidationError, ValueValidationError


class ValidatorTests(BaseTests):
    def test_key_validator_successfully(self) -> None:
        key = 'key2'
        self.assertEqual(key_validator(key=key), None)

    def test_key_validator_failed(self) -> None:
        key = 'key21361626123'
        with self.assertRaises(KeyValidationError):
            key_validator(key=key)

    def test_value_validator_successfully(self) -> None:
        value = 'value2'
        self.assertEqual(value_validator(value=value), None)

    def test_value_validator_failed(self) -> None:
        value = 'value21361626123232312'
        with self.assertRaises(ValueValidationError):
            value_validator(value=value)
