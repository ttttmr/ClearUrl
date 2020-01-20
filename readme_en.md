# Clear Url

[zh](./readme.md)

remove tracking from url query strings

# Rule

```
host: regex match host
  path: # regex match path
    query: # remove query list
      - xxx
      - xxx
    fragment: false # keep fragment
```

Example

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

[去除淘宝链接 SPM (Beta)](https://greasyfork.org/zh-CN/scripts/373176-%E5%8E%BB%E9%99%A4%E6%B7%98%E5%AE%9D%E9%93%BE%E6%8E%A5-spm-beta)

[链接精简](https://greasyfork.org/zh-CN/scripts/29788-%E9%93%BE%E6%8E%A5%E7%B2%BE%E7%AE%80/code)