from django.contrib import admin
from .models import Category
from .models import Course
from .models import Lesson
from .models import Tag
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CategoryAdmin(admin.ModelAdmin):
      list_display = ['pk', 'name']
      search_fields = ['name']
      list_filter = ['id', 'name']


class CourseForm(forms.ModelForm):
      description = forms.CharField(widget=CKEditorUploadingWidget)
      
      class Meta:
            model = Course
            fields = '__all__'


class TagInlineAdmin(admin.StackedInline):
      model = Course.tags.through
      


class CourseAdmin(admin.ModelAdmin):
      list_display = ['pk', 'subject', 'created_date', 'updated_date', 'category', 'active']
      readonly_fields = ['img']
      inlines = [TagInlineAdmin]
      form = CourseForm
      
      def img(self, course):
            if course:
                  return mark_safe(
                        '<img src="/static/{url}" width="120" />' \
                              .format(url= course.image.name)
                  )
                  
      class Media:
            css = {
                  'all': ('/static/css/style.css', )
            }
            js = ('/static/js/script.js',)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Tag)