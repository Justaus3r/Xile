### Readme.md 👋
## Penta
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Justaus3r/Penta)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
![Contribution](https://img.shields.io/badge/Contributions-Welcome-<brightgreen>)
[![Active](http://img.shields.io/badge/Status-Active-green.svg)](https://github.com/Justaus3r)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![semver](https://badgen.net/badge/Semantic-Version/1.0.2/purple)
[![GitHub commits since](https://img.shields.io/github/commits-since/Justaus3r/Penta/1.0.svg)](https://github.com/Justaus3r/Penta/commit/) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Issues](https://img.shields.io/github/issues-raw/Justaus3r/Penta?maxAge=25000)](https://github.com/Justaus3r/Penta/issues)
[![GitHub Release](https://img.shields.io/github/release/Justaus3r/Penta?style=flat)]()
[![Code of Conduct](https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=flat)](https://github.com/Justaus3r/Penta/blob/main/docs/CODE_OF_CONDUCT.md) 
[![Read the Docs](https://readthedocs.org/projects/penta/badge/?version=latest)](https://penta.readthedocs.io/en/latest/?badge=latest)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

 
Penta is a pure python **Command line** shell program that i have created to improve my understanding.As of now it supports all the basic commands(or thats what i think) that a shell program should have.i am working on it actively and improvements will be made in future.
Here is a table of commands that Penta supports as of now.i also converted a part of project into Python2(as an experiment),if you want to check that out just see the ```Pent2.py```. 
![List of commands-69](https://drive.google.com/uc?export=download&id=1ZfUtJmYf5mmUhKh8CHAfylyl069LWmwn)

### Download
|Operating System | Download                                                                                           |                                                               
| -------------   | ------------                                                                                       |
| Windows         | [Pentasetup.zip](https://mega.nz/file/481gUD5S#yEr5yZzfTepSVgwppwfBAPzuOxpsqmOnj70YEwSmCy8)|| 
| Linux           | [Penta-linux.zip](https://mega.nz/file/JplklbiI#ON2yVjeH0dnPeNwy5pVf8ZgRXzkAjIxIHvLz9AG3-RE)


### Changelog(Versionwise)
| Date:         | Comment:                                     | 
| ------------- |:-------------:                               | 
|23-Mar-2021    | Initial Release(Beta version)                |
|30-May-2021    | 1.0.3 Release                                |
### Changelog(Commitwise)
| Date:         | Comment:                                                                | 
| ------------- |:-------------:                                                          | 
|23-Mar-2021    | Initial Release(Beta version)                                           |
|28-Mar-2021    | Bug fix for windows and switched to nuitka for python compilation       |
|01-Apr-2021    | Fixed Typos and added ping and traceroute support for Windows           | 
|04-Apr-2021    | Can now download files from a server                                    |
|05-Apr-2021    | Tab Completion for both Windows and Linux and shows all the processes   |
|30-Apr-2021    | Read Markdown and list directories as a tree                            |
|22-May-2021    | Can detect a git initialized Directory                                  |


#### Upcoming update
--?
### Windows installation
**Penta will only run on windows 10.**

Download the setup from link above and execute it.after installing the setup,be sure to add the directory (present in installation Directory) named **bin** to [PATH](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/).
### Linux installation:
**if you are using bash instead of zsh,then edit Setup.sh and replace ```.zshrc``` with ```.bashrc```** 
Download the zip file from link above and follow following steps
- Unzip and file and cd to the directory.
- Open terminal here and type ```chmod +x Setup.sh ``` to give executable permission to script.
- Run the script i.e ./Setup.sh
- Restart the terminal after installing the setup
- Type ```penta``` and Have Fun 🥳...
#### Manual Installation(if the script doesn't work):
- Unzip the file and copy\move the ```bin``` ,```configs``` folder and executable named Penta to home directory
- Give executable permission to Penta.sh and copy\move it to /bin folder(linux bin folder and be sure that its on $PATH)
- (Optional)Now edit your ```.bashrc``` file and add a alias at the end of it: ```alias penta=Penta.sh```

**NOTE** Please be sure that your /bin directory is on $PATH. 

### Uninstallation:
Uninstallation in windows is pretty straightforward ,you just uninstall it like other softwares but there is no uninstalller for linux.delete Penta.sh from /bin folder,edit ```.bashrc``` file and remove the alias if any. and also remove the folder named ```bin```,```configs``` and Penta from home directory.
## Build from source
### Windows/Linux:
Penta can be built from pyinstaller,py2exe and Nuitka.
[Icon](https://www.flaticon.com/free-icon/command-window_656) used in Building Penta.

**[Nuitka(Recommended)](https://nuitka.net/)**([User manual](https://nuitka.net/doc/user-manual.html)):
- First install nuitka using ```pip install Nuitka```.
- Now open cmd in same Folder as the Project Folder and Type ```python3 -m nuitka --plugin-enable=tk-inter --windows-icon-from-ico=IconFileIfAnyIfNotThenSkipThisFlag --standalone Penta.py```(for linux remove the windows related flags)
- For the First time it's going to take some time depending on your network speed as nuitka installs a gcc compiler,for all the messages press Y.
- Your Executable will be compiled in Penta.dist.All the files in the dist folder are necessary to run Penta.if you want to make a single file executable then you can use the --onefile flag but i wouldn't recommend it. 

**[Py2exe](https://www.py2exe.org/)**:
- First install py2exe using ```pip install py2exe```.
- Now Create a file named setup.py or whatever.
- if you want to add icon *then*:
```
from distutils.core import setup
import py2exe
setup_dict = dict(console=[{'script':'Penta.py','icon_resources':[(0,'ICON.ico')]}])
setup(**setup_dict)
```
- Otherwise there is no need to create a dictionary i.e:
```
from distutils.core import setup
import py2exe
setup(console=['Penta.py'])
```
-now use python setup.py py2exe to build it.

**[Pyinstaller](https://www.pyinstaller.org/)**
- install pyinstaller using ```pip install pyinstaller```
- Now just cd to Project Folder and use ```pyinstaller --icon IconFileIfAny --onefile Penta.py```
- Your project will be built under the dist directory.
### TODO LIST
- [x] Support for changing directories
- [x] Support for listing directories
- [x] Support for creating files and directories
- [x] Support for deleting files and directories
- [ ] Support for Formatting Drives
- [x] Clears console
- [x] Read files
- [x] Show system info
- [x] Rename files and directories
- [x] Move files and directories
- [x] Show username
- [x] Tracerouting 
- [x] Show os version 
- [x] Copy files and directories
- [x] Change title of console
- [x] Print current time and date
- [x] Read Markdown Files 
- [ ] Encrypt Files and folders
- [x] Download videos and playlists from youtube 
- [ ] Tools for Pentesting
- [x] Shows all the processes 
- [x] Ping
- [X] Detect a git initialized directory 
- [x] Show network info
- [x] List directories as a tree 
- [x] Kill processes
- [x] Shutdown,reboot and logout
- [x] TAB Completion 
- [x] Search files.needs a bit of improvement
- [x] Change permissions of file
- [x] commands history
- [x] Supports Help command
- [x] Supports banner(Manual)
- [x] Supports custom prompt(Manual)
- [x] Download Files from a server 
- [ ] Much more...
# 🔴 Note: 🔴
Please do not confuse with the word "pure python" as some core operations such as shutting down pc ,etc require interaction with OS API(or thats what i think after my research),and low level languages are used to do so.python is a high level language and i think it can't interact with Os like C and other ll languages do.so i have used system commands to do such things.**if you think i am wrong**,Please do correct me 🙂..
### Bug report
Found any bug!
Report it to me at x-neron@pm.me
or open an [issue](https://github.com/Justaus3r/Penta/issues)
### Contributions:
All contributions are welcomed.fork this repo,improve it and [pull requests](https://github.com/Justaus3r/Penta/pulls)
### License
Distributed under GPLV3.0
### Note:
A General documentation is also available at [readthedocs.io](https://penta.readthedocs.io/en/latest/).Feel free to improve the doc.you can do so by editing this [File](https://github.com/Justaus3r/Penta/blob/main/docs/index.rst).



![Anurag's github stats](https://github-readme-stats.vercel.app/api?username=Justaus3r)
