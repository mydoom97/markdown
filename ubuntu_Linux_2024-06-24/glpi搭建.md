# 环境：
- rocky8.9
- mariadb 10.3
- php 8.3
- apache 2.4
- glpi 10.0.12


## 1.Apche 2.4

```
yum install httpd*
systemctl start httpd
systemctl enable httpd

```
---

## 2.mariadb 10.3


```shell
yum install mariadb*
systemctl start mariadb
systemctl enable mariadb
```





### 2-1. 创建数据库、用户名、密码并授权


```
create databases glpi;
create user 'glpi'@'localhost' identified by 'glpi';
grant all privileges on glpi.*  to  'glpi'@'localhost';
```

---

## 3. PHP 8.3

### 3-1.安装php支持库

``
yum install remi-release 
``

### 3-2. 查看php列表并启用8.3


```
dnf module list php
dnf module enable php:remi-8.3
```

### 3-3.安装php8.3及其所有组件

``
dnf module install php:remi-8.3 -y
``

---


## 4.glpi 10.0.12


> https://github.com/glpi-project/glpi/releases

### 4-1.解压到目录

```
tar zxvf glpi 
mv glpi /var/www/html
```
### 4-2.授权

```
chown -R apache:apache /var/www/html/glpi
chown -R apache:apache /var/www/html/glpi/config
chown -R apache:apache /var/www/html/glpi/files

```
