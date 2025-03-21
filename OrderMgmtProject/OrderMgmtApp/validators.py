from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_firstname(value: object) -> object:
    print("Validate First Name called = " + value)
    if value == 'Rogue':
        raise ValidationError(
            _('%(value)s is not an acceptable First Name'),
            params={'value': value},
        )
def validate_lastname(value):
        print ("Validate Last Name called = " + value)
        if value == 'Smith':
            raise ValidationError(
                _('%(value)s is not an acceptable last Name'),
                params={'value': value},
            )

def validate_cell(value):
        print ("Validate cell called = " + value)
        if value == '111-111-1111':
            raise ValidationError(
                _('%(value)s is not an acceptable Cell number'),
                params={'value': value},
            )
