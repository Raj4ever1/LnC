import os
for root,folders,files in os.walk('.'):
    for folder in folders:
        if 'pycache' in folder:
            path = root[2:] + '\\' + folder
            print(path)
            os.system('git rm -r --cached {}'.format(path))