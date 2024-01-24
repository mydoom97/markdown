# Webmin:开源的LinuxWeb管理工具
## 1.下载压缩包
> https://github.com/webmin/webmin/release
## 2.环境准备
### 2-1.关闭防火墙

```
    systemctl stop firewalld.service
    systemctl disable firewalld.service
```
### 2-2.关闭SELinux
```
    setenforce 0
    sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
```
### 2-3.解压安装包
```
    cd /home/                    # 进入要解压的目录，如/home/
    tar -zxvf webmin-*.tar.gz    # 解压
```
## 3.安装
### 3-1.安装依赖包
```
    yum -y install perl-CPAN  #进入web管理界面安装终端时用到
```
### 3-2.安装Webmin
```
    cd /home/webmin-*/
    chmod +x setup.sh
    ./setup.sh
```