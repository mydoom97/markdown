# 重新加载防火墙


```shell
firewall-cmd --reload
```



# 开放端口

```shell
firewall-cmd --zone=public --add-port= #端口 /tcp --permanent
```