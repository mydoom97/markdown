#   DHCP在应用层
#   DHCP工作过程：
1.  客户端广播DHCP discover报文，寻找DHCP服务器
2.  DHCP服务器单播客户端DHCP offer报文，提供IP地址。携带IP地址租约时间、子网掩码、网关、DNS等信息
3.  客户端广播DHCP request报文，选择IP地址。向服务器确认使用的IP，携带主备DHCP服务器的IP地址，续租时间等信息
4.  DHCP服务器单播DHCP ack报文，确认IP地址

>   续租：单播DHCP request报文，携带续租时间。二次续租：广播DHCP request报文，携带续租时间。二次续租重绑定：重新更改绑定信息

>   DHCP先到原则，ARP后到，MAC地址表后到  

#   DHCP报文：
1. DHCP discover：客户端广播DHCP discover报文，寻找DHCP服务器
2.  DHCP offer：
3.  DHCP request
4.  DHCP ack
5.  DHCP release：客户端广播DHCP release报文，释放IP地址
6.  DHCP decline：客户端广播DHCP decline报文，通知DHCP服务器IP被占用
7.  DHCP inform：客户端单播DHCP inform报文，客户端有IP，请求更详细的信息
8.  DHCP nak：DHCP服务器单播DHCP nak报文，拒绝续租IP地址
9.  


#   DHCP中继代理：
部署方式：
1.  网关交换机作为DHCP
2.  网关交换机作为DHCP中继代理，在服务器区部署专用DHCP服务器。汇聚交换机与DHCP之间广播变单播跨广播域发送。

- 位置：网关，网关要开DHCP
- 网关与DHCP保持通信
- 中继设备开DHCP服务  

#   安全问题：
1. 用户使用静态IP地址接入
2. 用户架设非法DHCP服务器

   防范：DHCP Snooping：信任接口，非信任接口，信任接口上配置DHCP Snooping，非信任接口上配置DHCP Snooping和IP Source Guard。交换机开启DHCP snooping后，全部接口默认为非信任接口，只需要将需要信任的接口配置为信任接口即可。生成绑定表，绑定表中的MAC地址和IP地址的对应关系，只有绑定表中的MAC地址和IP地址的对应关系才能通过交换机。

# 命令
ruiejie(config)#server dhcp

ruiejie(config)#ip dhcp pool 1

ruiejie(dhcp-config)#network 192.168.1.0 255.255.255.0

ruiejie(dhcp-config)#default-router 192.168.1.1

ruiejie(dhcp-config)#dns-server 8.8.8.8





排除IP地址：

ruiejie(dhcp-config)#excluded-address 192.168.1.1 192.168.1.100





在端口中获取IP地址

ruiejie(config)#interface fastEthernet 0/0

ruiejie(config-if)#ip address dhcp



