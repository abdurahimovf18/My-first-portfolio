from django.db import models
from django.db.models.query import Q
from datetime import datetime
from .admin import register_models


class CreatedUpdatedModelNR(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class InfoModel(CreatedUpdatedModelNR):
    image = models.ImageField(upload_to='images/', default="default-entry-image.png")

    started_programming = models.DateField(default=datetime.now)
    instagram_link = models.URLField()
    telegram_link = models.URLField()
    facebook_link = models.URLField()
    github_link = models.URLField()
    contact = models.CharField(max_length=50)

    @property
    def experience(self) -> str:
        return f"{datetime.now().year - self.started_programming.year}+ years"


class SkillCategoryModel(CreatedUpdatedModelNR):
    name = models.CharField(max_length=255)
    icon_class_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Skill Categories'
        verbose_name = 'Skill Category'


class SkillModel(CreatedUpdatedModelNR):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(SkillCategoryModel, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return f"{self.name} - {self.category}"

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'


class ReviewModel(CreatedUpdatedModelNR):
    image = models.ImageField(upload_to='images/', default="default-entry-image.png")
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField()
    content = models.TextField()

    class Meta:
        verbose_name_plural = "Reviews"
        verbose_name = 'Review'
        constraints = [
            models.CheckConstraint(name="My Rating Check Constraint", check=Q(rating__lte=5, rating__gte=1))
        ]


class ContactModel(CreatedUpdatedModelNR):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    message = models.TextField()


    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contact'


register_models(globals_=globals())