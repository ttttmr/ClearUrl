from filter import filter_url


def test_filter_url():
    # douban
    assert filter_url("https://www.douban.com/annual/2019?source=broadcast&dt_dapp=1") == "https://www.douban.com/annual/2019"
    assert filter_url("https://movie.douban.com/annual/2019?source=broadcast&dt_dapp=1") == "https://movie.douban.com/annual/2019"
    assert filter_url("https://www.douban.com/annual/2019#test") == "https://www.douban.com/annual/2019"
    # twitter
    assert filter_url("https://twitter.com/gentilkiwi/status/1217731204373499904?s=12") == "https://twitter.com/gentilkiwi/status/1217731204373499904"
    # bilibili
    assert filter_url("https://m.bilibili.com/bangumi/play/ep285192?share_source=more&share_medium=ipad&bbid=Z442BB442087877E463990432E2A2E386DE0&ts=1575632820") == "https://m.bilibili.com/bangumi/play/ep285192"
    assert filter_url("https://www.bilibili.com/bangumi/play/ep285192?share_source=more&share_medium=ipad&bbid=Z442BB442087877E463990432E2A2E386DE0&ts=1575632820") == "https://www.bilibili.com/bangumi/play/ep285192"
    # default
    assert filter_url("http://test.com/index.php?utm_social=test") == "http://test.com/index.php"