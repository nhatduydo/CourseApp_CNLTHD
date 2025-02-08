from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    description = RichTextField()
    image = models.ImageField(upload_to="courses/%Y/%m")
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ("subject", "category")


class Lesson(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    content = RichTextField()
    image = models.ImageField(upload_to="lessons/%Y/%m")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")

    class meta:
        unique_together = ("subject", "course")


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    # nếu không overwrite to string => tag sẽ hiện thị: tag object(1)
    # khi overwrite lên => ghi đè tên lên => hiển thị tên do user/admin đặt
    def __str__(self):
        return self.name
