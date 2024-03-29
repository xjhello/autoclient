#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from lib.conf.config import setting


class Board(object):
    def __init__(self):
        pass

    @classmethod
    def initial(cls):
        return cls()

    def process(self, command_func, debug):
        if debug:
            output = open(os.path.join(setting.BASEDIR, 'files/board.out'), 'r', encoding='utf-8').read()
        else:
            output = command_func("sudo dmidecode -t1")
        return self.parse(output)

    def parse(self, content):

        result = {}
        key_map = {
            'Manufacturer': 'manufacturer',
            'Product Name': 'model',
            'Serial Number': 'sn',
        }

        for item in content.split('\n'):
            row_data = item.strip().split(':')
            if len(row_data) == 2:
                if row_data[0] in key_map:
                    result[key_map[row_data[0]]] = row_data[1].strip() if row_data[1] else row_data[1]

        return result
