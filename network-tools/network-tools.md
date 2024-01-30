# 常用网络工具

1. nc（ncat）

## 1. nc（ncat）

### 1.1 简介：ncat 网络实用程序取代了红帽企业 Linux 7 中的 netcat。ncat 是可靠的后端工具，可向其他应用和用户提供网络连接。它从命令行在网络上读取和写入数据，并使用传输控制协议(TCP)、用户数据报协议(UDP)、流控制传输协议(SCTP)或 Unix 套接字进行通信。ncat 可以处理 IPv4 和 IPv6、打开连接、发送数据包、执行端口扫描，并支持更高级别的功能，如 SSL 和连接代理

### 1.2 命令格式

> ncat [options] [hostname] [port]

### 1.3 常用参数

1. -4只能使用IPv4
2. -6只支持IPv6
3. -U，——unixsock只使用Unix域套接字
4. -C，——crlf对EOL序列使用crlf
5. -c，——sh-exec <command>通过/bin/sh执行给定的命令
6. -e，——exec <command>执行给定的命令