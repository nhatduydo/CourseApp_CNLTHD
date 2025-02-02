# CourseApp_CNLTHD
Công nghệ lập trình hiện đại
# Mục lục
[tải các gói thư viện trong requirements](#tải-các-gói-thư-viện-trong-requirements)  
[xuất ra requirements](#xuất-ra-requirements)
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
   - [tạo lớp ghi đè](#tạo-lớp-ghi-đè)
## xuất ra requirements
```
pip freeze > requirements.txt
```
## tải các gói thư viện trong requirements
```
pip install -r requirements.txt
```
# 1. ## cài đặt django 
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
## kết nối cơ sở dữ liệu mySQL
- tạo 1 db mới mới: coursedb
- utf8mb4/utf8-unicode

## tạo app
```
django-admin startapp courses
```
- trong đó course: là tên mới do người dùng đặt
- khai báo trong setting có app mới
```
'courses.apps.CoursesConfig'
```
## kết nối CSDL
```
pip install pymysql
```
## import trong setting.py 
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
## tạo supper user
```
python manage.py createsuperuser
```
sau khi tạo thành công, đăng nhập tài khoản vừa tạo vào web http://127.0.0.1:8000/admin để kiểm tra
lúc này sẽ thấy file admin.py trong: courses > migrations > admin.py
## import trong admin
```
from .models import Category
```
```
admin.site.register(Category)
```
## custom theo ý người dùng 
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
## tạo class Course trong models
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

## tạo kế thừa những cái dùng chung thành những class riêng
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
## tạo migrations
```
python manage.py makemigrations courses
```
```
 python manage.py migrate courses
```
## quản trị trong admin
```
from .models import Course
```
## tạo model class lesson
trong folder courses => static => tạo folder: lessons
```
class Lesson(BaseModel):
      subject = models.CharField(max_length=255, null = False)
      content = models.TextField()
      image = models.ImageField(upload_to='lessons/%Y/%m')
      course = models.ForeignKey(Course, on_delete=models.CASCADE)
```
## ràng buộc meta
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
## gắn tag làm many to many
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

## tác động database để tạo model
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
## import trong admin
```
from .models import Lesson
from .models import Tag
```
tạo site.register cho lesson và tag 
```
admin.site.register(Lesson)
admin.site.register(Tag)
```
## chỉnh sửa admin hiển thị ảnh đã upload 
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
- ## tạo lớp ghi đè
```
class CourseAdmin(admin.ModelAdmin):
      readonly_fields = ['img']
      
      def img(self, course):
            if course:
                  return mark_safe(
                        '<img src="/static/{url}" width="120" />' \
                              .format(url= course.image.name)
                  )
```
























