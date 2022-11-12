import re


def name_validator(name: str) -> bool:
    """
    Validate if name contains only letters
    :param name:
    :return:
    """
    return name.replace(" ", '').isalpha()


def cellphone_validator(cellphone: str) -> bool:
    """
    Validate if cellphone contains only numbers and at least 10 digits
    :param cellphone:
    :return:
    """
    cellphone_regex = r'\b[0-9]{10,14}'
    return re.match(cellphone_regex, cellphone) is not None


def email_validator(email: str) -> bool:
    """
    Validate email
    :param email:
    :return:
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(email_regex, email) is not None


def color_validator(color: str) -> bool:
    return color in ['gray', 'yellow', 'blue']


def model_validator(model: str) -> bool:
    return model in ['hatch', 'sedan', 'convertible']
