from django.db import models


# Create your models here.
class MenuLink(models.Model):
    class Meta:
        verbose_name = "Menu Link"
        verbose_name = "Menu Links"

    text = models.CharField(max_lenght=50)
    url_or_path = models.CharField(max_lenght=2048)
    new_tab = models.BooleanField(default=False)

    def __str__(self):
        return self.text
