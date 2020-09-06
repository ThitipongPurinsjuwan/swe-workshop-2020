import re


def validate_name(name):
    special = re.compile('[@_!#$%^&*()<>?/\|}{~:\s\d]')
    if(special.search(name) != None) or name == "":  # len(name) == 0
        return False
    else:
        return True


def validate_id(id):
    if id.isalnum() and len(id) == 13:
        return True
    else:
        return False


def validate_phone_number(phone_number):
    if len(phone_number) != 10:
        return False
    if not phone_number.isalnum():
        return False
    else:
        return True
