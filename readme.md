# Clear Url

[en](./readme_en.md)

删除URL中的跟踪参数

`python3 main.py https://xxxxx`

# Rule

```
host: # 正则匹配host
  path: # 正则匹配path
    query: # 需要删除的列表
      - xxx
      - xxx
    fragment: false # 是否保留fragment
```

例子

```
"www\\.douban\\.com":
  ".*":
    query:
      - source
      - dt_dapp
    fragment: false
```

# More

https://github.com/jparise/chrome-utm-stripper

[分享更清爽的链接，可以试试这个 Android 小工具：清净分享 | App+1](https://sspai.com/post/45317)

[ClearURLs – 自动删除 URL 中跟踪字段[Chrome/Firefox]](https://www.appinn.com/clearurls-for-chrome-and-firefox/)

[【小书签】链接地址强力净化:sparkling_heart:与油猴脚本同步更新](https://meta.appinn.net/t/topic/3130)

[[Chrome/Firefox 扩展] Neat URL - 净化链接无用参数](https://meta.appinn.net/t/topic/6690)