# 自定义的配置文件
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODE = 'agent'  # agent(第一种方案) ssh(第二种方案) salt(第三中)

SSH_USER = 'root'
SSH_PWD = 'xujianzq123'
SSH_PORT = 22
SSH_KEY = 'private文件的路径'

DEBUG = False


PLUGINS_DICT = {
    'basic': 'src.plugins.basic.Basic',
    'cpu': 'src.plugins.cpu.Cpu',
    'disk': 'src.plugins.disk.Disk',
    'memory': 'src.plugins.memory.Memory',
    'nic': 'src.plugins.nic.Nic',
    'board': 'src.plugins.board.Board',
}
