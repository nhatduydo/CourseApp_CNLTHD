# CourseApp_CNLTHD
Công nghệ lập trình hiện đại
# Mục lục
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



## cài đặt django 
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
```
class Course(models.Model):
      subject = models.CharField(max_length=255, null = False)
      description = models.TextField()
      created_date = models.DateField(auto_now_add=True)
      updated_date = models.DateTimeField(auto_now=True)
```
## phân biệt auto now và auto now add
### auto_now=True
+ Cập nhật giá trị ngày/giờ thành thời điểm hiện tại mỗi khi đối tượng được lưu (save).
+ Dùng cho các trường cần cập nhật thời gian mỗi lần thay đổi, như updated_at.
### auto_now_add=True
+ Chỉ đặt giá trị ngày/giờ một lần khi đối tượng được tạo và không thay đổi sau đó.
+ Dùng cho các trường cần lưu thời điểm tạo, như created_at
