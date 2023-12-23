from django.db import models
from utils.rands import slugify_new
from django.contrib.auth.models import User
from utils.images import resize_image
from django_summernote.models import AbstractAttachment
from django.urls import reverse


class PostAttachment(AbstractAttachment):
    class Meta:
        verbose_name = 'Imagem do site'
        verbose_name = 'Imagens do site'

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name

        current_file_name = str(self.file.name)
        super_save = super().save(*args, **kwargs)
        file_changed = False

        if self.file:
            file_changed = current_file_name != self.file.name

        if file_changed:
            resize_image(self.file, 900, True, 70)

        return super_save


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


class PostManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True).order_by('-pk')


class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    objects = PostManager()

    title = models.CharField(max_length=150)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )
    excerpt = models.CharField(max_length=300)
    is_published = models.BooleanField(
        default=False,
        verbose_name="Publicar?",
        help_text=(
            "Este campo precisará estar marcado para que a"
            "pagina seja exibida publicamente."
            ),
        )
    content = models.TextField(
        verbose_name="Digite aqui seu conteúdo",
    )
    cover = models.ImageField(
        upload_to='posts/%Y/%m/',
        blank=True,
        default='',
    )
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text="Exibe a imagem de capa também dentro do conteúdo do post?",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    # user.post_created_by.all
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='post_created_by'
    )
    updated_at = models.DateTimeField(auto_now=True)
    # user.post_updated_by.all
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='post_updated_by'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        default='',
    )

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        return reverse('blog:post', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)

        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 70)

        return super_save

    def __str__(self):
        return self.title


class Technology(models.Model):
    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'

    name = models.CharField(max_length=20)
    image = models.ImageField(
        upload_to='assets/tecnology_image/%Y/%m',
        blank=True,
        default='',
        verbose_name="Adicionar imagem para a tecnologia",
        )

    def save(self, *args, **kwargs):
        current_image_name = str(self.image.name)
        super().save(*args, **kwargs)
        image_changed = False

        if self.image:
            image_changed = current_image_name != self.image.name

        if image_changed:
            resize_image(self.image, 60)

    def __str__(self):
        return self.name
