"""
██████╗░███████╗███╗░░██╗████████╗░█████╗░
██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔══██╗
██████╔╝█████╗░░██╔██╗██║░░░██║░░░███████║
██╔═══╝░██╔══╝░░██║╚████║░░░██║░░░██╔══██║
██║░░░░░███████╗██║░╚███║░░░██║░░░██║░░██║
╚═╝░░░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝
©Justaus3r 2021
Distributed under GPLV3
  This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os #for os thingis
from rich import print #for print beauty like pico sama
from rich.markdown import Markdown #for printing mardown
from clear_screen import clear #to clear screen
import sys #for system thingis
import stat #dunno,used it somewhere
import shlex # for spliting system commands and converting it onto list for subprocess
import subprocess # for system commands
import platform # for platform and other system info
import psutil # system info
import socket # for ping or other network thingis
import getmac #for getting mac
import shutil # for system info
import ctypes #for windows to play with.used to change title
from distutils.dir_util import copy_tree #for copying dirs 
from datetime import datetime #date and time
import signal # forgot
from tkinter import * # for some gui
from rich.console import Console # for importing console
from rich.table import Table #for tables
import pytube #for downloading vids from youthoob 
import requests # for downloading files from server
from tqdm import trange #for progress bar
#from now on usin prompt_toolkit for userinput
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
import seedir as sdir #for directory tree view
######Created an Class for Downloading files,might need it in future########
class DownloadFile:
    def __init__(self,url,filename):
        self.url = url
        self.filename = filename

    def Download(self):
        print("[green]Getting Meta Data from the server[/green]")
        try:
            metafile = requests.get(self.url, stream=True)
            print("[green]Server status code:[/green]",metafile.status_code)
            print("[green]Content Type:[/green]",metafile.headers['content-type'])
            print("[green]Encoding[/green]",metafile.encoding)        
            print(f"[purple]Downloading File from {self.url}[/purple]")
        except:
            print("An Error Occured while receiving headers")    
        #create an object that get the data in binary form
        for i in trange(1):
            thefile = requests.get(self.url)
        #write the data as binary
        with open(self.filename,"wb") as File:
            File.write(thefile.content)
            File.close()
        print("The file has been downloaded")
########################################################

#define a function to check os
def check_onichans_os():
  if os.name == 'nt':
     Os = 'Win'
     return Os
  Os = 'linux'
  return Os
#~VERSION AND BUILD DATE-----------------
_VER = "1.3.0"
_BULD_DATE = "1-June-2021"
# Func to check if the current directory is a git directory
def if_git_dir():
    if os.path.exists('.git'):
        return '[git]'
    else:
        return ''

#~PROGRAM STARTING/boot DIRECTORY
_prg_start_dir = os.getcwd()

 #######################################################################################################################################
#check the config file to see if the banner is to printed 
try:
    if check_onichans_os() == 'linux':     
        with open("configs/Bannerconfs/bannerbool","r") as bannerbool:
         Bool_value = bannerbool.read()
         bannerbool.close()
    else:
         with open("configs\\Bannerconfs\\bannerbool","r") as bannerbool:
             Bool_value = bannerbool.read()
             bannerbool.close()
except OSError as err:
    print("[red]%s[/red]"%err)         
#print banner if bool value is 1 otherwise continue
try:
 if Bool_value == '1':
     try:
         if check_onichans_os() == 'linux':
             with open("configs/Bannerconfs/banner","r") as banner:
                 Banner = banner.read()
                 print(Banner)
                 banner.close()
         else:
             with open("configs\\Bannerconfs\\banner","r") as banner:
                 Banner = banner.read()
                 print(Banner)
                 banner.close()                                  
     except OSError as err:
         print("[red]%s[/red]"%err)  
except NameError:
        print("[red]Configuration file Error[/red]")
#####################################################################
    #prompt
    # check the configuration file to see if custom prompt is to be printed
    #CHECK OS
if check_onichans_os() == 'linux':
    #Try and see if the configuration file(to print custom prompt) exists,if not throw an error and exit
    try:
        with open("configs/prompt/promptconf","r") as promptconf:
            _read_conf = promptconf.read()
            promptconf.close() 
    except FileNotFoundError:
        print("[red]Configuration file missing![/red]")
        sys.exit(1)                
    if _read_conf == '1':
        #Try and see if the prompt file exist,if not throw an error
        try:
            with open("configs/prompt/prompt","r") as promptfile:
                __prompt = promptfile.read()
                __prompt__cwd = False
        except FileNotFoundError:
            print("[red]Prompt file not found![/red]")
            choice = input("Do you want to create a prompt file[Y/N]:")
            if choice.upper() == 'Y':
                prompt = input("Type your custom prompt:")
                try:
                    with open("configs/prompt/prompt","w") as make_prompt_file:
                        make_prompt_file.write(prompt)
                        make_prompt_file.close()
                        print("Prompt file created successfully!,Restart the shell to take effect")
                        sys.exit(0)
                except OSError as err:
                    print("[red]%s[/red]"%err)
            else:
                print("[red]Please create a prompt file in configs/prompt/ \nor change the configuration file(i.e:configs/prompt/promptconf) from 1 to 0[/red]")
                sys.exit(1)                    
    else:
        __prompt__cwd = True                      
else:
    try:
        with open("configs\\prompt\\promptconf","r") as promptconf:
            _read_conf = promptconf.read()
            promptconf.close() 
    except FileNotFoundError:
        print("[red]Configuration file missing![/red]")
        sys.exit(1)                
    if _read_conf == '1':
        #Try and see if the prompt file exist.if the prompt file exists,read data from it and turn the __prompt__cwd bool to false as we dont want to print current directory as prompt.if not throw an error
        try:
            with open("configs\\prompt\\prompt","r") as promptfile:
                __prompt = promptfile.read()
                __prompt__cwd = False
        except FileNotFoundError:
            print("[red]Prompt file not found![/red]")
            choice = input("Do you want to create a prompt file[Y/N]:")
            if choice.upper() == 'Y':
                prompt = input("Type your custom prompt:")
                try:
                    with open("configs\\prompt\\prompt","w") as make_prompt_file:
                        make_prompt_file.write(prompt)
                        make_prompt_file.close()
                        print("Prompt file created successfully!,Restart the shell to take effect")
                        sys.exit(0)
                except OSError as err:
                    print("[red]%s[/red]"%err)
            else:
                print("[red]Please create a prompt file in configs\\prompt\\ \nor change the configuration file(i.e:configs\\prompt\\promptconf) from 1 to 0[/red]")
                sys.exit(1)                    
    else:
        #if the bool is not 1 then turn the bool to true as now we wanna print current directory as prompt
        __prompt__cwd = True                      
#####################################################################                  
while(True):    
    try:
        #if the bool(i.e:__prompt__cwd) is true then set prompt to current directory
        if __prompt__cwd is True:
            __prompt = os.getcwd()
        #getting cuurent directory list
        list_of_dir = os.listdir()
        tab_completer = WordCompleter(list_of_dir)    
        SESSION = PromptSession()
        command = SESSION.prompt(f'{__prompt}{if_git_dir()}>>', completer=tab_completer,auto_suggest=AutoSuggestFromHistory())
        #check OS And Store Commands for History CommaNd
        if check_onichans_os() == 'linux':
            try:
                with open(f"/home/{psutil.Process().username()}/Penta_history.his","a") as Historyfile:
                    Historyfile.write(f"{command}\n")
                    Historyfile.close()
            except:
                pass
        else:
            try:
                with open(f"C:\\Users\\{os.getlogin()}\\Documents\\Penta_history.his","a") as Historyfile:
                    Historyfile.write(f"{command}\n")
                    Historyfile.close()
            except FileNotFoundError:
                    pass
        #continue if user inputs empty strings instead of giving error
        if command == '' or command == ' ' or command == '  ' or command == '   ' or command == '    ' or command == '     ' or command == '      ' or command == '       ' or command == '        ' or command == '         ' or command == '          ' or command == '           ' or command == '            ' or command == '             ' or command == '              ' or command == '               ' or command == '                ' or command == '                 ' or command == '                  ' or command == '                   ' or command == '                    ' or command == '                     ' or command == '                      ' or command == '                       ' or command == '                        ' or command == '                         ' or command == '                          ' or command == '                           ' or command == '                            ' or command == '                             ' or command == '                              ' or command == '                               ' or command == '                                ' or command == '                                 ' or command == '                                  ' or command == '                                   ' or command == '                                    ' or command == '                                     ' or command == '                                      ' or command == '                                       ' or command == '                                        ' or command == '                                         ' or command == '                                          ' or command == '                                           ' or command == '                                            ' or command == '                                             ' or command == '                                              ' or command == '                                               ' or command == '                                                ' or command == '                                                 ' or command == '                                                  ' or command == '                                                   '    :
            continue
        if command == 'clear' or command == 'cls' or command == 'clr' :
            clear()
        elif command[:2] == 'cd' and len(command) > 2:
            path =command[3:]
            try:
                os.chdir(path)
            except OSError as err:
                print("[red]%s[/red] "%err)       
        elif command[:2] == 'cd' and len(command) == 2:
            print(f"Current Directory:{os.getcwd()}")
        elif command == 'cd ..':
            os.chdir("..")
        elif command[:4] == 'list' and len(command) == 4:
                for items in os.listdir('.'):
                    if os.path.isfile(items): print(f"[blue]f- {items}[/blue]")
                    elif os.path.isdir(items): print(f"[green]d- {items}[/green]")
                    elif os.path.islink(items): print(f"[yellow1]d- {items}[/yellow1]")
                    else: print(f"[red]--- {items}[/red]")        
        elif command[:4] == 'list' and len(command) > 4 and command[5:7] != '-p':
            try:
                path = command[5:]
                if path == '':
                    for items in os.listdir('.'):
                        if os.path.isfile(items): print(f"[blue]f- {items}[/blue]")
                        elif os.path.isdir(items): print(f"[green]d- {items}[/green]")
                        elif os.path.islink(items): print(f"[yellow1]d- {items}[/yellow1]")
                        else: print(f"[red]--- {items}[/red]")
                    continue                    
                for items in os.listdir(path):
                    if os.path.isfile(items): print(f"[blue]f- {items}[/blue]")
                    elif os.path.isdir(items): print(f"[green]d- {items}[/green]")
                    elif os.path.islink(items): print(f"[yellow1]d- {items}[/yellow1]")
                    else: print(f"[red]--- {items}[/red]")
            except OSError as err:
                print("[red]%s [/red]" %err)
        elif command[:4] == 'list' and len(command) > 4 and command[5:7] == '-p':
            try:
                for items in os.listdir('.'):
                    _Read_permissions = os.access(items,os.R_OK)
                    _Write_permissions = os.access(items,os.W_OK)
                    _Execute_permissions = os.access(items,os.X_OK)
                    if os.path.isfile(items):
                        print(f"Read={_Read_permissions},Write={_Write_permissions},Execute={_Execute_permissions}[blue] f- {items}[/blue]")
                    elif os.path.isdir(items):
                        print(f"Read={_Read_permissions},Write={_Write_permissions},Execute={_Execute_permissions}[green] d- {items}[/green]")
                    elif os.path.islink(items):
                        print(f"Read={_Read_permissions},Write={_Write_permissions},Execute={_Execute_permissions}[yellow1] d- {items}[/yellow1]")
                    else:
                        print(f"Read={_Read_permissions},Write={_Write_permissions},Execute={_Execute_permissions}[red] --- {items}[/red]")
            except OSError as err:
                print("[red]%s[/red]"%err)
        elif command == 'exit()' or command == 'quit()' or command == 'exit' or command == 'quit':
            break                
        elif command[:4] == 'sudo' and os.path.isfile(command[5:]) is True and check_onichans_os() != 'Win':
            filename,extension = os.path.splitext(command[5:])
            if extension != '':
                if extension.lower() == '.py':
                    try:
                        cmd = f'sudo python3 {filename}{extension}'
                        args = shlex.split(cmd)
                        subprocess.run(args)
                    except OSError as err:
                        print("[red]%s[/red]"%err)     
                elif extension.lower() == '.sh':
                    if check_onichans_os() == 'linux':
                        try:
                            cmd_1 = f'chmod +x {filename}{extension}' 
                            cmd_2 = f'sudo ./{filename}{extension}'
                            arg_1 = shlex.split(cmd_1)
                            arg_2 = shlex.split(cmd_2)
                            subprocess.run(arg_1)
                            subprocess.run(arg_2)
                        except OSError as err:
                            print("[red]%s[/red]"%err) 
                            print("[red]Possible Reasons:\n1:We couldn't get the permissions\n2:You didn't add the shebang(#!/bin/sh) at beggining of script.[/red]")
                    else:
                        print("[red]Not supported on Windows[/red]")    
                elif extension.lower() == '.c':
                    try:
                        cmd_1 = f"gcc {filename}{extension} -o {filename}"
                        cmd_2 = f"sudo ./{filename}"
                        arg_1 = shlex.split(cmd_1)
                        arg_2 = shlex.split(cmd_2)
                        subprocess.run(arg_1)
                        subprocess.run(arg_2)
                    except OSError as err:
                        print("[red]%s[/red]"%err)    
                elif extension.lower() == '.cpp':
                    try:
                        cmd_1 = f"g++ {filename}{extension} -o {filename}"
                        cmd_2 = f"sudo ./{filename}"
                        arg_1 = shlex.split(cmd_1)
                        arg_2 = shlex.split(cmd_2)
                        subprocess.run(arg_1)
                        subprocess.run(arg_2)
                    except OSError as err:
                        print("[red]%s[/red]"%err)    
                elif extension.lower() == '.java':
                    try:
                        cmd = f"sudo java {filename}{extension}"
                        arg = shlex.split(cmd)
                        subprocess.run(arg)
                    except OSError as err:
                        print("[red]%s[/red]"%err) 
                elif extension.lower() == '.jar':
                    try:
                        cmd = f"sudo java -jar {filename}{extension}"
                        arg = shlex.split(cmd)
                        subprocess.run(arg)
                    except OSError as err:
                        print("[red]%s[/red]"%err)  
                else:
                    pass 
        elif os.path.isfile(command) is True:
            filename,extension = os.path.splitext(command)
            if extension != '':
                if extension.lower() == '.py':
                    if check_onichans_os() == 'linux':
                        try:
                            cmd = f'python3 {filename}{extension}'
                            args = shlex.split(cmd)
                            subprocess.run(args)
                        except OSError as err:
                            print("[red]%s[/red]"%err)
                    else:
                        try:
                            cmd = f'python {filename}{extension}'
                            args = shlex.split(cmd)
                            subprocess.run(args)
                        except OSError as err:
                            print("[red]%s[/red]"%err)
                elif extension.lower() == '.sh':
                    if check_onichans_os() == 'linux':
                        try:
                            cmd_1 = f'chmod +x {filename}{extension}' 
                            cmd_2 = f'./{filename}{extension}'
                            arg_1 = shlex.split(cmd_1)
                            arg_2 = shlex.split(cmd_2)
                            subprocess.run(arg_1)
                            subprocess.run(arg_2)
                        except OSError as err:
                            print("[red]%s[/red]"%err) 
                            print("[red]Possible Reasons:\n1:We couldn't get the permissions\n2:You didn't add the shebang(#!/bin/sh) at beggining of script.[/red]")
                    else:
                        print("[red]Not supported on Windows[/red]")    
                elif extension.lower() == '.c':
                    try:
                        cmd_1 = f"gcc {filename}{extension} -o {filename}"
                        cmd_2 = f"./{filename}"
                        arg_1 = shlex.split(cmd_1)
                        arg_2 = shlex.split(cmd_2)
                        subprocess.run(arg_1)
                        subprocess.run(arg_2)
                    except OSError as err:
                        print("[red]%s[/red]"%err)    
                elif extension.lower() == '.cpp':
                    try:
                        cmd_1 = f"g++ {filename}{extension} -o {filename}"
                        cmd_2 = f"./{filename}"
                        arg_1 = shlex.split(cmd_1)
                        arg_2 = shlex.split(cmd_2)
                        subprocess.run(arg_1)
                        subprocess.run(arg_2)
                    except OSError as err:
                        print("[red]%s[/red]"%err)    
                elif extension.lower() == '.java':
                    try:
                        cmd = f"java {filename}{extension}"
                        arg = shlex.split(cmd)
                        subprocess.run(arg)
                    except OSError as err:
                        print("[red]%s[/red]"%err) 
                elif extension.lower() == '.jar':
                    try:
                        cmd = f"java -jar {filename}{extension}"
                        arg = shlex.split(cmd)
                        subprocess(arg)
                    except OSError as err:
                        print("[red]%s[/red]"%err)
                elif extension.lower() == '.bat':
                    if check_onichans_os() == 'linux':
                        cmd = f'wine cmd.exe /C {filename}{extension}'
                        arg = shlex.split(cmd)
                        subprocess.run(arg)
                    else:
                        cmd = f'{filename}{extension}'
                        arg = shlex.split(cmd)
                        subprocess.run(arg)
                elif extension.lower() == '.exe':
                    if check_onichans_os() == 'linux':
                        cmd = f'wine {filename}{extension}'
                        arg = shlex.split(cmd)
                        subprocess.run(arg)
                    else:
                        cmd = f'{filename}{extension}'
                        arg = shlex.split(cmd)
                        subprocess.run(arg)                            
                else:
                    pass                            
        elif command[:4] == 'nano':
            try:
                file = command[5:]
                cmd = f'nano {file}'
                arg = shlex.split(cmd)
                subprocess.run(arg)
            except OSError as err:
                print("[red]%s[/red]"%err) 
        elif command[:3] == 'cat' or command[:4] == 'type' or command[:4] == 'read':
            if command[:3] == 'cat':
                file = command[4:]
            else:
                file = command[5:]
            try:    
                with open(file,"r") as file:
                    buffer = file.read()
                    print(buffer)
                    file.close()
            except OSError as err:
                print("%s"%err)
            except:
                print("[red]An Error while reading the file![/red]")                    
        elif command == 'systeminfo' or command == 'sysinfo':
            #SYSTEM INFO
            print("[yellow1]SYSTEM INFO:::[/yellow1]")
            print("[blue]Basic Info:[/blue]")
            Username = psutil.Process().username()
            print(f"[green]Username:{Username}[/green]")
            #getting Host name by socket module
            _Host_name = socket.gethostname()
            print(f"[green]Hostname:{_Host_name}[/green]") 
            #Creating a dictionary to store system info in it
            sys_info = {} 
            # platform info
            platform_details = platform.platform()  
            sys_info["platform details"] = platform_details  
            # system info
            system_name = platform.system()  
            sys_info["system name"] = system_name 
            # processor info 
            processor_name = platform.processor()  
            sys_info["processor name"] = processor_name 
            # architectural info 
            architecture_details = platform.architecture() 
            sys_info["architectural detail"] = architecture_details 
            for keys,values in sys_info.items():
                print(f"[green]{keys} - {values}[/green]")
            #bios_version
            if check_onichans_os() == 'linux':
                try:
                    with open('/sys/class/dmi/id/bios_version','r') as Bios_ver:
                        bios_ver = Bios_ver.read()
                        print(f"[green]BIOS VERSION:{bios_ver}[/green]")
                        Bios_ver.close()
                except OSError as err:
                    print("[red]%s[/red]"%err)        
            else:
                try:
                    cmd = "wmic bios get smbiosbiosversion"
                    arg = shlex.split(cmd)
                    output = subprocess.check_output(arg)
                    print(f"[green]BIOS VERSION:{output}[/green]")
                except OSError as err:
                    print("[red]%s[/red]"%err)
            #Boot time
            if check_onichans_os() == 'linux':
                try:
                    output = subprocess.check_output(['uptime', '-p']).decode()
                    print(f"[green]Uptime:{output}[/green]")
                except OSError as err:
                    print("[red]%s[/red]"%err)
            else:
                try:
                    cmd = "wmic os get lastbootuptime"
                    arg = shlex.split(cmd)
                    output = subprocess.check_output(arg)
                    print(output)
                except OSError as err:
                    print("[red]%s[/red]"%err)
            #Ram usage
            print("[blue]Ram Usage:[/blue]")
            Values = []
            for items in psutil.virtual_memory():
                Values.append(items)
            Keys = ['Total','Available','Percent','Used','Free','Active','Inactive','Buffers','Cached','Shared',] 
            for limit in range (10):
                try:
                    print(f"[green]{Keys[limit]} -------- {Values[limit]}[/green]")
                except:
                    pass              
            #Network info:
            print("[blue]Network info:[/blue]")
            network_info = psutil.net_io_counters(pernic=True)
            for keys,values in network_info.items():
                print(keys,values)
            More_info = psutil.net_if_addrs()
            for keys,values in More_info.items():
                print(keys,values)    
            #using socket module to get ip
            Ip_address = socket.gethostbyname(_Host_name)
            print(f"IP Address:{Ip_address}")
            #getting mac address from get-mac
            MAC_ADDR = getmac.get_mac_address()
            print(f"MAC Address:{MAC_ADDR}")
            #Sensors info
            print("[blue]Sensors info:[/blue]")
            #temp
            try:
                Sensors_info_temp = psutil.sensors_temperatures()
                for keys,values in Sensors_info_temp.items():
                    print(f"{keys}:")
                    print(values)
                #fans
                Sensors_info_fan = psutil.sensors_fans()
                for keys,values in Sensors_info_fan.items():
                    print(f"{keys}:")
                    print(values)
            except:
                pass        
            #battery
            Sensors_info_battery = psutil.sensors_battery()
            print(f"[blue]Battery:[/blue]\n{Sensors_info_battery}")
        elif command[:3] == 'rem':
        #Try and read file,if user doesnt give file operand,then throw an error
            try:
                file = command[4:].split()[0]
            except IndexError:
                print("File operand missing!")    
            #Try and read -p argument and if user doesnt give the argument then set argument to a garbage~value and continue
            try:
                argument = command[4:].split()[1]
            except:
                #
                argument = 'GARBAGE~VALUE'
                pass   
            if argument == '-f' and os.path.isdir(file) is True:
                shutil.rmtree(file)
            else:
                try:
                    if os.path.isfile(file):
                        os.remove(file)
                    else:
                            os.rmdir(file)
                except OSError as err:
                        print("[red]%s[/red]"%err)
                        print("[red]Syntax:rem <file>/<directory>")
        elif command[:3] == 'ren' or command[:6] == 'rename':
            try:
                if (command.split()[0]) == 'ren':
                    files = command[4:]
                    _old_name = files.split()[0]
                    _new_name = files.split()[1]
                    os.rename(_old_name,_new_name)
                else:
                    files = command[7:]
                    _old_name = files.split()[0]
                    _new_name = files.split()[1]
                    os.rename(_old_name,_new_name)    
            except OSError as err:
                print("[red]%s[/red]"%err)
            except IndexError:
                print("[red]Missing file operand![/red]\n [green]Usage: ren/rename <oldname> <newname>[/green]")        
        elif command[:3] == 'mve' or command[:4] == 'move':
            try:
                if command[:3] == 'mve':
                    files = command[4:]
                    _old_place = files.split()[0]
                    _new_place = files.split()[1]
                    shutil.move(_old_place,_new_place)
                else:
                    files = command[5:]
                    _old_place = files.split()[0]
                    _new_place = files.split()[1]
                    shutil.move(_old_place,_new_place)
            except OSError as err:
                print("[red]%s[/red]"%err)
            except IndexError:
                print("[red]Missing file operand![/red]\n[green]Usage:mve/move <source> <destination>[/green]")            
        elif command[:3] == 'cpy':
            try:
                files = command[4:]
                source = files.split()[0]
                dest = files.split()[1]
                source_basename = os.path.basename(source)
                source_list = os.listdir(source)
                #Copy directories and files::the idea here is that copy_tree() method will copy all the data from source dir to destination
                # but it will not copy the directory it self so we will create a directory with same name in
                # destionation dir then we will copy all the data into that directory
                # if the source is a file an OSError exeption will be thrown ,we will
                # handle the exeption by using shutil.copy method 
                try:
                    copy_tree(source,dest)
                except OSError as err:
                    print("[red]%s[/red]"%err)    
                if check_onichans_os() == 'linux': 
                    os.mkdir(f'{dest}/{source_basename}')
                else:
                    os.mkdir(f'{dest}\\{source_basename}')
                for items in source_list:
                    if check_onichans_os() == 'linux':
                        src = f'{dest}/{items}'
                        des = f'{dest}/{source_basename}'
                    else:
                        src = f'{dest}\\{items}'
                        des = f'{dest}\\{source_basename}'
                    shutil.move(src,des)
            except OSError as err:
                shutil.copy(source,dest)
            except FileNotFoundError:
                print("[red]File/Directory not found[/red]")  
            except IndexError:
                print("[red]File operand missing![/red]")
            except:
                print("[red]Unknown Error[/red]"%err)            
        elif command[:4] == 'mdir':
            path = command[5:]
            try:
                os.mkdir(path)
            except OSError as err:
                print("[red]%s[/red]"%err)
                print("[green]Usage:mdir <directory name>[/green]")    
        elif command[:6] == 'create':
            file = command[7:]
            try:
                with open(file,'w') as file:
                    pass
            except OSError as err:
                print("[red]%s[/red]"%err)       
        elif command[:9] == 'ping-host':
                try:
                    raw_command = command[10:]
                    __host__ = raw_command.split()[0]
                    try:
                        __count__ = raw_command.split()[1]
                    except IndexError:
                        __count__ = 4       
                except IndexError:
                    print("[red]Error:Destination address required[/red]")      
                if check_onichans_os() == 'linux':    
                    print(f"[green]Hostname:{__host__}[/green]")
                    cmd = f"sudo python3 -c \"from pythonping import ping ; ping('{__host__}',verbose=True,count={__count__})\""
                    arg = shlex.split(cmd)
                    subprocess.run(arg)
                else:
                    os.system(f"cd {_prg_start_dir} & cd bin & adwin.bat pn '{__count__}' {__host__}")
        elif command[:8] == 'configip':
            print("[blue]Network info:[/blue]")
            network_info = psutil.net_io_counters(pernic=True)
            for keys,values in network_info.items():
                print(keys,values)
            More_info = psutil.net_if_addrs()
            for keys,values in More_info.items():
                print(keys,values)    
            #using socket module to get ip,here socket.gethostname returns the host name
            Ip_address = socket.gethostbyname(socket.gethostname())
            print(f"IP Address:{Ip_address}")
            #getting mac address from get-mac
            MAC_ADDR = getmac.get_mac_address()
            print(f"MAC Address:{MAC_ADDR}")
        elif command[:5].lower() == 'title':
            title = command[6:]
            if check_onichans_os() == 'linux':
                try:
                    cmd = f"python3 -c \"print(f'\33]0;{title}\a', end='', flush=True)\""
                    arg = shlex.split(cmd)
                    subprocess.run(arg)
                except:
                    print("[red]An error occured[/red]")    
            else:
                try:
                    ctypes.windll.kernel32.SetConsoleTitleW(f"{title}")
                except:
                    print("[red]An error occured[/red]")    
        elif command.lower() == 'os ver' or command.lower() == 'os version':
            system = platform.system()
            release = platform.release()
            version = platform.version()
            print(f"[green]System:{system}[/green]")
            print(f"[green]Release:{release}[/green]")
            print(f"[green]Version:{version}[/green]")
        elif command.lower() == 'getmac':
            print("MAC Address",getmac.get_mac_address())
        elif command.split()[0] == "getip" and int(len(command)) == 5:
            print("Local Ip address:",socket.gethostbyname(socket.gethostname()))
        try:
          elif command.split()[0] == "getip" and command.split()[1] == "-p":
              try:
                  print(f"Public Ip address:{requests.get('https://api.ipify.org').text}")
              except Exception:
                  print("[red]Error:couldn't connect to the server.\ncheck your internet connection[/red]") 
        except Exception:
            print("Local Ip address:",socket.gethostbyname(socket.gethostname()))
        elif command[:6] == 'murder':
            #kill process through name or pids
            try:
                raw_command = command[7:]
                argument = raw_command.split()[0]
                processid_or_name = raw_command.split()[1]
                process_list = psutil.pids()
                if argument == '-n':
                    # to kill a process through name, we would have to extract its pid
                    # to do this we will create a list of process ids then we will use 
                    #psutil.Process(PROCESS).name() method to convert pid into
                    # name then we will compare both names and if they math then we will kill the process
                    for process in process_list:
                        if processid_or_name.lower() in psutil.Process(process).name():
                            if check_onichans_os() == 'linux':
                                os.kill(process,signal.SIGKILL)
                            os.kill(process,signal.SIGTERM)                              
                elif argument == '-i':
                    if check_onichans_os() == 'linux':
                        os.kill(process,signal.SIGKILL)
                    os.kill(int(processid_or_name),signal.SIGTERM)
                else:
                    print("[red]Error:unidentified argument[/red]")
            except IndexError:
                print("[red]Processname/id or argument missing![/red]")
            #except :
            #   print("[red]Error Occured[/red]")
        elif command[:5] == 'shown':
            if check_onichans_os() == "linux":
                #Shutdown:
                try:        
                    argument_1 = command[6:].split()[0]
                except IndexError:
                    print("[red]argument missing[/red]")
                    continue      
                if argument_1 == '-s':
                    try:
                        argument_2 = command[6:].split()[1]
                        time = command[6:].split()[2]
                    except IndexError:
                        print("[red]Argument missing[/red]")    
                    if argument_2 != '-t':
                        print("[red]Undefined argument[/red]")
                        continue
                    cmd = f"shutdown {time}"
                    arg = shlex.split(cmd)
                    subprocess.run(arg)       
                elif argument_1 == '-r':
                    try:
                        argument_2 = command[6:].split()[1]
                        time = command[6:].split()[2]
                    except IndexError:
                        print("[red]Argument missing[/red]")
                        continue
                    if argument_2 != '-t':
                        print("[red]Undefined argument[/red]")
                        continue
                    cmd = f"shutdown -r {time}"
                    arg = shlex.split(cmd)
                    subprocess.run(arg)                
                elif argument_1 == '-l':
                    Username = psutil.Process().username()
                    cmd = f"skill -KILL -u {Username}"
                    arg = shlex.split(cmd)
                    subprocess.run(arg)
                elif argument_1 == '-c':
                    cmd = "shutdown -c"
                    arg = shlex.split(cmd)
                    subprocess.run(arg)
                else:
                    print("[red]Undefined argument![/red]")
            else:
                #Shutdown:
                try:        
                    argument_1 = command[6:].split()[0]
                except IndexError:
                    print("[red]argument missing[/red]")
                    continue      
                if argument_1 == '-s':
                    try:
                        argument_2 = command[6:].split()[1]
                        time = command[6:].split()[2]
                    except IndexError:
                        print("[red]Argument missing[/red]")    
                    if argument_2 != '-t':
                        print("[red]Undefined argument[/red]")
                        continue
                    cmd = f"shutdown /s /t {time}"
                    arg = shlex.split(cmd)
                    subprocess.run(arg)       
                elif argument_1 == '-r':
                    try:
                        argument_2 = command[6:].split()[1]
                        time = command[6:].split()[2]
                    except IndexError:
                        print("[red]Argument missing[/red]")
                        continue
                    if argument_2 != '-t':
                        print("[red]Undefined argument[/red]")
                        continue
                    cmd = f"shutdown /r /t {time}"
                    arg = shlex.split(cmd)
                    subprocess.run(arg)                
                elif argument_1 == '-l':
                    Username = psutil.Process().username()
                    cmd = f"shutdown /l"
                    arg = shlex.split(cmd)
                    subprocess.run(arg)
                elif argument_1 == '-c':
                    cmd = "shutdown /a"
                    arg = shlex.split(cmd)
                    subprocess.run(arg)
                else:
                    print("[red]Undefined argument![/red]")                                                
        elif command == "dime":
            date_time = datetime.now()
            dt_string = date_time.strftime("%d/%m/%Y %H:%M:%S")
            date = dt_string.split()[0]
            time = dt_string.split()[1]
            print(f"[green]Today's Date:{date}[green]")
            print(f"[green]Current Time:{time}[/green]")
        elif command == "username":
            Username = psutil.Process().username()
            print(f"[green]Username:{Username}[/green]")
        elif command[:6] == "search" or command[:6] == "reveal":
            try:
                File = command[7:].split()[0]
                #check os
                if check_onichans_os() == 'linux':
                    #first root point for linux
                    root_1 = f"/home/{psutil.Process().username()}/"
                    for root,dirs,files in os.walk(root_1):
                        for directory in dirs:
                            #print(directory)
                            if File in directory:
                                print("[purple]-----------------------------------------------------------------[/purple]")
                                print(f'[green]Directory:{root}[/green]:::[blue]Subdirectory:{directory}[/blue]')
                                print("[purple]-----------------------------------------------------------------[/purple]")
                                break   
                        for thefile in files:
                            #print(thefile)
                            if File in thefile:
                                print("[purple]-----------------------------------------------------------------[/purple]")
                                print(f'[green]Directory:{root}[/green]:::[blue]File:{thefile}[/blue]')
                                print("[purple]-----------------------------------------------------------------[/purple]")
                                break     
                    #second root point for linux
                    root_2 = f"/media/{psutil.Process().username()}/"
                    for root,dirs,files in os.walk(root_2):
                        for directory in dirs:
                            #print(directory)
                            if File in directory:
                                print("[purple]-----------------------------------------------------------------[/purple]")
                                print(f'[green]Directory:{root}[/green]:::[blue]Subdirectory:{directory}[/blue]')
                                print("[purple]-----------------------------------------------------------------[/purple]")
                                break
                        for thefile in files:
                            #print(thefile)
                            if File in thefile:
                                print("[purple]-----------------------------------------------------------------[/purple]")
                                print(f'[green]Directory:{root}[/green]:::[blue]File:{thefile}[/blue]')
                                print("[purple]-----------------------------------------------------------------[/purple]")
                                break 
                else:
                    #first root point for windows
                    root_1 = f"C:\\Users\\{psutil.Process().username()}\\"
                    for root,dirs,files in os.walk(root_1):
                        for directory in dirs:
                            #print(directory)
                            if File in directory:
                                print("[purple]-----------------------------------------------------------------[/purple]")
                                print(f'[green]Directory:{root}[/green]:::[blue]Subdirectory:{directory}[/blue]')
                                print("[purple]-----------------------------------------------------------------[/purple]")
                                break   
                        for thefile in files:
                            #print(thefile)
                            if File in thefile:
                                print("[purple]-----------------------------------------------------------------[/purple]")
                                print(f'[green]Directory:{root}[/green]:::[blue]File:{thefile}[/blue]')
                                print("[purple]-----------------------------------------------------------------[/purple]")
                                break
                    #First getting all the valid drive letters in windows
                    Drives = []
                    for drive_letters in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        if os.path.exists(f"{drive_letters}:"):
                            Drives.append(drive_letters)
                        else:
                            pass
                    for Drive_LETTERS in Drives:
                        for root,dirs,files in os.walk(f"{Drive_LETTERS}:\\"):
                            for directory in dirs:
                                #print(directory)
                                if File in directory:
                                    print("[purple]-----------------------------------------------------------------[/purple]")
                                    print(f'[green]Directory:{root}[/green]:::[blue]Subdirectory:{directory}[/blue]')
                                    print("[purple]-----------------------------------------------------------------[/purple]")
                                    break 
                            for thefile in files:
                                #print(thefile)
                                if File in thefile:
                                    print("[purple]-----------------------------------------------------------------[/purple]")
                                    print(f'[green]Directory:{root}[/green]:::[blue]File:{thefile}[/blue]')
                                    print("[purple]-----------------------------------------------------------------[/purple]")
                                    break
            except IndexError:
                print("[red]File operand missing[/red]")
            #except:
            #   print("[red]Error while searching[/red]")                                   
        elif command[:3] == "chp":
            try:
                raw_command = command[4:]
                Thefile =  raw_command.split()[0]
                Permissions = raw_command.split()[1]
                #check if permissions given are symbolic or absolute
                #if permissions given are integer then they r absolute otherwise symbolic
                if type(int(Permissions)) is int:
                    if Permissions == '0':
                        os.chmod(Thefile,0o0)
                    elif Permissions == '1':
                        os.chmod(Thefile,stat.S_IXUSR)
                    elif Permissions == '2':
                        os.chmod(Thefile,stat.S_IWUSR)
                    elif Permissions == '3':
                        os.chmod(Thefile,stat.S_IWUSR|stat.S_IXUSR )  
                    elif Permissions == '4':
                        os.chmod(Thefile,stat.S_IRUSR)
                    elif Permissions == '5':
                        os.chmod(Thefile,stat.S_IRUSR,stat.S_IXUSR)
                    elif Permissions == '6':
                        os.chmod(Thefile,stat.S_IRUSR,stat.S_IWUSR)
                    elif Permissions == '7':
                        os.chmod(Thefile,stat.S_IRWXU)
                    #Some extented permission for other groups and etc
                    elif Permissions == '777':
                        os.chmod(Thefile,stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
                    else:
                        print("[red]Error:You can only use octal values from 0 to 7[/red]")
                else:
                    print()        
            except IndexError:
                print("[red]Arguments missing[/red]")
            except FileNotFoundError:
                print("[red]Error:File not found[/red]")    
            except ValueError:
                #supported symbolic permissions
                if Permissions == '+x' or Permissions == '--x':
                    os.chmod(Thefile,stat.S_IRWXU)
                elif Permissions == '+r' or Permissions == 'r--':
                    os.chmod(Thefile,stat.S_IRUSR)
                elif Permissions == '+w' or Permissions =='-w-' or Permissions == '+r+w' or Permissions == '+w+r':
                    os.chmod(Thefile,stat.S_IWUSR|stat.S_IRUSR)    
                elif Permissions == '+w+r+x' or Permissions == '+w+x+r' or Permissions == '+r+w+x' or Permissions == '+r+x+w' or Permissions == '+x+w+r' or Permissions == '+x+r+w':
                    os.chmod(Thefile,stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
                else:
                    print("[red]Error:Unrecognized symbolic permission[/red]")        
            except:
                print("[red]Error while changing permission[/red]")            
        elif command == "about":
            window = Tk()
            window.title("About")
            Label(window,text="A open-source command-interpreter written in python").pack()
            Label(window,text=f"Version:{_VER}").pack()
            Label(window,text="License:Distributed under GPLv3").pack()
            Label(window,text="Report bugs and suggestions at:x-neron@pm.me").pack()
            window.mainloop()
        elif command == "chistory" or command == "ch":
            #check os
            if check_onichans_os() == 'linux':
                try:
                    with open(f"/home/{psutil.Process().username()}/Penta_history.his","r") as Historyfile:
                        history = Historyfile.read()
                        print(history)
                        Historyfile.close()
                except OSError as err:
                    print("[red]An Error occured.\nError:%s[/red]"%err)
            else:
                try:
                    with open(f"C:\\Users\\{os.getlogin()}\\Documents\\Penta_history.his","r") as Historyfile:
                        history = Historyfile.read()
                        print(history)
                        Historyfile.close()
                except OSError as err:
                    print("[red]An Error occured.\nError:%s[/red]"%err)
        elif command == "ver" or command == "version":
            print(f"Version:{_VER},Build Date:{_BULD_DATE}")
        elif command == "help" or command == "?":
            theconsole = Console()
            thetable = Table(show_header=True, header_style='bold #2070b2',title='[bold][#2070b2]HE[/#2070b2][#f8e020]LP[/#f8e020]')
            thetable.add_column('Command', justify='right')
            thetable.add_column('Description')
            thetable.add_row('cd','Change Directories,path indexing is [bold][green]\'Sensitive\'[/green][/bold]i.e: "cd Dir" and "cd  Dir"(extra space) are interpreted differently.use \'cd ..\' to cd one directory backward.Similarly you can use \'cd\' to show current directory\n_________________________________________________________')
            thetable.add_row('list<Directory>','lists directory Content.Use \'list\' to print Current Directory content.to list content with their permission,use \'-p\' parameter.\n_________________________________________________________')
            thetable.add_row('cls/clr/clear','Clear the console.\n_________________________________________________________')
            thetable.add_row('read,type,cat','Read Files.\n_________________________________________________________')
            thetable.add_row('sysinfo/systeminfo','Show system information such as hostname,platform,processor info,memory info,etc.\n_________________________________________________________')
            thetable.add_row('rem','Remove files and directories,use \'-f\' argument to remove directories that are not empty.\n_________________________________________________________')
            thetable.add_row('ren/rename','Rename files and directories.\n_________________________________________________________')
            thetable.add_row('mve/move','Move files and directories.\n_________________________________________________________')
            thetable.add_row('cpy','Copy files and directories.\n_________________________________________________________')        
            thetable.add_row('mdir','Make directories.\n_________________________________________________________')
            thetable.add_row('title','Change title of the shell.\n_________________________________________________________')
            thetable.add_row('dime','Use it to print date and time.\n_________________________________________________________')
            thetable.add_row('username','Print Username.\n_________________________________________________________')
            thetable.add_row('create','Create files.\n_________________________________________________________')
            thetable.add_row('ping-host','Ping an Host,use \'-t\' to specify number of echo requests.if none are specified then default number(i.e:4) is used.\n_________________________________________________________')
            thetable.add_row('configip','Shows network information.\n_________________________________________________________')
            thetable.add_row('getip','Show local ip address.use \'-p\' parameter to get the public ip address..\n_________________________________________________________')
            thetable.add_row('getmac','Print Mac Address.\n_________________________________________________________')
            thetable.add_row('murder <-i>/<-n> <Pid>/<Processname>','[bold][yellow]Epic name isn\'t it[/yellow][/bold].Use it to kill processes either by its ProcessId(pid,use -i) or Processname(use -n).\n_________________________________________________________')
            thetable.add_row('processlist','Shows all the Processes.\n_________________________________________________________')
            thetable.add_row('shown <-s>/<-r>/<-l> <-t> time','s\Shutdown,reboot or logout system.use <-s> for shutdown,<-r> for reboot and <-l> to logout.all arguments are must to shutdown or reboot system,but while loggingout <-t> will not be used.\nexample:shown -s -t 1234.timestamps for linux and windows are different.for windows time is counted in seconds while in linux time is counted in minutes.\n_________________________________________________________')
            thetable.add_row('chp <Filename> <permission>','Change file permissions.Works fine on *nix systems.use on windows is not preferable.use octal values from 0-7.More info [link=https://docs.oracle.com/cd/E19455-01/805-7229/6j6q8svd8/index.html][green]here[/green][/link].symbolic permissions such as +x(execute),+w(write),+r(read) are also supported\n[blue]Example:[/blue]chp Onichan_no_baka.txt 0 (will cease all permissions) .\n_________________________________________________________')
            thetable.add_row('os ver/ os version','Shows OS information.\n_________________________________________________________')
            thetable.add_row('reveal/search','Search for files and directories.\n_________________________________________________________')
            thetable.add_row('ver/version','Shows Penta version.\n_________________________________________________________')
            thetable.add_row('help','Show this help box.\n_________________________________________________________')
            thetable.add_row('chistory/ch','Prints commads history.\n_________________________________________________________')
            thetable.add_row('gtube <-v>/<-p> -q <video quality> <url>','A utility to download videos from youtube.use \'-v\' to download a video or \'-p\' to download a playlist.\n_________________________________________________________')
            thetable.add_row('gfile <url> <Filename>','Download Files from a server.\n_________________________________________________________')
            thetable.add_row('troute <host or url>','Trace possible routes and measures transit delay between packets across internet protocol network.\n_________________________________________________________')
            thetable.add_row('rmd <Markdown>','Reads Markdown with syntax highlight!.\n_________________________________________________________')
            thetable.add_row('treelist','Lists Directory as a tree.\n_________________________________________________________')
            thetable.add_row('about','About Penta.')
            theconsole.print(thetable) 
            print("""
    ╔==================================================================╗        
    |[green]Note:[/green]                                                             |
    |[green]1:[/green]If you want to print a banner at top                            |
    |of shell,goto to 'PROGRAMINSTALLATION/configs/Bannerconfs' and    |
    |change the file named bannerbool from 0 to 1                      |
    |and paste any banner to your liking in the                        |
    |file named 'banner'.                                              |
    |[blue]2:[/blue]Wanna print a custom prompt.                                    | 
    |goto'configs/prompt' and change the file named                    |
    |promptconf from 0 to 1.and type your prompt                       |
    |in file named prompt...cheers                                     |
    ╚==================================================================╝
            """)  
        elif command[:5] == "gtube":
        #Yeah i know i repeated the code,but am lazy to create functions    
            try:
                vid_arg = command.split()[1]
                vid_qual_arg = command.split()[2]
                vid_qual = command.split()[3]
                vid_url = command.split()[4]
                if vid_arg == '-v' and vid_qual_arg == '-q':
                    try:
                        if vid_qual == '360' or vid_qual == '360p':
                            itag = 18
                        elif vid_qual == '720' or vid_qual == '720p':
                            itag = 22
                        elif vid_qual == '1080' or vid_qual == '1080p':
                            itag = 137
                        elif vid_qual == '2160' or vid_qual == '2160p':
                            itag = 313
                        else:
                            print("Unsupported video quality")
                            continue
                        video = pytube.YouTube(vid_url)
                        thestream = video.streams.get_by_itag(itag)
                        if os.name == 'nt':
                            thestream.download(f"C:\\Users\\{os.getlogin()}\\Downloads")
                        else:
                            thestream.download(f"/home/{psutil.Process().username()}/Downloads")
                    except:
                        print("An Error occured\nPossible reasons:1:Internet connectivity.\n2:Video format not found.\n3:Video not found.")
                elif vid_arg == '-p' and vid_qual_arg == '-q':
                    try:
                        if vid_qual == '360' or vid_qual == '360p':
                            itag = 18
                        elif vid_qual == '720' or vid_qual == '720p':
                            itag = 22
                        elif vid_qual == '1080' or vid_qual == '1080p':
                            itag = 137
                        elif vid_qual == '2160' or vid_qual == '2160p':
                            itag = 313
                        else:
                            print("Unsupported video quality")
                            continue
                        Playlist_list = pytube.Playlist(vid_url)
                        for urls in Playlist_list:
                            video = pytube.YouTube(urls)
                            thestream = video.streams.get_by_itag(itag)
                            if os.name == 'nt':
                                thestream.download(f"C:\\Users\\{os.getlogin()}\\Downloads")
                            else:
                                thestream.download(f"/home/{psutil.Process().username()}/Downloads")                     
                    except:
                        print("[red]An Error occured.\nFolowing are some possible reasons\n1:Internet connectivity problem\n2:Video quality not found\n3:Video not found[/red]")
                else:
                    print("[red]Unrecognized Arguments[/red]")
            except:
                print("[red]Incorrect Command Structure![/red]")            
        elif command[:6] == 'troute':
            host = command.split()[1]       
            if check_onichans_os() == 'linux':
                troute_script = """
    from icmplib import traceroute
    hops = traceroute("%s")
    print('Distance/TTL    Address            Average round-trip time')
    Last_Distance = 0
    for hop in hops:
        if Last_Distance + 1 != hop.distance:
            print('Some gateways are not responding')
        # See the Hop class for details
        print(f'{hop.distance}               {hop.address}              {hop.avg_rtt} ms')
        Last_Distance = hop.distance        
                
            """%host
                with open("Tempscr.py","a") as TempScript:
                    TempScript.write(troute_script)
                cmd = "sudo python3 Tempscr.py"
                arg = shlex.split(cmd)
                subprocess.run(arg)
                os.remove("Tempscr.py")  
            else:
                os.system(f"cd {_prg_start_dir} & cd bin & adwin.bat tr '0' {host}")       
        elif command[:5] == 'gfile':
            #Download files from server
            try:
                raw_command= command[6:]
                url = raw_command.split()[0]
                Filename = raw_command.split()[1]
            except:
                print("[red]Missing Arguments!\n Usage:gfile <url> <filename>[red]")
                continue
            #Creating an object of class we have created
            File = DownloadFile(url,Filename)
            #Calling the Download method to download the file and store it
            File.Download()
        elif command == 'processlist':
            _pid_list = psutil.pids()
            console = Console()
            table = Table(show_header=True, header_style='bold #2070b2',title='[bold][#800080]Process[/#800080][#f8e020]Info[/#f8e020]')
            table.add_column('Process Name', justify='left')
            table.add_column('Process Id', justify='center')
            table.add_column('Status', justify='right')
            for pid in _pid_list:
                try:
                    process = psutil.Process(pid)
                    table.add_row(f'{process.name()}\n',f'{pid}\n',f'{process.status()}\n')
                except:
                    pass
            console.print(table)        
        elif command[:3] == 'rmd':
            # read markdown
            try:
                mdfile = command.split()[1]
            except IndexError:
                print("[red]File operand missing\nUsage:rmd <MARKDOWNFILE>[/red]")
                continue    
            try:
                with open(mdfile,'r') as Readmarkdown:
                    markdown = Readmarkdown.read()
                    Readmarkdown.close()
            except OSError as err:
                print("[red]%s[/red]"%err)
                continue
            console = Console()
            print("[green]Rendering Markdown File..[/green]\n")
            md = Markdown(markdown)
            console.print(md)
        elif command == 'treelist':
            # list dirs as tree
            if check_onichans_os() == 'linux':
                sdir.seedir(os.getcwd(),style='emoji')
            else:
                sdir.seedir(os.getcwd())    
        else:
            try:
                arg = shlex.split(f"{command} 2>nul")
                subprocess.run(arg,shell=True,check=True)
            except Exception:
                print(f"[red]Command not found[/red]")    
    except KeyboardInterrupt:
        print("KeyboardInterrupt")   
        continue
    except Exception as ex:
        print(f"""
[red]An Error occured during execution of command.
Error:
{ex}
report this error at https://github.com/Justaus3r/Penta/issues[/red]
 """)
else:
    sys.exit(0)
