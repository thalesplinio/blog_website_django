from typing import Any
import string
from random import SystemRandom
from django.utils.text import slugify


def random_letters(k: int = 5) -> str:
    """
    - Se precisar passe a quantidade de letras que desejar
    - Padrão são 5
    """
    return ''.join(SystemRandom().choices(
        string.ascii_letters + string.digits,
        k=k,
    ))


def slugify_new(text: Any, k: int = 4) -> str:
    """
    - Se precisar passe a quantidade de letras que desejar
    - Padrão são 4
    """
    return slugify(text) + random_letters(k)


if __name__ == '__main__':
    print(random_letters())
    print(slugify('Exemplo De Tag'))
    print(slugify_new('BLA BLA BLA TesTe'))
