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
