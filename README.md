### 项目说明

本项目采集后的直播源是txt形式的，可以用于DIYP直播这个软件的直播源。

### 项目简介

项目地址：[https://github.com/06yanm/TvSources](https://github.com/06yanm/TvSources)

项目中的采集代码位于master分支下的code文件夹

本项目是一个从网络上多个存储直播源地址的网站获取直播源，之后进行二次核验（验证源是否可用）的项目。

本项目有python编写，并且已经部署在github Actions上，因此小白可以直接使用以下直播源地址填入  ***DIYP影视***   这个软件。

ipv4源（第一个源只有央视频道和地方频道）：

```
http://06yanm.github.io/TvSources/code/ipv4normal.txt
http://06yanm.github.io/TvSourcescode/ipv4.txt
```

ipv6源（由于githubAction不能访问ipv6，暂停提供）（第一个源只有央视频道和地方频道）：

```
http://06yanm.github.io/TvSources/code/ipv6normal.txt
http://06yanm.github.io/TvSources/code/ipv6.txt
```

### 项目文件介绍

> **update.py**
>
> 采集程序代码，负责从urls.txt中获取已经有了源合集的源地址里面筛选最新可用的电视直播源，并对存储的直播源进行更新。
>
> （本站已经设置了每3天自动执行一次本代码）

> **ipv4.txt 和 ipv6.txt**
>
> 存储了已经筛选出来的成品直播源，根据需求选择使用ipv4直播源地址和ipv6直播源地址

> **ipv4normal.txt 和 ipv6normal.txt**
>
> 只包含 *央视频道和地方卫视频道* 的ipv4和ipv6直播源

> **urls.txt**
>
> 存储爬取源地址的文件（即目标合集地址）

> **program.txt**
>
> 这个文件里面包含的频道名称会被用来筛选，最后得出ipv4normal.txt和ipv6normal.txt
