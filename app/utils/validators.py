from app.utils.exceptions import KeyValidationError, ValueValidationError


def key_validator(key: str) -> None:
    """Validate the format of a key.

    Args:
        key (str): The key to validate.

    Raises:
        KeyValidationError: If the key is empty or exceeds 10 characters.
    """
    if not key or len(key) > 10:
        raise KeyValidationError(
            'The number of characters in the key should not exceed 10 and '
            'should be greater than 0.'
        )


def value_validator(value: str) -> None:
    """Validate the format of a value.

    Args:
        value (str): The value to validate.

    Raises:
        ValueValidationError: If the value is empty or exceeds 20 characters.
    """
    if not value or len(value) > 20:
        raise ValueValidationError(
            'The number of characters in the value should not exceed 10 and '
            'should be greater than 0.'
        )
