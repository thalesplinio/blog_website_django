from django.core.exceptions import ValidationError


def validate_png(image):
    """
    VALIDAÇÃO DE CAMPO IMAGEM
    - Validando campo para receber somente formato .png
    """
    if not image.name.lower().endswith('.png'):
        raise ValidationError("A imagen precisa ser no formato .png")
