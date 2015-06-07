##部署过程

1. 安装python 2.7，添加环境变量 `C:\Python27`

2. 安装django 1.6，必要时添加环境变量 `C:\Python27\Scripts`
    ```
    python setup.py install
    ```
3. 下载安装 [MySQL for Python](http://sourceforge.net/projects/mysql-python/)

4. 创建数据库（MySQL）
    ```sql
    create database supermarket collate utf8_general_ci;
    ```

5. 由django 创建数据库表
    ```
    python manage.py syncdb
    ```

6. 启动服务器
    ```
    python manage.py runserver
    ```