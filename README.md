# CourseApp_CNLTHD
Công nghệ lập trình hiện đại
# Mục lục
1. [cài đặt django](#cài-đặt-django)
2. [kết nối cơ sở dữ liệu mySQL](#kết-nối-cơ-sở-dữ-liệu-mySQL)
3. [tạo app](#tạo-app)
4. [kết nối CSDL](#kết-nối-CSDL)
5. [import trong setting.py](#import-trong-setting.py)
   - [tạo model truy vấn thử](#tạo-model-truy-vấn-thử)

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
  
