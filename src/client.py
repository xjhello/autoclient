import json
import os

import requests
from src.plugins import Plugins
from lib.conf.config import setting


# 收集收集,然后发送数据
class Base(object):
    def post_data(self, server_info):
        # server_info发送post请求给API
        # requests.post(setting.API_URL, json=server_info)  # 真实地址
        print('模拟发送post\n', json.dumps(server_info))
        # requests.post('http://localhost:8000/api/', json=server_info)


class Agent(Base):
    def collect(self):
        server_info = Plugins().execute()
        #  Agent模式防止主机名被改，然后存下
        hostname = server_info['basic']['data']['hostname']
        res = open(os.path.join(setting.BASEDIR, 'config/cert'), 'r', encoding='utf-8').read()
        # 如果没有值说明空，要录入数据
        if not res.strip():
            with open(os.path.join(setting.BASEDIR, 'config/cert'), 'w', encoding='utf-8') as fp:
                fp.write(hostname)
        else:
            server_info['basic']['data']['hostname'] = res

        # for k, v in server_info.items():
        #     print(k, v)
        self.post_data(server_info)


class SSHSalt(Base):
    def get_hostnames(self):
        # 从API请求到主机列表
        hostnames = 'test'
        # hostnames = requests.get(setting.API_URL)
        return ['10.0.0.100', '10.0.0.200']

    def run(self, hostname):
        server_info = Plugins(hostname).execute()
        self.post_data(server_info)

    def collect(self):
        hostnames = self.get_hostnames()
        # 线程池执行
        from concurrent.futures import ThreadPoolExecutor
        p = ThreadPoolExecutor(10)
        for hostname in hostnames:
            p.submit(self.run, hostname)
