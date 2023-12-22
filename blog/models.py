from django.db import models
from utils.rands import slugify_new


class Tag(models.Model):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 5)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 5)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Page(models.Model):
    class Meta:
        verbose_name = "Sobre min"
        verbose_name_plural = "Sobre min"

    full_name = models.CharField(
        max_length=65,
        verbose_name="Nome completo",
    )
    profission = models.CharField(
        max_length=130,
        verbose_name="Curso de formação",
    )
    function_name = models.CharField(
        max_length=130,
        verbose_name="Área de atuação",
    )

    email = models.EmailField(
        max_length=60,
        verbose_name="E-Mail",
    )
    phone = models.CharField(
        max_length=30,
        verbose_name="Telefone/Whatsapp",
    )
    locale = models.CharField(
        max_length=60,
        verbose_name="Localidade que reside",
    )
    content = models.TextField(
        verbose_name="Digite aqui seu conteúdo",
    )

    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
        verbose_name="URL",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Publicar?",
        help_text=(
            "Este campo precisará estar marcado para que a"
            "pagina seja exibida publicamente."
            )
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 5)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
