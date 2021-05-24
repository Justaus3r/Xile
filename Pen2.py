# PART OF PENTA PROJECT WRITTEN INTO PYTHON 2 
# WARNING:EXPERIMENTAL FILE ,PROBABLY ONLY SUPPORTS 2 OR 3 COMMANDS
# COPYRIGHT Justaus3r
from __future__ import with_statement
from __future__ import absolute_import

import os 
import sys 
import stat 
import shlex 
import subprocess 
import platform 
import psutil 
import socket # for ping or other network thingis
import getmac #for getting mac
import shutil # for system info
import ctypes #for windows to play with.used to change title
from distutils.dir_util import copy_tree #for copying dirs 
from datetime import datetime #date and time
import signal # forgot
from Tkinter import * # for some guifrom rich.table import Table #for tables
import requests # for downloading files from server
from tqdm import trange #for progress bar
#from now on usin prompt_toolkit for userinput
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
# import seedir as sdir #for directory tree view
from io import open
######Created an Class for Downloading files,might need it in future########
class DownloadFile(object):
    def __init__(self,url,filename):
        self.url = url
        self.filename = filename

    def Download(self):
        print u"greenGetting Meta Data from the server/green"
        try:
            metafile = requests.get(self.url, stream=True)
            print u"greenServer status code:/green",metafile.status_code
            print u"greenContent Type:/green",metafile.headersu,'content-type'
            print u"greenEncoding/green",metafile.encoding        
            print u"purpleDownloading File from",self.url,"/purple"
        except:
            print u"An Error Occured while receiving headers"    
        #create an object that get the data in binary form
        for i in trange(1):
            thefile = requests.get(self.url)
        #write the data as binary
        with open(self.filename,u"wb") as File:
            File.write(thefile.content)
            File.close()
        print u"The file has been downloaded"
########################################################

#define a function to check os
def check_onichans_os():
  if os.name == u'nt':
     Os = u'Win'
     return Os
  Os = u'linux'
  return Os
#~VERSION AND BUILD DATE-----------------
_VER = u"1.0.2"
_BULD_DATE = u"14-April-2021"
# Func to check if the current directory is a git directory
def if_git_dir():
    if os.path.exists(u'.git'):
        return u'git'
    else:
        return u''

#~PROGRAM STARTING/boot DIRECTORY
_prg_start_dir = os.getcwdu()

 #######################################################################################################################################
#check the config file to see if the banner is to printed 
try:
    if check_onichans_os() == u'linux':     
        with open(u"configs/Bannerconfs/bannerbool",u"r") as bannerbool:
         Bool_value = bannerbool.read()
         bannerbool.close()
    else:
         with open(u"configs\\Bannerconfs\\bannerbool",u"r") as bannerbool:
             Bool_value = bannerbool.read()
             bannerbool.close()
except OSError, err:
    print u"red%s/red"%err         
#print banner if bool value is 1 otherwise continue
try:
 if Bool_value == u'1':
     try:
         if check_onichans_os() == u'linux':
             with open(u"configs/Bannerconfs/banner",u"r") as banner:
                 Banner = banner.read()
                 print Banner
                 banner.close()
         else:
             with open(u"configs\\Bannerconfs\\banner",u"r") as banner:
                 Banner = banner.read()
                 print Banner
                 banner.close()                                  
     except OSError, err:
         print u"red%s/red"%err  
except NameError:
        print u"redConfiguration file Error/red"
#####################################################################
    #prompt
    # check the configuration file to see if custom prompt is to be printed
    #CHECK OS
if check_onichans_os() == u'linux':
    #Try and see if the configuration file(to print custom prompt) exists,if not throw an error and exit
    try:
        with open(u"configs/prompt/promptconf",u"r") as promptconf:
            _read_conf = promptconf.read()
            promptconf.close() 
    except FileNotFoundError:
        print u"redConfiguration file missing!/red"
        sys.exit(1)                
    if _read_conf == u'1':
        #Try and see if the prompt file exist,if not throw an error
        try:
            with open(u"configs/prompt/prompt",u"r") as promptfile:
                __prompt = promptfile.read()
                __prompt__cwd = False
        except FileNotFoundError:
            print u"redPrompt file not found!/red"
            choice = raw_input(u"Do you want to create a prompt fileY/N:")
            if choice.upper() == u'Y':
                prompt = raw_input(u"Type your custom prompt:")
                try:
                    with open(u"configs/prompt/prompt",u"w") as make_prompt_file:
                        make_prompt_file.write(prompt)
                        make_prompt_file.close()
                        print u"Prompt file created successfully!,Restart the shell to take effect"
                        sys.exit(0)
                except OSError, err:
                    print u"red%s/red"%err
            else:
                print u"redPlease create a prompt file in configs/prompt/ \nor change the configuration file(i.e:configs/prompt/promptconf) from 1 to 0/red"
                sys.exit(1)                    
    else:
        __prompt__cwd = True                      
else:
    try:
        with open(u"configs\\prompt\\promptconf",u"r") as promptconf:
            _read_conf = promptconf.read()
            promptconf.close() 
    except FileNotFoundError:
        print u"redConfiguration file missing!/red"
        sys.exit(1)                
    if _read_conf == u'1':
        #Try and see if the prompt file exist.if the prompt file exists,read data from it and turn the __prompt__cwd bool to false as we dont want to print current directory as prompt.if not throw an error
        try:
            with open(u"configs\\prompt\\prompt",u"r") as promptfile:
                __prompt = promptfile.read()
                __prompt__cwd = False
        except FileNotFoundError:
            print u"redPrompt file not found!/red"
            choice = raw_input(u"Do you want to create a prompt fileY/N:")
            if choice.upper() == u'Y':
                prompt = raw_input(u"Type your custom prompt:")
                try:
                    with open(u"configs\\prompt\\prompt",u"w") as make_prompt_file:
                        make_prompt_file.write(prompt)
                        make_prompt_file.close()
                        print u"Prompt file created successfully!,Restart the shell to take effect"
                        sys.exit(0)
                except OSError, err:
                    print u"red%s/red"%err
            else:
                print u"redPlease create a prompt file in configs\\prompt\\ \nor change the configuration file(i.e:configs\\prompt\\promptconf) from 1 to 0/red"
                sys.exit(1)                    
    else:
        #if the bool is not 1 then turn the bool to true as now we wanna print current directory as prompt
        __prompt__cwd = True                      
#####################################################################                  
while(True):
    #if the bool(i.e:__prompt__cwd) is true then set prompt to current directory
    if __prompt__cwd is True:
        __prompt = os.getcwd()
    #getting cuurent directory list
    list_of_dir = os.listdir(os.getcwd())
    PROMPT = __prompt + if_git_dir() + '>>'
    command = raw_input(PROMPT)
    #check OS And Store Commands for History CommaNd
    if check_onichans_os() == u'linux':
        try:
            with open(u"/home" + psutil.Process().username() + "/Penta_history.his","a") as Historyfile:
                Historyfile.write(command,"\n")
                Historyfile.close()
        except:
            pass
    else:
           try:
            with open(u"C:\\Users\\" + os.getlogin() + "\\Documents\\Penta_history.his","a") as Historyfile:
                Historyfile.write({command},"\n")
                Historyfile.close()
           except FileNotFoundError:
                pass
    #continue if user inputs empty strings instead of giving error
    if command == u'' or command == u' ' or command == u'  ' or command == u'   ' or command == u'    ' or command == u'     ' or command == u'      ' or command == u'       ' or command == u'        ' or command == u'         ' or command == u'          ' or command == u'           ' or command == u'            ' or command == u'             ' or command == u'              ' or command == u'               ' or command == u'                ' or command == u'                 ' or command == u'                  ' or command == u'                   ' or command == u'                    ' or command == u'                     ' or command == u'                      ' or command == u'                       ' or command == u'                        ' or command == u'                         ' or command == u'                          ' or command == u'                           ' or command == u'                            ' or command == u'                             ' or command == u'                              ' or command == u'                               ' or command == u'                                ' or command == u'                                 ' or command == u'                                  ' or command == u'                                   ' or command == u'                                    ' or command == u'                                     ' or command == u'                                      ' or command == u'                                       ' or command == u'                                        ' or command == u'                                         ' or command == u'                                          ' or command == u'                                           ' or command == u'                                            ' or command == u'                                             ' or command == u'                                              ' or command == u'                                               ' or command == u'                                                ' or command == u'                                                 ' or command == u'                                                  ' or command == u'                                                   '    :
        continue
    if command == u'clear' or command == u'cls' or command == u'clr' :
        clear()
    elif command[:2] == u'cd' and len(command) > 2:
        path = command[:3]
        try:
            os.chdir(path)
        except OSError, err:
            print u"red%s/red "%err       
    elif command[:2] == u'cd' and len(command) == 2:
        print u"Current Directory:",os.getcwd()
    elif command == u'cd ..':
        os.chdir(u"..")
    elif command[:4] == u'list' and len(command) == 4:
            for items in os.listdir(u'.'):
                if os.path.isfile(items): print u"f-",items
                elif os.path.isdir(items): print u"d-",items
                elif os.path.islink(items): print u"d-",items
                else: print u"---",items        
    elif command[:4] == u'list' and len(command) > 4 and command[5:7] != u'-p':
        try:
         path = command[5:]
         if path == u'':
            for items in os.listdir(u'.'):
                if os.path.isfile(items): print u"f-",items
                elif os.path.isdir(items): print u"d-",items
                elif os.path.islink(items): print u"d-",items
                else: print u"---",items        
            continue                    
         for items in os.listdir(path):
            for items in os.listdir(u'.'):
                if os.path.isfile(items): print u"f-",items
                elif os.path.isdir(items): print u"d-",items
                elif os.path.islink(items): print u"d-",items
                else: print u"---",items        
        except OSError, err:
            print u"red%s /red" %err
    elif command[:4] == u'list' and len(command) > 4 and command[5:7] == u'-p':
         try:
             for items in os.listdir(u'.'):
                _Read_permissions = os.access(items,os.R_OK)
                _Write_permissions = os.access(items,os.W_OK)
                _Execute_permissions = os.access(items,os.X_OK)
                if os.path.isfile(items):
                     print u"Read=",_Read_permissions,u",Write=",_Write_permissions,u",Execute=",_Execute_permissions,u"f- ",items
                elif os.path.isdir(items):
                     print u"Read=",_Read_permissions,u",Write=",_Write_permissions,u",Execute=",_Execute_permissions,u"d- ",items
                elif os.path.islink(items):
                     print u"Read=",_Read_permissions,u",Write=",_Write_permissions,u",Execute=",_Execute_permissions,u"d- ",items
                else:
                     print u"Read=",_Read_permissions,u",Write=",_Write_permissions,u",Execute=",_Execute_permissions,u"--- ",items
         except OSError, err:
             print u"red%s/red"%err
    elif command == u'exit()' or command == u'quit()' or command == u'exit' or command == u'quit':
        break                
    elif command.lower() == u'help':
        print u'HELP:'
        print u'WARNING:Part of program written in Python2 as a experiment,only supports cd,list and quit/exit command and tested only on linux.'
    else:
        try:
            arg = shlex.split(command)
            subprocess.run(arg)
        except Exception:
            print u"Command not found"    
else:
    sys.exit(0)
