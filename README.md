# speed-github
一键解决github在国内加载和下载速度慢的问题


### 速度慢原因


CDN，Content Distribute Network，可以直译成内容分发网络，CDN解决的是如何将数据快速可靠从源站传递到用户的问题。用户获取数据时，不需要直接从源站获取，通过CDN对于数据的分发，用户可以从一个较优的服务器获取数据，从而达到快速访问，并减少源站负载压力的目的。

但是GitHub的CDN被某墙屏了，由于网络代理商的原因，所以访问下载很慢。




### 实现原理
直接获取ip地址并绑定本地host，绕过DNS解析。通过脚本获取下列网址ip
<pre>
<code>
	github.com
	github.global.ssl.fastly.net
	assets-cdn.github.com
	documentcloud.github.com
	gist.github.com
	help.github.com
	nodeload.github.com
	raw.github.com
	status.github.com
	training.github.com
	ithubusercontent.com
	avatars1.githubusercontent.com
	codeload.github.com
</code>
</pre>

将获取的ip与对应的网址填入host文件中，然后刷新本地DNS.


### 运行环境

- python3+
- 依赖库
	- BeautifulSoup
	- requests
	- shutil

### 使用方式
 


1. 用记事本或notepad++打开startFly.bat文件，将 var变量值改成你自己存放该项目的地址
2. 右键点击startFly.bat, 以管理员身份运行

### 效果图
![Ok啦](https://github.com/jvxiao/speed-github/blob/master/img/screenShot.PNG)
