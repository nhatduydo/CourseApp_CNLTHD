# CourseApp_CNLTHD
## Công nghệ lập trình hiện đại
# Mục lục
[tải các gói thư viện trong requirements](#tải-các-gói-thư-viện-trong-requirements)  
[xuất ra requirements](#xuất-ra-requirements)  
[Quy tắc Import trong Python](#quy-tắc-import-trong-python)  
[tự động sắp xếp import theo thứ tự chuẩn PEP8](#tự-động-sắp-xếp-import-theo-thứ-tự-chuẩn-pep8)  
[hướng dẫn chứng thực](#hướng-dẫn-chứng-thực)  

1. [cài đặt django](#cài-đặt-django)
2. [kết nối cơ sở dữ liệu mySQL](#kết-nối-cơ-sở-dữ-liệu-mySQL)
3. [tạo app](#tạo-app)
4. [kết nối CSDL](#kết-nối-CSDL)
5. [import trong setting.py](#import-trong-setting.py)
   - [tạo model truy vấn thử](#tạo-model-truy-vấn-thử)
   - [thực hiện để xem mysql](#thực-hiện-để-xem-mysql)
   - [kiểm tra 1 vài lệnh để kiểm tra model](#kiểm-tra-1-vài-lệnh)
   - [kiểm tra trên django](#kiểm-tra-trên-django)
6. [tạo supper user](#tạo-supper-user)
7. [import trong admin](#import-trong-admin)
8. [custom theo ý người dùng](#custom-theo-ý-người-dùng)
9. [tạo class Course trong models](#tạo-class-Course-trong-models)
    - [phân biệt auto now và auto now add](#phân-biệt-auto-now-và-auto-now-add)
    - [sử dụng on delete trong khóa ngoại](#sử-dụng-on-delete-trong-khóa-ngoại)
10. [tạo kế thừa những cái dùng chung thành những class riêng](#tạo-kế-thừa-những-cái-dùng-chung-thành-những-class-riêng)
11. [tạo-migrations](#tạo-migrations)
12. [quản-trị-trong-admin](#quản-trị-trong-admin)
13. [tạo model class lesson](#tạo-model-class-lesson)
14. [ràng buộc meta](#ràng-buộc-meta)
15. [gắn tag làm many to many](#gắn-tag-làm-many-to-many)
16. [tác động database để tạo model](#tác-động-database-để-tạo-model)
17. [import trong admin](#import-trong-admin)
18. [chỉnh sửa admin hiển thị ảnh đã upload](#chỉnh-sửa-admin-hiển-thị-ảnh-đã-upload)
      - [tạo lớp ghi đè hiển thị img](#tạo-lớp-ghi-đè-hiển-thị-img)
      - [thêm css và js vào trang ModelAdmin](#thêm-css-và-js-vào-trang-modeladmin)
19. [tích hợp CKEditor vào admin](#tích-hợp-ckeditor-vào-admin)
20. [chỉnh sửa content của model Lesson](#chỉnh-sửa-content-của-model-lesson)
21. [xử lý upload hình](#xử-lý-upload-hình)
22. [InlineModelAdmin chỉnh sửa nhiều model many to many](#inlinemodeladmin-chỉnh-sửa-nhiều-model-many-to-many)
23. [django debug toolbar](#django-debug-toolbar)
    - [cấu hình trong setting để debug_toolbar chạy local](#cấu-hình-trong-setting-để-debug_toolbar-chạy-local)
24. [tạo dao và viết hàm truy vấn](#tạo-dao-và-viết-hàm-truy-vấn)
    - [truy vấn gom nhóm dữ liệu hoặc truy vấn thống kê](#truy-vấn-gom-nhóm-dữ-liệu-hoặc-truy-vấn-thống-kê)
    - [order_by](#order_by)
25. [adminsite - tùy chỉnh trang web](#adminsite---tùy-chỉnh-trang-web)
    - [thêm view mới vào admin site](#thêm-view-mới-vào-admin-site)
    - [đổ dữ liệu ra](#đổ-dữ-liệu-ra)
    - [vẽ biểu đồ charjs](#vẽ-biểu-đồ-charjs)
    - [khắc phục lỗi khi thêm {% %} trong vscode](#khắc-phục-lỗi-khi-thêm-{%-%}-trong-vscode)
26. [Xây dựng API theo yêu cầu](#xây-dựng-api-theo-yêu-cầu)
27. [tích hợp swagger](#tích-hợp-swagger)
    - [khái niệm swagger](#khái-niệm-swagger)
    - [api categories](#api-categories)
    - [api course khóa học](#api-course-khóa-học)
28. [phân trang](#phân-trang)
    - [custom lại đường dẫn hình ảnh](#custom-lại-đường-dẫn-hình-ảnh)
    - [hiển thị thông tin tên của tag](#hiển-thị-thông-tin-tên-của-tag)
    - [thêm phần lọc dữ liệu](#thêm-phần-lọc-dữ-liệu)
      + [lấy danh sách tất cả khóa học](#lấy-danh-sách-tất-cả-khóa-học)
      + [lấy danh sách các bài học của một khóa học](#lấy-danh-sách-các-bài-học-của-một-khóa-học)
      + [thử debug](#thử-debug)
29. [API chi tiết bài học](#api-chi-tiết-bài-học)
30. [đăng ký user](#đăng-ký-user)
    - [chạy postman kiểm tra](#chạy-postman-kiểm-tra)
31. [upload hình ảnh lên couldinary](#upload-hình-ảnh-lên-couldinary)
32. [OAuth2](#oauth2)
    - [Django OAuth Toolkits](#django-oauth-toolkits)
    - [bắt đầu chứng thực bằng postman](#bắt-đầu-chứng-thực-bằng-postman)
    - [defind định nghĩa một API /users/current-user/](#defind-định-nghĩa-một-api-users-current-user)
    - [lấy danh sách comment - api con của lessons](#lấy-danh-sách-comment---api-con-của-lessons)
    - [thêm bình luận mới vào bài học](#thêm-bình-luận-mới-vào-bài-học)
    - [chứng thực để có thể comment](#chứng-thực-để-có-thể-comment)
    - [quy tắc làm api create: phải trả về dữ liệu sau khi tạo](#quy-tắc-làm-api-create-phải-trả-về-dữ-liệu-sau-khi-tạo)
    - 


## xuất ra requirements
```
pip freeze > requirements.txt
```
## tải các gói thư viện trong requirements
```
pip install -r requirements.txt
```
# Quy tắc Import trong Python
- Import tuyệt đối (Absolute Import) – Dùng khi import từ module bên ngoài thư mục hiện tại.  
  Rõ ràng, dùng tốt cho project lớn.
  ```
  from courses.models import Category
  from django.template.response import TemplateResponse
  from courses import dao
  ```
- Import tương đối (Relative Import) – Dùng khi import trong cùng thư mục.  
  Ngắn gọn, nhưng dễ lỗi khi thay đổi thư mục.
  ```
  from .models import Category
  ```
- Import cả module – Dùng khi muốn import toàn bộ file/module.
  Khi dùng phải gọi đầy đủ courses.dao.function_name().
  ```
  import courses.dao
  ```
  ##  Kinh nghiệm thực tế:
  - Dùng Absolute Import cho project lớn để tránh lỗi khi thay đổi thư mục.
  - Dùng Relative Import khi làm việc trong cùng một app nhỏ để code gọn hơn.
 
## tự động sắp xếp import theo thứ tự chuẩn PEP8
- cài extension isort trong vscode để tự sắp xếp các import theo thứ tự chuẩn của PEP8
## mikegrations
```
python manage.py makemigrations courses
```
## migrate
```
python manage.py migrate
```
chạy server django
```
python manage.py runserver
```
## hướng dẫn chứng thực
1. vào postman: chọn method POST, paste url, và chọn body > form-data (khoảng line 1390) hoặc raw > json
   ```
   http://127.0.0.1:8000/o/token/
   ```
2. vào trang admin đăng nhập admin
   ```
   http://127.0.0.1:8000/admin/
   ```
   ```
   http://127.0.0.1:8000/o/applications/
   ```
   tạo app và phải copy client_id và client_secret lưu vào  
   nếu đã có thì không cần tạo lại
3. thêm cấu hình này trong setting
   ```
   DAUTH2_PROVIDER = {
    "OAUTH2_BACKEND_CLASS": "bauth2_provider.oauth2_backends.JSONOAuthLibCore"
   }
   ```
4. quay lại postman ghi dữ liệu vào và thực hiện send
   - phần này ghi dữ liệu json
```
{
    "client_id": "uLZYLmAw9sFvEWOlPnyLlEGMiHXOrRLnag4IsmTK",
    "client_secret": "7HUEH6pfe3vHkhPSVaPRradXkOIWNgxHijggGqiJyXLmckBC1hXu2YNrbd3DZoQhARJveQ8NjGZzENoxbnLIqVvQaNCgjCJcnELwhAaQgNZjgRqr1jfrYWxzYBmVMJCZ",
    "username":"admin",
    "password": "1",
    "grant_type": "password"
}
```
1. ## cài đặt django 
```
pip install django
```
```
 django-admin startproject courseapp
```
```
cd courseapp
```
```
 python manage.py runserver
```
2. ## kết nối cơ sở dữ liệu mySQL
- tạo 1 db mới mới: coursedb
- utf8mb4/utf8-unicode

3. ## tạo app
```
django-admin startapp courses
```
- trong đó course: là tên mới do người dùng đặt
- khai báo trong setting có app mới
```
'courses.apps.CoursesConfig'
```
4. ## kết nối CSDL
```
pip install pymysql
```
5. ## import trong setting.py 
(nếu import mà không dùng được: bị gạch chân => ctrl + shift + p => select interpreter => chọn python đang dùng <vì nó chưa ở đúng python>)
- copy phần này vào biến database
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'coursedb',
        'USER': 'root',
        'PASSWORD': 'Admin@123',
        'HOST': '' # mặc định localhost
    }
}
```
## tạo model truy vấn thử
### trong models
```
from django.contrib.auth.models import AbstractUser
```
class User(AbstractUser):
      pass
```
```
class Category(models.Model):
      name = models.CharField(max_length = 50, null = False)
      
      def __str__(self):
            return self.name
```
### trong setting
```
```
AUTH_USER_MODEL = 'courses.User'
```
tạm hiểu: dùng AUTH_USER_MODEL của mình để chứng thực chứ không dùng cái của nó
chạy lệnh: 
```
python manage.py makemigrations courses
```
nếu xảy ra lỗi: hãy thử:
```
pip install cryptography
```
ra kết quả như dưới là chính xác:
```
Migrations for 'courses':
  courses\migrations\0001_initial.py
    + Create model Category
    + Create model User
```
## thực hiện để xem mysql
```
python manage.py sqlmigrate courses 0001
```
với 0001 là tên file.py trong folder migrations => file: 0001_initial.py được tạo từ lệnh python manage.py makemigrations courses
```
python manage.py migrate
```
vào trong mysql refresh ta sẽ thấy các table được tạo ra
## kiểm tra 1 vài lệnh
```
python manage.py shell
```
```
from courses.models import *
```
```
Category.objects.create(name = "Cong nghe phan mem")
```
```
Category.objects.create("khoa hoc mau tinh")
```
```
Category.objects.create("khoa hoc du lieu")
```
ctrl + z để thoát ra 
## kiểm tra trên django
```
python manage.py runserver
```
6. ## tạo supper user
```
python manage.py createsuperuser
```
sau khi tạo thành công, đăng nhập tài khoản vừa tạo vào web http://127.0.0.1:8000/admin để kiểm tra
lúc này sẽ thấy file admin.py trong: courses > migrations > admin.py
7. ## import trong admin
```
from .models import Category
```
```
admin.site.register(Category)
```
8. ## custom theo ý người dùng 
# trong admin thực hiện ghi đè mặc định
```
class CategoryAdmin(admin.ModelAdmin):
      list_display = ['pk', 'name']
      search_fields = ['name']
      list_filter = ['id', 'name']
```
sau khi ghi đè, gắn phần ghi đè vừa tạo vào trang, để yêu cầu thực hiện theo dev chứ không phải hệ thống, bằng cách gắn thêm biến CategoryAdmin vào
```
admin.site.register(Category, CategoryAdmin)
```
9. ## tạo class Course trong models
trong folder courses => tạo folder: static => tạo folder: course
trong setting.py paste biến MEDIA_ROOT (vị trí nào cũng được)
```
MEDIA_ROOT = '%s/courses/static' % BASE_DIR
```
```
class Course(models.Model):
      subject = models.CharField(max_length=255, null = False)
      description = models.TextField()
      created_date = models.DateField(auto_now_add=True)
      updated_date = models.DateTimeField(auto_now=True)
      active = models.BooleanField(default=True)
      image = models.ImageField(upload_to='courses/%Y/%m')
      category = models.ForeignKey(Category, on_delete=models.RESTRICT)
      
      def __str__(self):
            return self.subject
```
## phân biệt auto now và auto now add
### auto_now=True
+ Cập nhật giá trị ngày/giờ thành thời điểm hiện tại mỗi khi đối tượng được lưu (save).
+ Dùng cho các trường cần cập nhật thời gian mỗi lần thay đổi, như updated_at.
### auto_now_add=True
+ Chỉ đặt giá trị ngày/giờ một lần khi đối tượng được tạo và không thay đổi sau đó.
+ Dùng cho các trường cần lưu thời điểm tạo, như created_at
## sử dung on delete trong khóa ngoại
### on_delete quy định hành vi khi một bản ghi liên quan bị xóa trong quan hệ ForeignKey. 
- CASCADE: Xóa bản ghi liên quan khi bản ghi gốc bị xóa.
  ví dụ cụ thể: khi danh mục của khóa học bị xóa thì khóa học cũng bị xóa theo
- SET_NULL: Đặt khóa ngoại thành NULL (cần null=True).
  ví dụ: khi trường danh mục category bị xóa, thì trường này (Course) bằng null
- RESTRICT: Chỉ chặn xóa nếu có ràng buộc khác ảnh hưởng.
- SET_DEFAULT: Đặt khóa ngoại thành giá trị mặc định (cần default=value).
- SET(): Gán khóa ngoại bằng một giá trị hoặc hàm tùy chỉnh.
- PROTECT: Ngăn không cho xóa bản ghi gốc (gây lỗi nếu cố xóa).
- DO_NOTHING: Không thực hiện hành động nào, có thể gây lỗi tham chiếu nếu không xử lý thủ công.

10. ## tạo kế thừa những cái dùng chung thành những class riêng
- thực hiện tạo class mới và xóa những cái dùng chung trong class course
- đây là lớp sử dụng cho các lớp khác, không cần tạo ra => trừu tượng
- dùng lớp lồng trong lớp class Meta => abstract = True
```
class BaseModel(models.Model):
      created_date = models.DateField(auto_now_add=True)
      updated_date = models.DateTimeField(auto_now=True)
      active = models.BooleanField(default=True)
      
      class Meta:
            abstract = True
```
- dùng class course kế thừa lại BaseModel
```
class Course(BaseModel):
      subject = models.CharField(max_length=255, null = False)
      description = models.TextField()
      img = models.CharField(max_length=100)
      Category = models.ForeignKey(Category, on_delete=models.CASCADE)
      
      def __str__(self):
            return self.subject
```
dùng class category kế thừa lại BaseModel 
```
class Category(BaseModel):
      name = models.CharField(max_length = 50, null = False)
      
      def __str__(self):
            return self.name
```
11. ## tạo migrations
```
python manage.py makemigrations courses
```
```
 python manage.py migrate courses
```
12. ## quản trị trong admin
```
from .models import Course
```
13. ## tạo model class lesson
trong folder courses => static => tạo folder: lessons
```
class Lesson(BaseModel):
      subject = models.CharField(max_length=255, null = False)
      content = models.TextField()
      image = models.ImageField(upload_to='lessons/%Y/%m')
      course = models.ForeignKey(Course, on_delete=models.CASCADE)
```
14. ## ràng buộc meta
thực hiện ràng buộc trong model class Course
trong class course có class Meta <class con>
```
class Meta:
         unique_together = ('subject', 'category')
```
trong class Lesson có class Meta
```
class meta:
         unique_together = ('subject', 'course')
```
- mẫu khi kết hợp 2 class
```
class Course(BaseModel):
      subject = models.CharField(max_length=255, null = False)
      description = models.TextField()
      image = models.ImageField(upload_to='courses/%Y/%m')
      category = models.ForeignKey(Category, on_delete=models.RESTRICT)
      
      def __str__(self):
            return self.subject
      
      class Meta:
            unique_together = ('subject', 'category')
```
15. ## gắn tag làm many to many
- tạo class model Tag
- nếu không overwrite to string => tag sẽ hiện thị: tag object(1)
- khi overwrite lên => ghi đè tên lên => hiển thị tên do user/admin đặt
```
class Tag(BaseModel):
      name = models.CharField(max_length=50, unique=True)

      def __str__(self):
               return self.name
```
gắn thêm biến tag lên class Lesson
- 1 bài học sẽ gắn tag gì
- vì class Tag ở dưới class Lesson nên khi gọi Tag ta phải bỏ vào dấu '' => 'Tag' [chương trình chưa chạy tới ở dưới nên chưa biết biến ở đâu => phải thêm nháy]
- nếu class Tag ở phía trên Lesson thì khi gọi không cần phải bỏ vào dấu nháy 
```
tags = models.ManyToManyField('Tag')
```
class Lesson trở thành 
```
class Lesson(BaseModel):
      subject = models.CharField(max_length=255, null = False)
      content = models.TextField()
      image = models.ImageField(upload_to='lessons/%Y/%m')
      course = models.ForeignKey(Course, on_delete=models.CASCADE)
      tags = models.ManyToManyField('Tag')
      
      
      class meta:
            unique_together = ('subject', 'course')
```
tương tự thêm tag với class Course
```
tags = models.ManyToManyField('Tag')
```

16. ## tác động database để tạo model
đầu tiền cài thư viện 
```
pip install pillow
```
```
python manage.py makemigrations courses
```
```
python manage.py migrate
```
17. ## import trong admin
```
from .models import Lesson
from .models import Tag
```
tạo site.register cho lesson và tag 
```
admin.site.register(Lesson)
admin.site.register(Tag)
```
18. ## chỉnh sửa admin hiển thị ảnh đã upload 
import vào admin.py
Django 4.x và các phiên bản trước
```
from django.utils.html import mark_safe
```
nếu mark_safe không có => Trong Django mới hơn, mark_safe được di chuyển sang django.utils.safestring  
Django 5.0 và sau
```
from django.utils.safestring import mark_safe
```
- ## tạo lớp ghi đè hiển thị img
```
class CourseAdmin(admin.ModelAdmin):
      list_display = ['pk', 'subject', 'created_date', 'updated_date', 'category', 'active']
      readonly_fields = ['img']
      
      def img(self, course):
            if course:
                  return mark_safe(
                        '<img src="/static/{url}" width="120" />' \
                              .format(url= course.image.name)
                  )
```
## thêm css và js và trang ModelAdmin
- tạo thư mục css: static/css/style.css
- trong class Course: thêm class Media
- nguyên tắc: / từ static / vô 
```
class Media:
            css = {
                  'all': ('/static/css/style.css', )
            }
            js = ('/static/js/script.js',)
```
## tích hợp CKEditor vào admin
- hỗ trợ chỉnh sửa văn bản giống như Microsoft Word với các tính năng như in đậm, in nghiêng, chèn ảnh, bảng,...
cài thư viện 
```
pip install django-ckeditor
```
trong setting, vô biến: INSTALL _APP:
```
'ckeditor',
'ckeditor_uploader'
```
thêm biến cấu hình chỉ định nơi upload: đặt ở bất kì trong settting
```
CKEDITOR_UPLOAD_PATH = "ckeditor/images/"
```
cập nhập urls của project
trong urls.py 
import thư viện 
```
from django.urls import re_path
from django.urls import include
```
trong biến urlpatterns thêm phần tử: 
```
re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
```
## chỉnh sửa content của model Lesson
trong models import thư viện 
```
from ckeditor.fields import RichTextField
```
thay đổi content trong Lesson
```
content = RichTextField()
```
thay đổi description trong Course
```
description = RichTextField()
```
sau đó thực hiện make mikegrations và migrate
```
python manage.py makemigrations courses
```
```
python manage.py migrate
```
sau đó thực hiện chạy server lại 
```
python manage.py runserver
```
## xử lý upload hình
trong admin.py thực hiện import 
```
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
```
tạo class mới: xử lý cho Course nên đặt tên: CourseForm
```
class CourseForm(forms.ModelForm):
      description = forms.CharField(widget=CKEditorUploadingWidget)
      
      class Meta:
            model = Course
            fields = '__all__'
```
trong class CourseAdmin thêm biến:
```
form = CourseForm
```
thực hiện runserver lại để kiểm tra 
khi upload hình phải thêm đăng trước /static/<url hình> thì hình mới hiển thị được
## InlineModelAdmin chỉnh sửa nhiều model many to many
chỉnh sửa nhiều model có quan hệ với nhau trong cùng một trang của model cha  
tạo class trong admin.py
```
class TagInlineAdmin(admin.StackedInline):
      model = Tag
```
trong class CourseAdmin thêm biến:
```
inlines = ['TagInlineAdmin']
```
## django debug toolbar
- là một package giúp hiển thị thông tin chi tiết về các request, database queries, settings, và hiệu suất của ứng dụng Django ngay trên trình duyệt
- hữu ích cho việc debug và tối ưu hóa code trong quá trình phát triển.
-  Tính năng chính:
   + Hiển thị SQL queries, thời gian thực thi
   + Kiểm tra cache, signals, template rendering
   +  Xem thông tin request, response, session
cài đặt
```
pip install django-debug-toolbar
```
trong settings.py thêm vào biến INSTALLED_APPS
```
'debug_toolbar',
```
trong settings.py thêm vào biến MIDDLEWARE
```
'debug_toolbar.middleware.DebugToolbarMiddleware',
```
trong urls.py thêm vào biến urlpatterns
```
path("__debug__", include("debug_toolbar.urls")),
```
### cấu hình trong setting để debug_toolbar chạy local
```
INTERNAL_IPS = [
    "127.0.0.1",
]
```
chạy server lại để kiểm tra 
## tạo dao và viết hàm truy vấn
import thư viện vào dao.py
```
from .models import Category
from .models import Course
```
```
def load_coueses(params={}):
      q = Course.objects.filter(active = True)
      
      kw = params.get('kw')
      if kw:
            q = q.filter(subject__icontains=kw)
            
      cate_id = params.get('cate_id')
      if cate_id:
            q = q.filter(category_id=cate_id)
      
      return q
```
## truy vấn gom nhóm dữ liệu hoặc truy vấn thống kê
- sử dụng annotate()
     + dùng để thêm các giá trị tính toán (aggregate) vào mỗi đối tượng trong queryset.
     + Nó giúp bạn thực hiện các phép tính như đếm, tổng, trung bình... trên dữ liệu liên quan.
import thư viện
```
from django.db.models import Count
```
- ### order_by
     + Mặc định (ASC - Ascending - Tăng dần):  sẽ sắp xếp dữ liệu theo thứ tự tăng dần (nhỏ → lớn, A → Z).
     + Giảm dần (DESC - Descending - Giảm dần): ẽ sắp xếp theo thứ tự giảm dần (lớn → nhỏ, Z → A).
       ví dụ:
       ```
       users = User.objects.order_by('age')  # Sắp xếp theo tuổi tăng dần
       users_desc = User.objects.order_by('-age')  # Sắp xếp theo tuổi giảm dần
       ```
- câu lệnh truy vấn đơn giản
```
def count_courses_by_cate():
      return Category.objects.annotate(count = Count('course__id')).values("id", "name", "count").order_by("-count")
```
## adminsite - tùy chỉnh trang web  
   - Định nghĩa trang admin riêng thay vì mặc định (django.contrib.admin.site).
   - Tùy chỉnh giao diện & chức năng của Django Admin.
   - Quản lý nhiều trang admin với cấu hình khác nhau.
trong trang admin.py thực hiện:
không cần import vẫn thực hiện được <chỉ ghi vào import cho chắc>
```
from django.contrib.admin import AdminSite
```
- tạo một class adminsite
- nguyên tắc: tất cả các trang đều kế thừa trang adminsite
```
class CourseAppAdminSite(admin.AdminSite):
      site_header = 'isSuccess' # đặt tên gì cũng được
      
      
admin_site = CourseAppAdminSite(name='myapp')
```
như vậy, đăng ký app từ đây sẽ thay biến của nó thành biến của mình 
<biến của mình là admin_site>: (biến cũ là admin.site <đừng nhầm lẫn>)
```
# Register your models here.
admin_site.register(Category, CategoryAdmin)
admin_site.register(Course, CourseAdmin)
admin_site.register(Lesson)
admin_site.register(Tag)
```
chuyển qua trang urls.py để defind (định nghĩa) lại, lấy url của trang mới của mình
```
from courses.admin import admin_site
```
sửa lại thành đường path của mình 
```
path('admin/', admin_site.urls),
```
chạy lại server để kiểm tra
```
python manage.py runserver
```
thấy có isSuccess ==> đã chạy đúng
## thêm view mới vào admin site
import thư viện trong admin.py
```
from django.urls import path
```
trong admin.py thêm hàm vào class CourseAppAdminSite mới tạo mở trên
```
def get_urls(self):
            return [
                        path('course-stats/', self.stats_view)
                  ] + super().get_urls()
```
vậy ta đã có trang mới, mới endpoint là course-stats/
tạo folder và file mới: courses > templetes > admin > stats.html
trong stats.html
```
{% extends 'admin/base_site.html' %}
{% block content %}
<h1>Thống kê khóa học trực tuyến</h1>
{% endblock %}
```
import thư viện trong admin.py
```
from django.template.response import TemplateResponse
```
tiếp đó, viết hàm stats_view để nó gọi (vẫn viết trong class CourseAppAdminSite của admin.py), trong hàm này sẽ trả về một view mới 
```
def stats_view(self, request):
            return TemplateResponse(request, 'admin/stats.html') # đường dẫn theo vị trí tạo thư mục
```
thực hiện chạy runserver để kiểm tra: http://127.0.0.1:8000/admin/course-stats/
- sau khi thấy trang mới không lỗi: thực hiện hoàn thiện tiếp code trên

## đổ dữ liệu ra 
trong admin.py ghi hàm trong class CourseAppAdminSite cùng cấp với def stats_view
```
from courses import dao
```
```
def stats_view(self, request):
            return TemplateResponse(request, 'admin/stats.html',{
                        'stats': dao.count_courses_by_cate()
                        
                  }) # đường dẫn theo vị trí tạo thư mục
```
qua trang stats.html gọi biến stats vừa tạo 
```
<ul>
      {% for c in stats %}
            <li><strong>{{ c.name }}</strong>: {{ c.count }}</li>
      {% endfor %}
</ul>
```
chạy runserer để kiểm tra biến vừa tạo đã gọi được dữ liệu ra chưa
## vẽ biểu đồ charjs
import cdn charjs vào, tạm thời để ở stats.html
```
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```
bỏ vùng canvas vào: là vùng đồ họa, để đổ biểu đồ vào
```
<div>
      <canvas id="myChart"></canvas>
</div>
```
bỏ đoạn script vào window.onload để có thể chạy được
```
<script>
      let labels = [];
      let values = [];

      {% for c in stats %}
      labels.push('{{ c.name }}');  // vì c.name là chuỗi, nếu để không sẽ bị lầm tưởng là biến của javascript, phải thêm ''
      values.push({{ c.count }});
      {% endfor %}

      window.onload = () => {
            const ctx = document.getElementById('myChart');

      new Chart(ctx, {
      type: 'bar',
      data: {
            labels: labels,
            datasets: [{
            label: '# Số lượng',
            data: values,
            borderWidth: 1
            }]
      },
      options: {
            scales: {
            y: {
            beginAtZero: true
            }
            }
      }
      });
      }
</script>
```
## [khắc phục lỗi khi thêm {% %} trong vscode](#khắc-phục-lỗi-khi-thêm-{%-%}-trong-vscode)
- cài extensions:
     + django <mấy duy đang cài>
     + janja
- cách 2 (chưa thấy hiệu quả)
     + ctrl + shift + p => Preferences: Open user Settings (JSON) => thêm dòng lệnh vào
```
"javascript.validate.enable": false
```
# Xây dựng API theo yêu cầu
import gói thư viện 
```
pip install djangorestframework
```
```
pip freeze > requirements.txt
```
tạo file: courses > serializers.py
import category và course
```
from courses.models import Category
from courses.models import Course
from rest_framework import serializers
```
```
class CategorySeializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = "__all__"
```
qua view.py tạo serializer
```
from rest_framework import viewsets
from rest_framework import generics
from courses.models import Category
from courses import serializers
```
```
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySeializer
```
tạo file: courses > urls.py
ra urls.py ở ngoài trang chủ courseapp/urls.py link urls.py mới tạo vô 
```
path("", include("courses.urls")),
```
thực hiện code trong courses/urls.py
```
from django.urls import path
from django.urls import include
from rest_framework import routers
```
```
router = routers.DefaultRouter()
router.register("categories", views.CategoryViewSet, basename="categories")
urlpatterns = [
    path("", include(router.urls)),
]
```
trong setting.py thêm vào biến INSTALLED_APPS
```
"rest_framework",
```
## khái niệm swagger
- Swagger là một công cụ giúp tạo tài liệu API tự động cho ứng dụng Django REST framework (DRF)
- Nó hiển thị danh sách API, phương thức (GET, POST, PUT, DELETE), request/response mẫu và cho phép test API trực tiếp trên giao diện web.
## tích hợp swagger 
- cài đặt thư viện 
```
pip install drf-yasg
```
trong setting.py thêm vào biến INSTALLED_APPS
```
'drf_yasg',
```
trong courseapp/urls.py 
```
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
```
```
schema_view = get_schema_view(
    openapi.Info(
        title="Course API",
        default_version="v1",
        description="APIs for CourseApp",
        contact=openapi.Contact(email="thanh.dh@ou.edu.vn"),
        license=openapi.License(name="Dương Hữu Thành@2021"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
```
thêm vào mảng urlpatterns
## api categories
```
re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
```
chạy runserver để kiểm tra
```
python manage.py runserver
```
```
http://127.0.0.1:8000/swagger/
```
## api course khóa học
1. tạo class serializer trong serializers.py
```
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
```
2. tạo queryset trong class Viewset trong views.py
```
from courses.models import Course
```
```
class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True).all()
    serializer_class = serializers.CourseSerializer
```
3. vào courses/urls.py đăng ký cho nó 1 cái API
```
router.register("courses", views.CourseViewSet, basename="courses")
```
4. vào runserver và kiểm tra
```
python manage.py runserver
```
```
http://127.0.0.1:8000/swagger
```
## phân trang 
- một dạng mì ăn liền, lên docs để đọc thông tin, không cần nhớ
```
https://www.django-rest-framework.org/topics/documenting-your-api/
```
- slide có hướng dẫn phân trang toàn cục
- giờ thực hiện phân trang cục bộ
1. tạo một lớp paginator.py riêng: courses/pagiinators.py
2. nguyên tắc: dùng hướng đối tượng, kế thừa
import thư viện đọc từ docs
```
from rest_framework.pagination import PageNumberPagination
```
```
class CoursePpaginator(PageNumberPagination):
    page_size = 2
```
gọi lớp vừa tạo bên views.py để sử dụng 
import 
```
from courses import paginators
```
trong class CourseViewSet cho thêm 1 thuộc tính
```
    pagination_class = paginators.CoursePpaginator
```
vào runserver để kiểm tra 
```
http://127.0.0.1:8000/swagger/
```
## custom lại đường dẫn hình ảnh
```
http://127.0.0.1:8000/courses/?page-1
```
khi vào đường dẫn và chọn linlk hình ảnh ta thấy lỗi => phải custom lại 
vào serializers.py > class CourseSerializer
```
image = serializers.SerializerMethodField(source="image")

    def get_image(self, course):
        if course.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri("/static/%s" % course.image.name)
```
## hiển thị thông tin tên của tag
trong serialixers.py 
import 
```
from courses.models import Tag
```
tạo 1 class mới 
```
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]
```
sau đó trong class CourseSerializer gọi lại trường tag vừa được tạo ở trên
```
tags = TagSerializer(many=True)
```
chạy lại server để kiểm tra
```
http://127.0.0.1:8000/courses/?page-2
```
lúc này nó sẽ hiển thị thông tin tags ra cho mình xem
## thêm phần lọc dữ liệu 
## lấy danh sách tất cả khóa học
- vd: &category_id=&q=
trong views.py thực hiện can thiệp query trước khi nó trả về all
trong class CourseViewSet thêm hàm
```
def get_queryset(self):
        queries = self.queryset

        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries
```
thực hiện runserver vào xem phần subject là vì và tìm kiếm xem có ra không 
```
http://127.0.0.1:8000/courses/?q=Introduce
```
tương tự thực hiện với class CategoryViewSet
phần này tự làm, chưa biết đúng sai
```
def get_queryset(self):
        queries = self.queryset

        # q = self.request.GET.get("q")
        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(name__icontains=q)
        return queries
```
```
http://127.0.0.1:8000/categories/?q=Category
```
## lấy danh sách các bài học của một khóa học
- defind một API mới không nằm trong các chuẩn generics.ListAPIView trong CourseViewSet
- thực hiện viết hàm trong class CourseViewSet
- nếu đường dãn không có course_id thì không để biến pk vào, nếu có thì để
- import thư viện trong views.py
```
from rest_framework.decorators import action
```
trong serializers.py thực hiện tạo một class lessonSerializer
```
from courses.models import Lesson
```
```
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
```
vì thấy trong lesson có có thuộc tính: image, tags giống CourseSerializer:
cắt 2 thuộc tính này ra cho vào class mối, và thực hiện kế thừa class đó
```
class BaseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source="image")
    tags = TagSerializer(many=True)

    def get_image(self, course):
        if course.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri("/static/%s" % course.image.name)
```
lúc này: CourseSerializer và LessonSerializer sẽ kế thừa lại BaseSerializer
```
class CourseSerializer(BaseSerializer):

    class Meta:
        model = Course
        fields = "__all__"
```
```
class LessonSerializer(BaseSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "subject", "image", "tags"]

```
chuyển qua thực hiện viết hàm bên views.py 
- thực hiện viết hàm trong class CourseViewSet
```
    # nếu detail=True => có biến tham số pk ở hàm
    # nếu detail=False => không có biến tham số pk ở hàm
    # pk: tham số id: đại diện cho model Course
    @action(methods=["get"], detail=True)
    def lessons(self, request, pk):
        lessons = self.get_object().lesson_set.filter(active=True).all()

        # # thử debug
        # import pdb
        # pdb.set_trace()

        return Response(
            serializers.LessonSerializer(
                lessons, many=True, context={"request": request}
            ).data,
            status=status.HTTP_200_OK,
        )

```
chạy runserver và kiểm tra, trước đó, nếu chưa tạo dữ liệu cho lesson thì phải vào tạo
- kiểm tra mysql courses_lesson nếu rỗng tức chưa tạo dữ liệu
```
http://127.0.0.1:8000/admin/courses/lesson/
```
```
http://127.0.0.1:8000/courses/1/lessons/
```
nếu gặp lỗi thử debug ở dưới
# thử debug
```
 # thử debug
        import pdb
        pdb.set_trace()
```
vào trang lỗi, tải lại, sau đó bên terminal sẽ hiển thị pdb
nhập vào để xem có kết quả không\
- lesssons là biến code ở trên tạo
```
lesssons
```
giả sử ở trên đúng, nhập tiếp pk xem có hiển thị khóa không
```
pk
```
## API chi tiết bài học 
trong views.py thực hiện tạo một class mới
```
from courses.models import Lesson
```
```
class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True).all()
    serializer_class = serializers.LessonSerializer
```
vậy là xong api cơ bản  
qua resources/urls.py đăng ký một router mới 
```
router.register("lessons", views.LessonViewSet, basename="lessons")
```
thực hiện runserver swagger thì sẽ thấy một api mới được tạo ra
```
http://127.0.0.1:8000/swagger/
```
thực hiện try it out và điền id kiểm tra thử 
## đăng ký user
- defind ra một class user trong serializers.py
- phải định nghĩa được đăng ký cần dùng những trường gì
import user vào
```
from courses.models import User
```
```
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
        ]  # cái này trong model của django đã có sẵn những trường này rồi
```
sau đó, dùng những trường này cho nó tạo đối tượng 
trong views.py thực hiện tạo một class view mới
```
from courses.models import User
```
```
# để post và chèn vô => CreateAPIView
class UserViewset(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = serializers.UserSerializer
```
tạo router đăng ký trong resourses/urls.py
```
router.register("users", views.UserViewset, basename="users")
```
lúc này, nó đã hình thành một bộ API và chỉ có duy nhất một API
thực hiện runserver để kiểm tra
```
python manage.py runserver
```
```
http://127.0.0.1:8000/swagger/
```
lúc này thấy user có phương thức post là đúng
## chạy postman kiểm tra 
yêu cầu: phải sài được postman
- chọn phương thức post
- thêm đường dẫn vào
```
http://127.0.0.1:8000/users/
```
body => raw => json 
trong bảng ghi nội dung để kiểm tra
```
{
    "first_name": "nhat",
    "last_name": "duy",
    "username":"nhatduy242",
    "password": 1,
    "email": "nhatduy242@gmail.com"
}
```
nhấn nút send => nếu xuất hiện màu xanh 201 created => tạo thành công 
- tuy nhiên có vấn đề: password đang được lưu hiển thị => không bảo mật => can thiệp hàm để băm mật khẩu
- ghi đè lại phương thức create trong class UserSerializer bằng cách tạo hàm trong class UserSerializer
```
def create(self, validated_data):
        data = validated_data.copy()

        user = User(**data)
        user.set_password(data["password"])
        user.save()

        return user
```
thực hiện đổi username mới và kiểm tra postman lại 
```
{
    "first_name": "nhat",
    "last_name": "duy",
    "username":"nhatduy2705",
    "password": 1,
    "email": "nhatduy242@gmail.com"
}
```
lúc này nếu ra 200 và kết quả cho password đã băm là chính xác
ví dụ kết quả password trả về:
```
  "password": "pbkdf2_sha256$870000$SiwU5arVZ7QaWLkysU79kz$MU3yMmYJO/QaWOS667kCi1Qabh34qNoj4hnrKg6+h2U=",
```
tuy nhiên: khi đọc user không ai trả về password như vậy, không ai đọc api mà trả mã băm về
- không hiểu
- nhiều vấn đề
thực hiện thêm biến vào class UserSerializer
```
extra_kwargs = {"password": {"write_only": True}}
```
vậy class UserSerializer sẽ trở thành:
```
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
        ]  # cái này trong model của django đã có sẵn những trường này rồi
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        data = validated_data.copy()

        user = User(**data)
        user.set_password(data["password"])
        user.save()

        return user
```
thực hiện đổi user và kiểm tra postman lại 
lúc này, kết quả nhận được không hiển thị phần password nữa 
## upload hình ảnh lên couldinary
cài gói thư viện 
```
pip install cloudinary
```
```
pip freeze > requirements.txt
```
trong setting.py vào biến INSTALLED_APPS thêm:
```
 "cloudinary",
```
trong models.py import thư viện 
```
from cloudinary.models import CloudinaryField
```
```
class User(AbstractUser):
    avatar = CloudinaryField("avatar", null = True)
```
qua serializers.py thêm trường avatar vào UserSerializer
```
fields = [
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
            "avatar",
        ]
```
copy phần code trên docs của cloudinary vào settting.py (đặt ở đâu cũng được)
```
https://console.cloudinary.com/pm/c-036c8753dcf1d538b7c7cdec713f4b/getting-started
```
```
import cloudinary

# Configuration
cloudinary.config(
    cloud_name="devtqlbho",
    api_key="654785974366212",
    api_secret="yBPftN_K0QlSh0mAUyCZ-ewTxUY",
    secure=True,
)
```
qua views.py: để upload cần có một parsers
import parsers
```
from rest_framework import parsers
```
trong class UserViewset bật parsers class lên
```
 parser_classes = [
        parsers.MultiPartParser
    ]  # nhờ thằng này, nó sẽ tiến hành upload được tập tin của mình, upload hẳn lên cloudinary chứ không còn server
```
thực hiện makemigration lại 
```
python manage.py makemigrations
```
```
python manage.py migrate
```
chạy server lên và thực hiện kiểm tra bằng postman
```
python manage.py runserver
```
thực hiện kiểm tra thử bằng postman
- để test upload thì không dùng json được vì nó không gửi file lên được
- dùng form-data để test: body => form-data
```
key: frist_name; last_name; username; password; avatar <chọn loại file>
value: nhat; duy; upload1; 1; chọn hình
```
nhấn nút send để kiểm tra
- nếu xuất hiện trường avatar và hiện 201 là đúng: đã trên server của cloudinary
- vào media library để kiểm tra
## OAuth2
- là một giao thức ủy quyền (authorization) cho phép ứng dụng bên thứ ba truy cập tài nguyên trên một dịch vụ mà không cần chia sẻ thông tin đăng nhập.
- Nó hoạt động dựa trên các token thay vì mật khẩu, giúp tăng cường bảo mật.
## Django OAuth Toolkits
- Django OAuth Toolkit (DOT) là một thư viện giúp tích hợp OAuth2 vào ứng dụng Django, cho phép tạo máy chủ OAuth2 để quản lý xác thực và cấp quyền truy cập API một cách an toàn

cài đặt gói thư viện 
```
pip install django-oauth-toolkit
```
```
pip freeze > requirements.txt
```
Cập nhật biến INSTALLED_APP trong settings.py
```
'oauth2_provider',
```
Bổ sung thông tin cấu hình cho biến REST_FRAMEWORK trong settings.py (tạo biến mới)
```
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    )
}
```
Cập nhật urls cho URLConfig của project: urls ở ROOT hay: courseapp/urls.py
```
path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
```
thực hiện chạy lại mikegrate và runserver để kiểm tra
11. ## tạo migrations

```
 python manage.py migrate
```
```
python manage.py runserver
```
vào admin để đằng nhập: 
```
http://127.0.0.1:8000/admin/
```
```
http://127.0.0.1:8000/o/applications/
```
trong setting.py copy key bỏ vào 
```
CLiENT_ID = "uLZYLmAw9sFvEWOlPnyLlEGMiHXOrRLnag4IsmTK"
CLIENT_SCERET = "7HUEH6pfe3vHkhPSVaPRradXkOIWNgxHijggGqiJyXLmckBC1hXu2YNrbd3DZoQhARJveQ8NjGZzENoxbnLIqVvQaNCgjCJcnELwhAaQgNZjgRqr1jfrYWxzYBmVMJCZ"
```
name: "tên tự do"
client_type: "confidential"
Authorization grant type: "resource owner password-based"
=> save
## bắt đầu chứng thực bằng postman
- vào postman tạo post mới
- url chứng thực, methods = POST
  ```
  http://127.0.0.1:8000/o/token/
  ```
body => form-data
```
username: admin
password: 1
client_id: uLZYLmAw9sFvEWOlPnyLlEGMiHXOrRLnag4IsmTK
client_secret: 7HUEH6pfe3vHkhPSVaPRradXkOIWNgxHijggGqiJyXLmckBC1hXu2YNrbd3DZoQhARJveQ8NjGZzENoxbnLIqVvQaNCgjCJcnELwhAaQgNZjgRqr1jfrYWxzYBmVMJCZ
grant_type: password
```
thực hiện nhấn send => kết quả sẽ có access_token
- với access_token này, thực hiện API để chứng thực
## defind định nghĩa một API /users/current-user/
và user đó phải được chứng thức
- trong views.py: viết hàm vào class UserViewset
```
from rest_framework import permissions
```
```
def get_permissions(self):
        if self.action.__eq__("current-user"):
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]
```
tất cả các thông tin sau khi chứng thực sẽ được nằm trong đối tượng: request.user   
```
    # nó gọi API này khi nó đã được chứng thực rồi
    @action(methods=["GET"], url_name="current-user", detail=False)
    def current_user(self, request):
        return Response(serializers.UserSerializer(request.user).data)
```
thực hiện runserver và kiểm tra bằng postman 
```
http://127.0.0.1:8000/swagger/
```
kiểm tra xem đã có /users/current_user/ chưa
sau đó thực hiện kiểm tra postman, tại post mới, phương thức get
```
http://127.0.0.1:8000/users/current_user/
```
nó hiển thị:  "detail": "Authentication credentials were not provided." => không có quyền
bắt đầu chứng thực bằng cách đưa: access_token vô 
- vào headers > nhập key: ```Authorization```
- bỏ token vô: ```bearer P7LrMVheL7PY70vWccN6JY1d8Q04iE```
- khi send => nó trả về kêt quả và 200 là đúng
## lấy danh sách comment - api con của lessons
- tương tự như trên, thực hiện api cho tương tác: comment và like

tổ chức model: tạo một model mới: Interaction, kế thừa BaseModel, thêm 2 thông tin riêng
- user nào thực hiện Interaction này
- comment trên bài học nào, like trên bào học nào
  => đây là thông tin chung của tất cả các tương tác
  không nên gộp phần comment và đánh giá vô cùng một table => gây lãng phí tài nguyên trong thiết kế dữ liệu
trong models.py sử dụng trừu tượng cho class model mới tạo
```
class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=False)

    class Meta:
        Abstract = True
```
trong models.py tạo class Like 
```
class Comment(Interaction):
    content = models.CharField(max_length=255, null=False)
```
thực hiện makemigrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```
kiểm tra trong mysql server sẽ thấy courses_comment, trong bài tập lớn phần vấn đáp: xuất cho thầy phần lược đồ cơ sở quan hệ, tuy nhiên chỉ xuất những cái nào của mình. còn cái nào của nó đừng xuất 
bởi vì nếu xuất là xuất rất nhiều

trong models.py tạo class Like (tương tự class comment):
```
class Like(Interaction):
    active = models.BooleanField()  # like hoặc chưa like
```
trong models.py tạo class Rating (đánh giá từ 1 -> 5):
```
class Rating(Interaction):
    rate = models.SmallIntegerField(default=0)  # đánh giá sao từ 1 đến 5
```
tạo makemigrations
```
python manage.py makemigrations courses
```
```
 python manage.py migrate
```
lúc này sẽ có 2 model trong mysql: courses_like và courses_rating
## thêm bình luận mới vào bài học
- thêm bài mới: method = POST
- phải chứng thực mới được thêm
trong views.py > class LessonViewSet định nghĩa một API
nếu để bình thường thì sẽ không có ý nghĩa gì, bắt buộc phải gắn
```
@action(methods=["POST"], url_path="comments", detail=True)
```
trong yêu cầu /lessons/{lesson_id}/comments/: có biến: {lesson_id} => detail phải là True => trong hàm phải có pk truyền vào
```
from courses.models import Comment
```
```
    @action(methods=["POST"], url_path="comments", detail=True)
    def add_comment(self, request, pk):
        # user đã chứng thực rồi sẽ nằm trong request.user
        # tất cả dữ liệu từ body data lấy từ client lấy lên đều trong: request.data
        c = Comment.objects.create(
            user=request.user,
            lesson=self.get_object(),
            content=request.data.get("content"),
        )
```
## chứng thực để có thể comment
```
permission_classes = [permissions.AllowAny]  # ai cũng được
```
```
    # tùy nhiên, ở dưới thì phải xác thực mới được comment => thực hiện ghi đè

    def get_permissions(self):
        if self.action in ["add_comment"]:
            return [permissions.IsAuthenticated()]
        return self.permission_classes
```
## quy tắc làm api create: phải trả về dữ liệu sau khi tạo
- để trả về được: phải tạo một serializer
vào serializers.py thực hiện tạo mới mới một serializers:
```
from courses.models import Comment
```
```
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # để lấy avatar của user

    class Meta:  # thực hiện ghi đè
        model = Comment
        fields = ["id", "content", "user"]
```
sau khi có serializer thực hiện quay lại views.py để return hàm add_comment trong LessonViewSet
```
return Response(
            serializers.CommentSerializer(c).data, status=status.HTTP_201_CREATED
        )
```
vậy lúc này class LessonViewSet sẽ trở thành 
```
class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True).all()
    serializer_class = serializers.LessonSerializer
    permission_classes = [permissions.AllowAny]  # ai cũng được
    # tùy nhiên, ở dưới thì phải xác thực mới được comment => thực hiện ghi đè

    def get_permissions(self):
        if self.action in ["add_comment"]:
            return [permissions.IsAuthenticated()]
        return self.permission_classes

    @action(methods=["POST"], url_path="comments", detail=True)
    def add_comment(self, request, pk):
        # user đã chứng thực rồi sẽ nằm trong request.user
        # tất cả dữ liệu từ body data lấy từ client lấy lên đều trong: request.data
        c = Comment.objects.create(
            user=request.user,
            lesson=self.get_object(),
            content=request.data.get("content"),
        )

        return Response(
            serializers.CommentSerializer(c).data, status=status.HTTP_201_CREATED
        )
```
thực hiện runserver 
```
python manage.py runserver
```
vào kiểm tra xem có phương thức post lesson/{id}/comment 
```
http://127.0.0.1:8000/swagger/
```
muốn chạy: 
- thực hiện vào postman: tạo chứng thực lấy token ra 
- sau khi đã có access_token (ví dụ dưới lấy bằng postman, không biết access_token có thay đổi không)
```
"access_token": "2qtIWyQ3lWRKhcpBTsWGKsNTEDJ1ir",
```
- tạo một postman mới, phương thức post, body: raw > JSON,  url:
```
http://127.0.0.1:8000/lessons/1/comments/
```
```
{
    "content": "good"
}
```
khi gửi lên sẽ có kết quả 
```
    "detail": "Authentication credentials were not provided."
```
vì chưa chứng thực, thực hiện thêm chứng thực
vào headers, bỏ token vào key:Authorization; value: Bearer + token  
sẽ nhận được kết quả phản hồi, ví dụ:
```
{
    "id": 1,
    "content": "good",
    "user": {
        "first_name": "",
        "last_name": "",
        "username": "admin",
        "email": "admin@gmail.com",
        "avatar": null
    }
}
```
vô mysql courses_comment xem để tra 

