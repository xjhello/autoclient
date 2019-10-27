from lib.conf.config import setting
import importlib
import traceback


# 收集执行对象，可动态加载插件
class Plugins(object):
    def __init__(self, hostname=None):
        self.hostname = hostname
        self.plugins_dict = setting.PLUGINS_DICT
        self.mode = setting.MODE
        if self.mode == 'ssh':
            self.ssh_user = setting.SSH_USER
            self.ssh_port = setting.SSH_PORT
            self.ssh_pwd = setting.SSH_PWD
            self.ssh_key = setting.SSH_KEY

    def execute(self):
        # 1.循环从配置文件里面取出插件配置  'basic': 'src.plugins.basic.Basic',
        response = {}
        for k, v in self.plugins_dict.items():
            ret = {"status":None, "data":None}
            try:
                moudle_name, class_name = v.rsplit('.',1)
                # 2. 导入文件的类 (Basic类)
                m = importlib.import_module(moudle_name)
                if hasattr(m, class_name):
                    cls = getattr(m,class_name)
                    # 3. 执行下面的process方法 插件的方法在这里提供_cmd_run
                    res = cls().process(self._cmd_run, setting.DEBUG)
                    ret['status'] = 10000
                    ret['data'] = res
            except Exception as e:
                ret['status'] = 100001
                ret['data'] = "[%s] 采集 [%s] 出错, 错误信息是: %s" % (self.hostname if self.hostname else "Agent", k, str(traceback.format_exc()) )
            response[k] = ret
        return response

    def _cmd_run(self, cmd):
        if self.mode == 'agent':
            return self.__agent_run(cmd)
        elif self.mode == 'ssh':
            return self.__ssh_run(cmd)
        elif self.mode == 'salt':
            return self.__salt_run(cmd)
        else:
            print('现在只支持agent/ssh/salt模式')

    def __agent_run(self, cmd):
        import subprocess
        res = subprocess.getoutput(cmd)
        return res

    def __ssh_run(self,cmd):
        import paramiko
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=self.hostname, port=self.ssh_port, username=self.ssh_user, password=self.ssh_pwd)
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # 获取命令结果
        result = stdout.read()
        print(result)
        # 关闭连接
        ssh.close()

    def __salt_run(self,cmd):
        import subprocess
        cmd = 'salt "%s" cmd.run "%s"' % (self.hostname, cmd)
        res = subprocess.getoutput(cmd)
        return res