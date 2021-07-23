.. role:: raw-html-m2r(raw)
   :format: html


Documentation 👋
^^^^^^^^^^^^^^^^

Penta
-----


.. image:: https://img.shields.io/badge/badges-awesome-green.svg
   :target: https://github.com/Justaus3r/Penta
   :alt: Awesome Badges


.. image:: https://img.shields.io/badge/License-GPL%20v3-yellow.svg
   :target: https://opensource.org/licenses/
   :alt: GPLv3 License


.. image:: https://img.shields.io/badge/Contributions-Welcome-<brightgreen>
   :target: https://img.shields.io/badge/Contributions-Welcome-<brightgreen>
   :alt: Contribution


.. image:: http://img.shields.io/badge/Status-Active-green.svg
   :target: https://github.com/Justaus3r
   :alt: Active


.. image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/
   :alt: made-with-python


.. image:: https://badgen.net/badge/Semantic-Version/1.3.1/purple
   :target: https://badgen.net/badge/Semantic-Version/1.3.1/purple
   :alt: semver


.. image:: https://img.shields.io/github/commits-since/Justaus3r/Penta/1.0.svg
   :target: https://github.com/Justaus3r/Penta/commit/
   :alt: GitHub commits since
 

.. image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square
   :target: http://makeapullrequest.com
   :alt: PRs Welcome


.. image:: https://img.shields.io/github/issues-raw/Justaus3r/Penta?maxAge=25000
   :target: https://github.com/Justaus3r/Penta/issues
   :alt: Issues


.. image:: https://img.shields.io/github/release/Justaus3r/Penta?style=flat
   :target: 
   :alt: GitHub Release


.. image:: https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=flat
   :target: https://github.com/Justaus3r/Penta/blob/main/docs/CODE_OF_CONDUCT.md
   :alt: Code of Conduct
 

.. image:: https://readthedocs.org/projects/penta/badge/?version=latest
   :target: https://penta.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs


.. image:: https://badges.frapsoft.com/os/v3/open-source.svg?v=103
   :target: https://opensource.org/
   :alt: Open Source


*A cmd/command prompt/shell/command interpreter(whatever you say) purely written in python* .tries to be more efficient ,functional and easier to use than our classic cmd.
Here is a table of commands that Penta supports as of now.i also converted a part of project into Python2(as an experiment),if you want to check that out just see the ``Pent2.py``. 

Note:
~~~~~

**Please note that commands that have additional argumnents such as ``cd <directory>`` are index sensitive.i.e ``cd MyDirectory`` and ``cd  MyDirectory``\ (with extra space) are interpreted differently.also all the system commands are also supported** 

.. list-table::
   :header-rows: 1

   * - Commands:
     - Description:
   * - cd
     - Change Directories
   * - list
     - lists directory Content.use '-p' to list directory content with its permission.
   * - clear,clr,cls
     - Clear screen
   * - read,type,cat
     - Read Files
   * - sysinfo/systeminfo
     - Show system info
   * - rem  \\ :raw-html-m2r:`<filename>`
     - Remove Files and Folders.use '-f' to remove directories that are unempty.
   * - ren/rename \\ :raw-html-m2r:`<oldname>` \\ :raw-html-m2r:`<newname>`
     - Rename files and directories
   * - mve/move \\ :raw-html-m2r:`<source>` \\ :raw-html-m2r:`<destination>`
     - Move files and directories
   * - cpy \<source&gt; \\ :raw-html-m2r:`<destination>`
     - Copy files and directories
   * - mdir \\ :raw-html-m2r:`<dirname>`
     - Make Directories
   * - title \\ :raw-html-m2r:`<name>`
     - Change title of window
   * - dime
     - Print date and time(ik,that command tho,lol)
   * - username
     - Print username
   * - ping-host
     - Ping host,use '-t' to specify the count.default is 4 requests
   * - configip
     - Shows network info
   * - getip
     - Show local ip address.use '-p' parameter to get the public ip address.
   * - getmac
     - Show Mac address
   * - murder <-i>/<-n> \\ :raw-html-m2r:`<Pid>`\ /\\ :raw-html-m2r:`<Processname>`
     - Kill a process by either its pid(by using -i parameter) or its name(by using -n parameter).
   * - processlist
     - Show all the processes
   * - shown \<-s>/\<-r>/\<-l> \<-t> time
     - shutdown,reboot or logout system.use -s to shutdown,-r to reboot,-l to logout,-t to set time-out before shutdown.on windows the timout is in seconds where as in linux its in minutes.
   * - chp :raw-html-m2r:`<Filename>` :raw-html-m2r:`<permission>`
     - Change File permissions.works partially on windows.use octal values from 0-7.\ `More info <https://docs.oracle.com/cd/E19455-01/805-7229/6j6q8svd8/index.html>`_.Symbolic permissions(i.e:+x,+r,+w) are also supported.
   * - os ver/ os version
     - Shows OS information.
   * - search/reveal \\ :raw-html-m2r:`<filename>`
     - Search Files and Folder.
   * - ver/version
     - Show Penta's version.
   * - help
     - Shows this help box.
   * - chistory/ch
     - Show command history.
   * - gtube <-v>/<-p> -q :raw-html-m2r:`<video quality>` :raw-html-m2r:`<url>`
     - Download videos(-v)/playlists(-p) from youtube using available quality.
   * - gfile \\ :raw-html-m2r:`<url>` \\ :raw-html-m2r:`<Filename>`
     - Download files from a http server.
   * - troute \\ :raw-html-m2r:`<host or url>`
     - traceroute an host.
   * - rmd \\ :raw-html-m2r:`<Markdown>`
     - Read Markdown with syntax highlight!
   * - treelist
     - lists current directory as a tree
   * - about
     - About Penta


Download
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Operating System
     - Download:
   * - Windows
     - `Penta-Setup.zip <https://mega.nz/file/481gUD5S#yEr5yZzfTepSVgwppwfBAPzuOxpsqmOnj70YEwSmCy8>`_
   * - Linux
     - `Penta-linux.zip <https://mega.nz/file/JplklbiI#ON2yVjeH0dnPeNwy5pVf8ZgRXzkAjIxIHvLz9AG3-RE>`_
     
Changelog(Versionwise)
^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Date:
     - Comment:
   * - 23-Mar-2021
     - Initial Release(Beta version)
   * - 30-May-2021
     - Release 1.3.0


CommitTable
^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Date:
     - Comment:
   * - 23-Mar-2021
     - Initial Release(Beta version)
   * - 28-Mar-2021
     - Bug fix for windows and switched to nuitka for python compilation
   * - 01-Apr-2021
     - Fixed Typos and added ping and traceroute support for Windows
   * - 04-Apr-2021
     - Can now download files from a server
   * - 05-Apr-2021
     - Tab Completion for both Windows and Linux and shows all the processes
   * - 30-Apr-2021
     - Read Markdown and list directories as a tree
   * - 22-May-2021
     - Can detect a git initialized Directory
   * - 23-July-2021
     - Fix some system commands not working and other bugs and can now show pulic ip addresses


Upcoming update
~~~~~~~~~~~~~~~

--?

Windows installation
^^^^^^^^^^^^^^^^^^^^

**Penta will only run on windows 10.**

Download the setup from link above and execute it.after installing the setup,be sure to add the directory (present in installation Directory) named **bin** to `PATH <https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/>`_.

Linux installation:
^^^^^^^^^^^^^^^^^^^

**if you are using bash instead of zsh,then edit Setup.sh and replace ``.zshrc`` with ``.bashrc``\ ** 
Download the zip file from link above and follow following steps


* Unzip and file and cd to the directory.
* Open terminal here and type ``chmod +x Setup.sh`` to give executable permission to script.
* Run the script i.e ./Setup.sh
* Restart the terminal after installing the setup
* Type ``penta`` and Have Fun 🥳...
  #### Manual Installation(if the script doesn't work):
* Unzip the file and copy\move the ``bin`` ,\ ``configs`` folder and executable named Penta to home directory
* Give executable permission to Penta.sh and copy\move it to /bin folder(linux bin folder and be sure that its on $PATH)
* (Optional)Now edit your ``.bashrc`` file and add a alias at the end of it: ``alias penta=Penta.sh``

**NOTE** Please be sure that your /bin directory is on $PATH. 

Uninstallation:
^^^^^^^^^^^^^^^

Uninstallation in windows is pretty straightforward ,you just uninstall it like other softwares but there is no uninstalller for linux.delete Penta.sh from /bin folder,edit ``.bashrc`` file and remove the alias if any. and also remove the folder named ``bin``\ ,\ ``configs`` and Penta from home directory.

Build from source
-----------------

Windows/Linux:
^^^^^^^^^^^^^^

Penta can be built from pyinstaller,py2exe and Nuitka.
`Icon <https://www.flaticon.com/free-icon/command-window_656>`_ used in Building Penta.

**\ `Nuitka(Recommended) <https://nuitka.net/>`_\ **\ (\ `User manual <https://nuitka.net/doc/user-manual.html>`_\ ):


* First install nuitka using ``pip install Nuitka``.
* Now open cmd in same Folder as the Project Folder and Type ``python3 -m nuitka --plugin-enable=tk-inter --windows-icon-from-ico=IconFileIfAnyIfNotThenSkipThisFlag --standalone Penta.py``\ (for linux remove the windows related flags)
* For the First time it's going to take some time depending on your network speed as nuitka installs a gcc compiler,for all the messages press Y.
* Your Executable will be compiled in Penta.dist.All the files in the dist folder are necessary to run Penta.if you want to make a single file executable then you can use the --onefile flag but i wouldn't recommend it. 

**\ `Py2exe <https://www.py2exe.org/>`_\ **\ :


* First install py2exe using ``pip install py2exe``.
* Now Create a file named setup.py or whatever.
* if you want to add icon *then*\ :
  .. code-block::

     from distutils.core import setup
     import py2exe
     setup_dict = dict(console=[{'script':'Penta.py','icon_resources':[(0,'ICON.ico')]}])
     setup(**setup_dict)

* Otherwise there is no need to create a dictionary i.e:
  .. code-block::

     from distutils.core import setup
     import py2exe
     setup(console=['Penta.py'])
  -now use python setup.py py2exe to build it.

**\ `Pyinstaller <https://www.pyinstaller.org/>`_\ **


* install pyinstaller using ``pip install pyinstaller``
* Now just cd to Project Folder and use ``pyinstaller --icon IconFileIfAny --onefile Penta.py``
* Your project will be built under the dist directory.

Bug report
^^^^^^^^^^

Found any bug!
Report it to me at x-neron@pm.me
or open an `issue <https://github.com/Justaus3r/Penta/issues>`_

Contributions:
^^^^^^^^^^^^^^

All contributions are welcomed.fork this repo,improve it and `pull requests <https://github.com/Justaus3r/Penta/pulls>`_

License
^^^^^^^

Distributed under GPLV3.0

Note:
^^^^^

A General documentation is also available at `readthedocs.io <https://penta.readthedocs.io/en/latest/>`_.Feel free to improve the doc.you can do so by editing this `File <https://github.com/Justaus3r/Penta/blob/main/docs/index.rst>`_.
