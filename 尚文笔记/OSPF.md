#   OSPF：开放最短路径优先协议（Open Shortest Path First）是IETF组织开发的的基于链路状态的内部网关协议（IGP）
## 动态路由协议
-   IGP：内部网关协议（Interior Gateway Protocol）
    -   OSPF：开放最短路径优先协议（Open Shortest Path First）
    -   IS-IS：中间系统到中间系统（Intermediate System to Intermediate System）
    -   EIGRP：增强型内部网关路由协议（Enhanced Interior Gateway Routing Protocol）
-   EGP：外部网关协议（External Gateway Protocol）
    -   BGP：边界网关协议（Border Gateway Protocol）


## OSPF协议基本概念
-   专为TCP/IP网络设计，支持VLSM，路由汇总，支持认证，支持区域划分，支持层次化路由结构
    -   VLSM：可变长子网掩码（Variable Length Subnet Mask），允许子网掩码长度可变。VLSM可以更有效地利用IP地址空间，减少路由表的大小，提高网络性能。分地址避免浪费，等价负载均衡
    -   区域划分：产生LSA（Link State Advertisement，链路状态公告），减少LSA泛洪范围，减少路由器负担，提高网络性能。适应大型网络 
-   在RGOS平台上，管理距离为***110***
-   封装在报文中，IP协议号为***89***
-   具备无环路，快速收敛，扩展性好
    -   无环路：计算最短路径树，避免环路
    -   收敛：当网络拓扑发生变化时，OSPF协议能够快速地计算出新的路由，并且将新的路由信息广播给网络中的其他路由器。这可以确保网络中的路由器始终拥有最新的路由信息，从而保证网络的稳定性和可靠性。
## OSPF的开销值（cost）：100M/带宽
-    带宽越大，开销值越小
    -    解决方法：修改带宽值，修改开销值
        1.   修改带宽值
            >   router ospf 1
            >   auto-cost reference-bandwidth 1000000
        2.   修改开销值
            >   interface GigabitEthernet0/0/0
            >   ip ospf cost 1

## OSPF邻居关系建立：两台运行OSPF协议的路由器，项链的接口上会相互各自参数，若双方参数符合条件则建立关系
### 建立过程：
    1. 发现：通过Hello报文发现邻居，Hello报文周期性发送
    2. 建立邻居表
        - 参数匹配
        -         
    3. 交换LSA
    4. LSDB（全网LSA建立的数据库）
    5. 路由表      

## OSPF邻接关系建立：邻居不一定邻接，已经完成双方参数交换。

## DR和BDR：DR（Designated Router，指定路由器）和BDR（Backup Designated Router，备份指定路由器）

## Router-ID：路由器标识符，唯一标识一台路由器
-   手动配置
-   自动配置
    -   loockup interface：若未配置Router-ID，则自动选择物理接口中IP地址最大的作为Router-ID
    -   物理接口中


#   配置命令：
##   1.   配置lockup接口IP地址：
    

```

ruijie(config)#interface loopback 0
ruijie(config-if)#ip address 1.1.1.1 32
ruijie(config-if)#exit
```

## 2.  OSPF下发默认路由：
```
ruijie(config)#router ospf 1
ruijie(config-router)#default-information originate
```


