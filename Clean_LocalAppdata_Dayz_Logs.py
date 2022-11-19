# Author:GROOT aka XxToxicScriptxX

import subprocess
import os

Dayz_Dir = subprocess.check_output('echo %localappdata%/Dayz/',shell=True)

def clean_output(Dayz_Dir):
    Dayz_Dir = str(Dayz_Dir) #convert bytes output to string
    #clean the string for later use
    Dayz_Dir = Dayz_Dir.replace('\\\\','/')
    Dayz_Dir = Dayz_Dir.replace('\\r','')
    Dayz_Dir = Dayz_Dir.replace('b\'','')
    Dayz_Dir = Dayz_Dir.replace('\\n\'','')
    return Dayz_Dir


def remove_files(Dayz_Dir):

    for root, dirs, files in os.walk(Dayz_Dir, topdown=True):
        for name in files:
            if 'crash_' in name:
                file = os.path.join(root, name)

                if os.access(file, os.R_OK) is True:
                    print(f'[+] Read Access for : {file} [OK]')
                    if os.access(file, os.W_OK) is True:
                        print(f'[+] Write Access for : {file} [OK]')
                        print(f'Removing: {file}')
                        os.remove(file)
                    else:
                        if os.access(file, os.F_OK) is True:
                            print(f'[+] File Found: {file}')
                            print(f'You do not have Write access to: {file}')
                        else:
                            print(f'[!!] File not found by script: {file}')                   

            if '.mdmp' in name:
                file = os.path.join(root, name)
                if os.access(file, os.R_OK) is True:
                    print(f'[+] Read Access for : {file} [OK]')
                    if os.access(file, os.W_OK) is True:
                        print(f'[+] Write Access for : {file} [OK]')
                        print(f'Removing: {file}')
                        os.remove(file)
                    else:
                        if os.access(file, os.F_OK) is True:
                            print(f'[+]File Found: {file}')
                            print(f'You do not have Write access to: {file}')
                        else:
                            print(f'[!!] File not found by script: {file}')

            if 'script_' in name:
                file = os.path.join(root, name)
                if os.access(file, os.R_OK) is True:
                    print(f'[+] Read Access for : {file} [OK]')
                    if os.access(file, os.W_OK) is True:
                        print(f'[+] Write Access for : {file} [OK]')
                        print(f'Removing: {file}')
                        os.remove(file)
                    else:
                        if os.access(file, os.F_OK) is True:
                            print(f'[+]File Found: {file}')
                            print(f'You do not have Write access to: {file}')
                        else:
                            print(f'[!!] File not found by script: {file}')
            
            if 'Log' in name:
                file = os.path.join(root, name)
                if os.access(file, os.R_OK) is True:
                    print(f'[+] Read Access for : {file} [OK]')
                    if os.access(file, os.W_OK) is True:
                        print(f'[+] Write Access for : {file} [OK]')
                        print(f'Removing: {file}')
                        os.remove(file)
                    else:
                        if os.access(file, os.F_OK) is True:
                            print(f'[+]File Found: {file}')
                            print(f'You do not have Write access to: {file}')
                        else:
                            print(f'[!!] File not found by script: {file}')
            

Dayz_Dir = clean_output(Dayz_Dir)
print(f'Cleaning:[{Dayz_Dir}]')
remove_files(Dayz_Dir)
