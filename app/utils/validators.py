from app.utils.exceptions import KeyValidationError, ValueValidationError


def key_validator(key):
    if not key or len(key) > 10:
        raise KeyValidationError(
            'The number of characters in the key should not exceed 10 and '
            'should be greater than 0.'
        )

def value_validator(value):
    if not value or len(value) > 20:
        raise ValueValidationError(
            'The number of characters in the value should not exceed 10 and '
            'should be greater than 0.'
        )
