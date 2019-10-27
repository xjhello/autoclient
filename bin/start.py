import os
import sys
os.environ['CUSTOM_CONF'] = 'config.settings'  # 定义环境变量指定配置文件路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from src.script import run

if __name__ == '__main__':
    run()

