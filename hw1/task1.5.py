import subprocess

args = ['ping', 'yandex.ru']
ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in ping.stdout:
    print(line.decode('utf-8'))
