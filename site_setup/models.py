from django.db import models
from utils.model_validators import validate_png
from utils.images import resize_image


# Create your models here.
class MenuLink(models.Model):
    class Meta:
        verbose_name = "Menu Link"
        verbose_name = "Menu Links"

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)

    site_setup = models.ForeignKey(
        'SiteSetup',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):
        return self.text


class SiteSetup(models.Model):
    class Meta:
        verbose_name = "Setup"
        verbose_name_plural = "Setups"

    site_name = models.CharField(max_length=65)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=600)
    name_footer = models.CharField(max_length=65)

    show_first_top_bar = models.BooleanField(
        default=True,
        verbose_name="Mostrar a primeira barrado Azul site.",
    )
    show_search = models.BooleanField(
        default=True,
        verbose_name="Mostrar campo de busca.",
    )
    show_dark_mode = models.BooleanField(
        default=True,
        verbose_name="Mostrar botão de modo escuro/branco.",
    )
    show_header = models.BooleanField(
        default=True,
        verbose_name="Mostrar cabeçalho do site.",
    )
    show_title_subtitle = models.BooleanField(
        default=True,
        verbose_name="Mostrar título e Subtitulo site.",
    )
    show_project_highlight = models.BooleanField(
        default=True,
        verbose_name="Mostrar Projeto em destaque.",
    )
    show_technology = models.BooleanField(
        default=True,
        verbose_name="Mostrar algumas tecnologias.",
    )
    show_some_projects = models.BooleanField(
        default=True,
        verbose_name="Mostrar Alguns projetos.",
        )
    show_menu = models.BooleanField(
        default=True,
        verbose_name="Mostrar menu do site.",
    )
    show_pagination = models.BooleanField(
        default=True,
        verbose_name="Mostrar paginação do site.",
    )
    show_footer = models.BooleanField(
        default=True,
        verbose_name="Mostrar rodapé do site.",
    )
    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m',
        blank=True,
        default='',
        validators=[validate_png],
        verbose_name="Adicionar icone da janela/logotipo",
    )

    def save(self, *args, **kwargs):
        current_favicon_name = str(self.favicon.name)
        super().save(*args, **kwargs)
        favicon_changed = False

        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name

        if favicon_changed:
            resize_image(self.favicon, 32)

    def __str__(self):
        return self.site_name
