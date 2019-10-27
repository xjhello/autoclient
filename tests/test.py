####### 1.agent执行脚本
# import  subprocess
# res = subprocess.getoutput('ipconfig')
# print(res[5:6])
#
# # request模块
# import requests
# res = requests.post('http://127.0.0.1:8000/asset/', data={"ip":res[5:6]})

###### 2.ssh类 paramiko模块
import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.0.0.100', port=22, username='root', password='1')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ifconfig')
# 获取命令结果
result = stdout.read()
print(result)
# 关闭连接
ssh.close()




