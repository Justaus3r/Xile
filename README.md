### Readme.md 👋
## Penta
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
![Contribution](https://img.shields.io/badge/Contributions-Welcome-<brightgreen>)
[![Active](http://img.shields.io/badge/Status-Active-green.svg)](https://tterb.github.io)
[![Issues](https://img.shields.io/github/issues-raw/Justaus3r/Penta?maxAge=25000)](https://github.com/Justaus3r/Penta/issues)
[![GitHub Release](https://img.shields.io/github/release/Justaus3r/Penta?style=flat)]()
[![Code of Conduct](https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=flat)](https://github.com/Justaus3r/Penta/blob/main/docs/CODE_OF_CONDUCT.md) 
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
>>Penta is under active development.anything can change without prior notice. 
Penta is a pure python shell program that i have created to improve my understanding of python.As of now it supports all the basic commands(or thats what i think) that a shell program should have.i am working on it actively and improvements will be made in future.
Here is a table of commands that Penta supports as of now.
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        Command ┃ Description                                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│                             cd │ Change Directories,path indexing is         │
│                                │ 'Sensitive'i.e: "cd Dir" and "cd            │
│                                │ Dir"(extra space) are interpreted           │
│                                │ differently.use 'cd ..' to cd one directory │
│                                │ backward.Similarly you can use 'cd' to show │
│                                │ current directory                           │
│                                │ __________________________________________… │
│                list<Directory> │ lists directory Content.Use 'list' to print │
│                                │ Current Directory content.to list content   │
│                                │ with their permission,use '-p' parameter.   │
│                                │ __________________________________________… │
│                  cls/clr/clear │ Clear the console.                          │
│                                │ __________________________________________… │
│                  read,type,cat │ Read Files.                                 │
│                                │ __________________________________________… │
│             sysinfo/systeminfo │ Show system information such as             │
│                                │ hostname,platform,processor info,memory     │
│                                │ info,etc.                                   │
│                                │ __________________________________________… │
│                            rem │ remove files and directories,use '-f'       │
│                                │ argument to remove directories that are not │
│                                │ empty.                                      │
│                                │ __________________________________________… │
│                     ren/rename │ Rename files and directories.               │
│                                │ __________________________________________… │
│                       mve/move │ Move files and directories.                 │
│                                │ __________________________________________… │
│                            cpy │ Copy files and directories.                 │
│                                │ __________________________________________… │
│                           mdir │ Make directories.                           │
│                                │ __________________________________________… │
│                          title │ Change title of the shell.                  │
│                                │ __________________________________________… │
│                           dime │ daym!.lol use it to print date and time.    │
│                                │ __________________________________________… │
│                       username │ print Username.                             │
│                                │ __________________________________________… │
│                         create │ Create files.                               │
│                                │ __________________________________________… │
│                      ping-host │ Ping an Host,use '-t' to specify number of  │
│                                │ echo requests.if none are specified then    │
│                                │ default number(i.e:4) is used.Not supported │
│                                │ on windows(as of yet).                      │
│                                │ __________________________________________… │
│                       configip │ Shows network information.                  │
│                                │ __________________________________________… │
│                          getip │ Print IP address.                           │
│                                │ __________________________________________… │
│                         getmac │ Print Mac Address.                          │
│                                │ __________________________________________… │
│ murder <-i>/<-n> <Processname> │ Epic name isn't it.Use it to kill processes │
│                                │ either by its ProcessId(pid,use -i) or      │
│                                │ Processname(use -n).                        │
│                                │ __________________________________________… │
│ shown <-s>/<-r>/<-l> <-t> time │ shutdown,reboot or logout system.use <-s>   │
│                                │ for shutdown,<-r> for reboot and <-l> to    │
│                                │ logout.all arguments are must to shutdown   │
│                                │ or reboot system,but while loggingout <-t>  │
│                                │ will not be used.                           │
│                                │ example:shown -s -t 1234.timestamps for     │
│                                │ linux and windows are different.for windows │
│                                │ time is counted in seconds while in linux   │
│                                │ time is counted in minutes.                 │
│                                │ __________________________________________… │
│    chp <Filename> <permission> │ Change file permissions.Works fine on *nix  │
│                                │ systems.use on windows is not               │
│                                │ preferable.use octal values from 0-7.More   │
│                                │ info here.symbolic permissions such as      │
│                                │ +x(execute),+w(write),+r(read) are also     │
│                                │ supported                                   │
│                                │ Example:chp Onichan_no_baka.txt 0 (will     │
│                                │ cease all permissions) .                    │
│                                │ __________________________________________… │
│             os ver/ os version │ Shows OS information.                       │
│                                │ __________________________________________… │
│                  reveal/search │ Search for files and directories.           │
│                                │ __________________________________________… │
│                    ver/version │ Shows Penta version.                        │
│                                │ __________________________________________… │
│                           help │ Show this help box.                         │
│                                │ __________________________________________… │
│                       chistory │ prints commads history.                     │
│                                │ __________________________________________… │
│                          about │ About Penta.                                │
└────────────────────────────────┴────────────────────────────────------------─┘
