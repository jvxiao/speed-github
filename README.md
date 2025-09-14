


<!-- </img> -->
<div align="center"> <img src="./img/logo.jpg" width="400px"></div>

<p align="center" style="padding:10px 6px">
  <img src="https://img.shields.io/badge/Windows-10-2376bc?style=plastic&logo=microsoft&logoColor=ffffff" />
   <img src="https://img.shields.io/badge/Python-3.11-2376bc?style=plastic&logo=microsoft&logoColor=ffffff" />
  <img src="https://img.shields.io/github/issues/jvxiao/speed-github.svg?color=F48D73" />
  <img src="https://img.shields.io/github/license/jvxiao/speed-github.svg?logo=github"
</p>

[中文](./README-Cn.md) &emsp; [English](./README.md)

# speed-github

A tool to solve the problem of slow loading and downloading speed of GitHub in the country.

## Reason for slow speed

CDN, Content Distribute Network, can be literally translated into content distribution network. CDN solves the problem of how to quickly and reliably deliver data from the source site to users.

When users obtain data, they do not need to obtain it directly from the source site. Through CDN's distribution of data, users can obtain data from a better server, thereby achieving fast access and reducing the load pressure on the source site.

For some reasons, Github is restricted in China. The main method is`DNS pollution`, which is to inject the wrong IP address of Github into the DNS server, thereby affecting user access.

## Solution

Resolve the GitHub-related domain name into the correct IP address, and then fill it into the local host file. When users visit GitHub, they will no longer resolve the IP address to the DNS server, but use the correct local IP address, which will not be affected by DNS pollution.

## Usage
>Tip: run with admin permission, because the `/etc/hosts` file need to be modified.

``` bash
# Download this repo to local
git clone https://github.com/jvxiao/speed-github.git
cd speed-github

# install dependencies
pip install -r requirements.txt

# run
python ./src/main.py
```

After doing this, copy the content `src/hosts` to update you hosts in `etc`, or you can just relace it. And then run the following command to update local DNS.
```
ipconfig /flushdns
```

**A more quick way**， run the folloing command, which will automaticlly do the all thing for you.

```
python src/main.py -w
# or 
python src/main.py --writehosts
```
## github-hosts

After executing the above command, your hosts file will add the following content,and then automatically refresh the local DNS.

Or you can choose to copy the following content into your hosts file, and manually refresh local DNS with  `ipconfig /flushdns`

```
# Gennerate by Speed-github
185.199.111.154                github.githubassets.com
140.82.113.21                  central.github.com
185.199.111.133                desktop.githubusercontent.com
185.199.108.133                camo.githubusercontent.com
185.199.108.133                github.map.fastly.net
146.75.77.194                  github.global.ssl.fastly.net
140.82.113.4                   gist.github.com
185.199.108.153                github.io
140.82.113.4                   github.com
140.82.113.6                   api.github.com
185.199.109.133                raw.githubusercontent.com
185.199.111.133                user-images.githubusercontent.com
185.199.108.133                favicons.githubusercontent.com
185.199.108.133                avatars5.githubusercontent.com
185.199.108.133                avatars4.githubusercontent.com
185.199.111.133                avatars3.githubusercontent.com
185.199.108.133                avatars2.githubusercontent.com
185.199.108.133                avatars1.githubusercontent.com
185.199.108.133                avatars0.githubusercontent.com
185.199.108.133                avatars.githubusercontent.com
140.82.114.10                  codeload.github.com
52.216.50.73                   github-cloud.s3.amazonaws.com
52.217.117.113                 github-com.s3.amazonaws.com
16.15.195.104                  github-production-release-asset-2e65be.s3.amazonaws.com
16.182.67.49                   github-production-user-asset-6210df.s3.amazonaws.com
3.5.29.99                      github-production-repository-file-5c1aeb.s3.amazonaws.com
185.199.108.153                githubstatus.com
140.82.113.17                  github.community
185.199.108.133                media.githubusercontent.com


# Last modified 2025-09-14 11:02:16
# Star repo at https://github.com/jvxiao/speed-github
```

## Sponsor me

If you like this project, or if it helps you, please consider buying the author a cup of coffee :coffee:

<img src="https://image.baidu.com/search/down?url=http://tvax2.sinaimg.cn/mw690/0071fJItgy1i1vlvailptj30ih0h80wf.jpg" style="width:300px">
