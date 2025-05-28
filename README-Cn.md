
<div align="center"> <img src="./img/logo.jpg" width="400px"></div>

<p align="center" style="padding:10px 6px">
  <img src="https://img.shields.io/badge/Windows-10-2376bc?style=plastic&logo=microsoft&logoColor=ffffff" />
   <img src="https://img.shields.io/badge/Python-3.11-2376bc?style=plastic&logo=microsoft&logoColor=ffffff" />
  <img src="https://img.shields.io/github/issues/jvxiao/speed-github.svg?color=F48D73" />
  <img src="https://img.shields.io/github/license/jvxiao/speed-github.svg?logo=github"
</p>

[中文](./README-Cn.md) &emsp; [English](./README.md)

# speed-github

一个解决github在国内加载和下载速度慢问题的工具

### 速度慢原因

CDN，Content Distribute Network，可以直译成内容分发网络，CDN解决的是如何将数据快速可靠从源站传递到用户的问题。

用户获取数据时，不需要直接从源站获取，通过CDN对于数据的分发，用户可以从一个较优的服务器获取数据，从而达到快速访问，并减少源站负载压力的目的。

处于某些原因的考虑，Github在国内被限制的访问。其手段主要是通过DNS污染，就是通过向DNS服务器其中注入github错误的IP地址，从而影响用户访问。


### 如何解决

将github相关的域名解析成正确的ip, 然后填入本地的host文件中。当用户访问github时就不会再从DNS服务器解析ip, 而是使用本地的正确ip，也就不受DNS污染影响。


## 使用
> Tip: 用管理员（admin)权限运行下面的命令，因为需要对`/etc/hosts`文件做修改

``` bash
# 下载仓库到本地
git clone https://github.com/jvxiao/speed-github.git
cd speed-github

# 安装依赖
pip install -r requirements.txt

# 执行脚本
python ./src/main.py

```

执行上述命令后，您的 hosts 文件将添加以下内容，并自动刷新本地 DNS。

您也可以选择将以下内容复制到 hosts 文件中，然后使用“ipconfig /flushdns”手动刷新本地 DNS。

**一个更快的方式** 是直接运行下面的命令，它会自动更新`hosts`文件并且刷新本地DNS

```
python src/main.py -w
# 或者
python src/main.py --writehosts
```

## github-hosts

```
# Gennerate by Speed-github
185.199.110.154                github.githubassets.com
140.82.113.21                  central.github.com
185.199.108.133                desktop.githubusercontent.com
185.199.108.133                camo.githubusercontent.com
185.199.108.133                github.map.fastly.net
146.75.29.194                  github.global.ssl.fastly.net
140.82.112.4                   gist.github.com
185.199.109.153                github.io
140.82.112.4                   github.com
140.82.114.6                   api.github.com
185.199.111.133                raw.githubusercontent.com
185.199.109.133                user-images.githubusercontent.com
185.199.111.133                favicons.githubusercontent.com
185.199.108.133                avatars5.githubusercontent.com
185.199.108.133                avatars4.githubusercontent.com
185.199.110.133                avatars3.githubusercontent.com
185.199.108.133                avatars2.githubusercontent.com
185.199.108.133                avatars1.githubusercontent.com
185.199.108.133                avatars0.githubusercontent.com
185.199.111.133                avatars.githubusercontent.com
140.82.112.9                   codeload.github.com
52.216.184.195                 github-cloud.s3.amazonaws.com
3.5.30.165                     github-com.s3.amazonaws.com
16.15.217.215                  github-production-release-asset-2e65be.s3.amazonaws.com
54.231.226.25                  github-production-user-asset-6210df.s3.amazonaws.com
3.5.13.29                      github-production-repository-file-5c1aeb.s3.amazonaws.com
185.199.108.153                githubstatus.com
140.82.112.17                  github.community
185.199.108.133                media.githubusercontent.com


# Last modified 2025-05-16 18:21:39
# Star repo at https://github.com/jvxiao/speed-github
```



### 关于

该项目从第一次发布之后到这一次更新，隔了有好几年的时间，未来该项目将会持续更新。后续在使用过程中，如果有什么问题，欢迎提issue，我也会及时跟进。

## 赞赏 

如果你喜欢该项目，或者该项目有帮助到你，考虑请作者喝一杯咖啡吧 :coffee:

<img src="https://image.baidu.com/search/down?url=http://tvax2.sinaimg.cn/mw690/0071fJItgy1i1vlvailptj30ih0h80wf.jpg" style="width:300px">
<!-- ![赞赏](https://image.baidu.com/search/down?url=http://tvax2.sinaimg.cn/mw690/0071fJItgy1i1vlvailptj30ih0h80wf.jpg) -->