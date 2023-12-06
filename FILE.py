import os,time,platform
os.system('pip uninstall requests -y');os.system('pip install requests')
bit = platform.architecture()[0]
if bit=='64bit':
    import abir404
else:
    print('\033[1;31m[×] Sorry your Device 32 bit Not Support')
