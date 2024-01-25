# 以下系统的网卡基本配置及防火墙启停及文件位置
[TOC]
1. centos6.5
2. centos7.9
3. rocky8.9
4. rocky9.3

## 1. centos6.5
## 2. centos7.9
1. 网卡启停及重启
```
    systemctl enable NetworkManager     # 开机自启动
    systemctl disable NetworkManager    # 取消开机自启动
    systemctl status NetworkManager     # 查看状态
    systemctl restart NetworkManager    # 重启服务
    systemctl stop NetworkManager       # 停止服务
    systemctl start NetworkManager      # 启动服务
    systemctl status NetworkManager     # 查看状态
```
1. 网卡文件位置及内容更改
> /etc/sysconfig/network-scripts/ifcfg-*
#### 如下图为静态IP配置例子
![Alt text](image.png)
1. 启停防火墙


2. 防火墙文件位置及内容更改