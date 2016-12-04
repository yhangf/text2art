# gctag: 网页及本地标签云生成工具
```
                    ___                        
                   (   )                       
  .--.     .--.     | |_       .---.    .--.   
 /    \   /    \   (   __)    / .-, \  /    \  
;  ,-. ' |  .-. ;   | |      (__) ; | ;  ,-. '
| |  | | |  |(___)  | | ___    .'`  | | |  | |
| |  | | |  |       | |(   )  / .'| | | |  | |
| |  | | |  | ___   | | | |  | /  | | | |  | |
| '  | | |  '(   )  | ' | |  ; |  ; | | '  | |
'  `-' | '  `-' |   ' `-' ;  ' `-'  | '  `-' |
 `.__. |  `.__,'     `.__.   `.__.'_.  `.__. |
 ( `-' ;                               ( `-' ;
  `.__.                                 `.__.  


                            --------- by Yanghangfeng
```

#### 1.把仓库克隆到本地
```
>>> git clone https://github.com/Fenghuapiao/gctag.git
```
#### 2.安装依赖文件
* 方法一
```
>>> pip install -r requirements.txt
```
* 方法二(推荐)

如果方法一安装失败，可以在这个[网站下载](http://www.lfd.uci.edu/~gohlke/pythonlibs/)相应的.whl包,然后pip安装即可
```
>>> pip install wheel
```
##### 请注意！！！一定要在.whl文件目录里打开命令行窗口
```
>>> pip install 下载文件名.whl
```
#### 3.参数介绍
- `--url`:待画网页的url， 默认为`None`
- `--input`:本地待画的文本文件路径
- `--output`:生成的图片保存形式(可选参数，默认为运行文件的根目录且为wordcloud.jpg)
- `--model`:生成图片的形式(可选参数，自定义图片mask)
- `--ttf`:标签云中的字体格式(可选参数)
- `--width`:生成图片的宽度(可选参数，默认为1800)
- `--height`:生成图片的高度(可选参数，默认为1000)
- `--bg`:生成图片的背景颜色(可选参数，black or white，默认为black)
- `--margin`:生成图片中文字的边距(可选参数，默认为5)

说明: `--url`,`--input`参数必选其一

#### 4.使用方法
##### 4-1. 在线获取网页并生成标签云
```
>>> python gctag.py --url https://www.douban.com/note/591278881/ --output ./douban.jpg --bg white --ttf ./font/叶立群几何体.ttf
```
* 结果一:
![](https://github.com/Fenghuapiao/gctag/blob/master/example/douban_your_name3.jpg)

```
>>> python gctag.py --url https://www.douban.com/note/591278881/ --output ./douban_your_name2.jpg --bg white --ttf ./font/奇思_奔跑吧电影.ttf
```
* 结果二:
![](https://github.com/Fenghuapiao/gctag/blob/master/example/douban_your_name2.jpg)

##### 4-2.利用本地文件生成标签云
```
>>> python gctag.py --input ./test.txt --output ./js.jpg --bg white --ttf ./font/李旭科漫画体v1.0.ttf
```

* 结果三:
![](https://github.com/Fenghuapiao/gctag/blob/master/example/js.jpg)

以alice_mask.png为模板生成标签云
```
>>> python gctag.py --input ./alice.txt --model ./alice_mask.png --bg white --output ./alice.jpg
```
![alice_mask.png](https://github.com/Fenghuapiao/gctag/blob/master/example/alice_mask.png)
* 结果四:
![](https://github.com/Fenghuapiao/gctag/blob/master/example/alice_white.jpg)

#### 5.LICENSE
[MIT](https://github.com/Fenghuapiao/gctag/blob/master/LICENSE)
