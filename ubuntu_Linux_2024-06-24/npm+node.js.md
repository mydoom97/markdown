## 1.更新npm和node

###  使用 nvm（Node Version Manager）

1. #### 安装

[https://github.com/nvm-sh/nvm](https://github.com/nvm-sh/nvm "https://github.com/nvm-sh/nvm")

> **~~*==安装后重开终端或添加环境变量重启等使其生效==*~~**

  下载脚本install.sh运行进行安装

2. #### 安装最新版本node

```shell
nvm install node
```

3. #### 使用最新版本node

```shell
nvm use node
```

4. #### 更新npm

```shell
nvm install --latest-npm
npm install -g npm@latest
```