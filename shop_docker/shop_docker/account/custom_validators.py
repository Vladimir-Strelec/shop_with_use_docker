from django.core.exceptions import ValidationError


def check_only_characters_in_name(value):
    if value[0].isdigit():
        raise ValidationError('Name cannot start with numbers')
