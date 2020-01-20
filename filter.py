#!/usr/bin/env python3
# coding=UTF-8

import yaml
import re
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

def filter_url(url):
    u = urlparse(url)
    query_dict, keep_fragment = filter_by_rule(u.hostname, u.path, parse_qs(u.query))
    query = urlencode(query_dict, doseq=True)
    return urlunparse((u.scheme, u.netloc, u.path, u.params, query, u.fragment if keep_fragment else None))


def filter_by_rule(host, path, query_dict):
    with open("rule.yaml") as f:
        rules = yaml.safe_load(f)

    remove_list = []
    # 默认保留 fragment
    keep_fragment = True

    # 加载 基于 host 的规则
    for host_rule in rules:
        if re.match(host_rule, host):
            # 加载 基于 path 的规则
            path_rules = rules.get(host_rule,[])
            for path_rule in path_rules:
                if re.match(path_rule, path):
                    if path_rules.get(path_rule,[]):
                        remove_list += path_rules[path_rule].get("query",[])
                        keep_fragment = path_rules[path_rule].get("fragment",True)
                        break
            break

    for k in remove_list:
        if query_dict.get(k):
            query_dict.pop(k)
    return query_dict, keep_fragment