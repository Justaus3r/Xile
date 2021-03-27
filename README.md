### Readme.md 👋
## Penta
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
![Contribution](https://img.shields.io/badge/Contributions-Welcome-<brightgreen>)
[![Active](http://img.shields.io/badge/Status-Active-green.svg)](https://github.com/Justaus3r)
[![GitHub commits since](https://img.shields.io/github/commits-since/Justaus3r/Penta/1.0)]() 
[![Issues](https://img.shields.io/github/issues-raw/Justaus3r/Penta?maxAge=25000)](https://github.com/Justaus3r/Penta/issues)
[![GitHub Release](https://img.shields.io/github/release/Justaus3r/Penta?style=flat)]()
[![Code of Conduct](https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=flat)](https://github.com/Justaus3r/Penta/blob/main/docs/CODE_OF_CONDUCT.md) 
[![Read the Docs](https://readthedocs.org/projects/penta/badge/?version=latest)](https://penta.readthedocs.io/en/latest/?badge=latest)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
>>Penta is under active development.anything can change without prior notice.
 
Penta is a pure python **Command line** shell program that i have created to improve my understanding of python.As of now it supports all the basic commands(or thats what i think) that a shell program should have.i am working on it actively and improvements will be made in future.
Here is a table of commands that Penta supports as of now.
![List of commands-69](https://drive.google.com/uc?export=download&id=1ZfUtJmYf5mmUhKh8CHAfylyl069LWmwn)

### Download
|Operating System | Download                                                                                           |                                                               
| -------------   | ------------                                                                                       |
| Windows         | [Pentasetup.exe](https://drive.google.com/uc?export=download&id=1rf2yExnM9oiEWqZK-1h18XHenkyWJA2t)|| 
| Linux           | [Penta-linux.zip](https://drive.google.com/uc?export=download&id=1zh2-uv_dd1cd3d3pkv87xPDXUO7N1tKe)
### Changelog
| Date:         | Comment:                     | 
| ------------- |:-------------:               | 
|23-Mar-2021    | Initial Release(Beta version)|
#### Upcoming update
--?
### Windows installation
Download the setup from link above and execute it.after installing the setup,be sure to add the directory present in Program Files(or where you have installed Penta) named bin to [PATH](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/).
### Linux installation
**if you are using bash instead of zsh,then don't use the Setup.sh(or just edit it and add .bashrc instead of .zshrc),instead follow the steps afterward.** 

Download the zip file from link above and follow following steps
- Unzip and file and cd to the directory.
- Open terminal here and type ```chmod +x Setup.sh ``` to give executable permission to script.
- Run the script i.e ./Setup.sh
- Restart the terminal after installing the setup
- Type ```penta``` and Have Fun 🥳...
#### Steps for bash Users:
Bash users would have to do the configurations manually:
- Unzip the file and copy\move the ```bin``` ,```configs``` folder and executable named Penta to home directory
- Give executable permission to Penta.sh and copy\move it to /bin folder(linux bin folder and be sure that its on $PATH)
- (Optional)Now edit your ```.bashrc``` file and add a alias at the end of it: ```alias penta=Penta.sh```

**NOTE** Please be sure that your /bin directory is on $PATH. 

### Uninstallation:
Uninstallation in windows is pretty straightforward ,you just uninstall it like other softwares but there is no uninstalller for linux(well it ain't installation in first place but some configuration).delete Penta.sh from /bin folder,edit ```.bashrc``` file and remove the alias if any. and also remove the folder named ```bin```,```configs``` and Penta from home directory.
## Build from source
#### Windows:
- First install all the dependencies using ```pip install -r requirements.txt```.
- if you dont want to build it then its all done.otherwise follow ⬇️ 
- First install py2exe using ```pip install py2exe```.
- Now Create a file named setup.py or whatever.
- if you want to add icon then:
```
from distutils.core import setup
import py2exe
setup_dict = dict(console=[{'script':'Penta.py','icon_resources':[(0,'ICON.ico')]}])
setup(**setup_dict)
```
- Otherwise there is no need to create a dictionary.
```
from distutils.core import setup
import py2exe
setup(console=['Penta.py'])
```
-now use python setup.py py2exe to build it.
#### Linux:
- Clone the repo and install the dependencies(also install them as sudo user or you may face some problems).
- For linux i have used pyinstaller.you can install pyinstaller using ```python3 -m pip install pyinstaller```
- Now use ```pyinstaller --onefile Penta.py``` to build.be sure to copy the ```configs``` and ```bin``` directory to the executable directory. 
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
- [x] Show os version 
- [x] Copy files and directories
- [x] Change title of console
- [x] Print current time and date
- [ ] Encrypt Files and folders
- [x] Download videos and playlists from youtube 
- [ ] Tools for Pentesting
- [x] Ping.Only available for linux(for now atleast)
- [x] Show network info
- [x] Kill processes
- [x] Shutdown,reboot and logout
- [x] Search files.needs a bit of improvement
- [x] Change permissions of file
- [x] commands history
- [x] Supports Help command
- [x] Supports banner(Manual)
- [x] Supports custom prompt(Manual)
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
