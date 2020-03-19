#!/usr/bin/env python3
# coding=UTF-8

import yaml
import re
import fnmatch
import json
import requests
from difflib import SequenceMatcher
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from . import utils

class Url(object):
    def __init__(self, url=None):
        self.scheme = None
        self.netloc = None
        self.host = None
        self.path = None
        self.params = None
        self.query = None
        self.fragment = None
        self.query_dict = None
        if url:
            self.original_url = url
            self.parse_url()
            self.parse_query()

    def parse_url(self):
        u = urlparse(self.original_url)
        self.scheme = u.scheme
        self.netloc = u.netloc
        self.host = u.hostname
        self.path = u.path
        self.params = u.params
        self.query = u.query
        self.fragment = u.fragment
        return u

    def parse_query(self):
        self.query_dict = parse_qs(self.query)
        return self.query_dict

    def get_query_by_dict(self):
        return urlencode(self.query_dict, doseq=True)

    def get_url(self):
        self.query = self.get_query_by_dict()
        return urlunparse((self.scheme, self.netloc, self.path, self.params, self.query, self.fragment))

    def copy(self):
        return Url(self.get_url())


class Filter(object):
    def __init__(self, rule_file="rule.yaml", self_study=True):
        self.study = self_study
        self.rule_file = rule_file
        self.load_rule_file(rule_file)

    def load_rule_file(self, rule_filename):
        with open(rule_filename) as f:
            self.rules = yaml.safe_load(f)

    def reload_rule(self):
        self.load_rule_file(self.rule_file)

    def dump_rule_file(self, rule_filename):
        with open(rule_filename, 'w') as f:
            yaml.safe_dump(self.rules, f)

    def save_rule(self):
        self.dump_rule_file(self.rule_file)

    def add_to_rule(self, host, remove_list):
        if self.rules['hosts'].get(host):
            self.rules['hosts'].get(host)['query'] += remove_list
        else:
            self.rules['hosts'][host] = {"query": remove_list}

    def filter_url(self, url, mode=None):
        self.url = Url(url)

        if mode == "rule":
            self.filter_by_rule()
        elif mode == "auto":
            self.filter_auto()
        elif mode == "full":
            self.filter_by_rule()
            self.filter_auto()
        else:
            if not self.filter_by_rule():
                self.filter_auto()
        return self.url.get_url()

    def filter_by_rule(self):
        remove_list = []
        # 默认保留 fragment
        keep_fragment = True

        # 加载 基于 host 的规则 (wildcard)
        host_flag = False
        for host in self.rules.get("hosts"):
            if fnmatch.fnmatch(self.url.host, host):
                host_flag = True
                host_rules = self.rules["hosts"].get(host, {})
                remove_list = host_rules.get("query", [])
                keep_fragment = host_rules.get("fragment", [])
                break
        if not host_flag:
            remove_list = self.rules["default"]
        # 删除
        for k in remove_list:
            if self.url.query_dict.get(k):
                self.url.query_dict.pop(k)
        if not keep_fragment:
            self.url.fragment = None
        if self.url.get_url() == self.url.original_url:
            return False
        else:
            return True

    def filter_auto(self):
        content = utils.get_url_content(self.url.get_url())
        differ = SequenceMatcher()
        differ.set_seq1(content)
        # 依次删掉不必要的 query
        remove_list = []
        for k in self.url.query_dict:
            select_query_dict = self.url.query_dict.copy()
            select_query_dict.pop(k)
            select_url = self.url.copy()
            select_url.query_dict = select_query_dict
            select_content = utils.get_url_content(select_url.get_url())
            differ.set_seq2(select_content)
            if differ.ratio() > 0.5:
                remove_list.append(k)
        for k in remove_list:
            self.url.query_dict.pop(k)
        if self.study:
            self.add_to_rule(self.url.host, remove_list)
            self.save_rule()
            self.reload_rule()
        if self.url.get_url() == self.url.original_url:
            return False
        else:
            return True