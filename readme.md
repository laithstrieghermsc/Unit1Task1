# Shuffle 
![MSC]
![laith.striegher]

A classic puzzle game by Laith Striegher


<!-- ABOUT THE PROJECT -->
## About The Project
This simple shuffle game was created for Computer Science ATAR Unit 1, Task 1 Year 11

<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

To run the program you require;

One of:

![Windows 10/11]
![MacOSX]
![Debian]

With a desktop environment and

All of:

![Python3]
[![RDM][random]][random URL]
[![TKN][tkinter]][tkinter URL]
[![PIL][Pillow]][Pillow URL]


### Windows 10/11
This will show you how to install Python3, Pip3, and Pillow on Windows 10/11.

Step 1: Download Python3
* Go to the Python download page and click on the "Download Python 3.x.x" button (x.x.x represents the latest version).
* Scroll down and select the appropriate version for your operating system (32-bit or 64-bit).
* Click on the "Download" button to start the download.

Step 2: Install Python3
* Double-click the downloaded file to start the installation process.
* Select "Add Python X.X to PATH" (X.X represents the version number) and click on the "Customize installation" button.
* Choose the components you want to install and click on the "Next" button.
* Select the installation directory and click on the "Install" button.
* Wait for the installation to complete.

Step 3: Download Pip3
* Go to the [Pip download page](https://bootstrap.pypa.io/get-pip.py) and download the "get-pip.py" file.
* Save the file to your computer.

Step 4: Install Pip3
* Open the command prompt by pressing the "Windows" key and typing "cmd".
* Right-click on the "Command Prompt" option and select "Run as administrator".
* Navigate to the directory where the "get-pip.py" file is saved using the "cd" command (e.g. `cd C:\Users\Username\Downloads`).
* Type `python3 get-pip.py` and press "Enter".
* Wait for the installation to complete.

Official installation guides [here](https://pip.pypa.io/en/stable/installation/)

Step 5: Download Pillow
* Open the command prompt by pressing the "Windows" key and typing "cmd".
* Right-click on the "Command Prompt" option and select "Run as administrator".
* Type `pip install pillow` and press "Enter".
* Wait for the installation to complete.

Step 6: Verify the Installation
* Open the command prompt by pressing the "Windows" key and typing "cmd".
* Type `python3` and press "Enter" to open the Python interpreter.
* Type `import pillow` and press "Enter".
* If no error message appears, Pillow has been installed successfully.

You have successfully installed Python3, Pip3, and Pillow on your Windows 10/11 system.


### Debian
Installing Python3 and pip3 on Debian

Step 1. First, update the package list using the following command:
```sh
sudo apt update
```

Step 2. Once the update process completes, install Python3 and pip3 by running the following command:
```sh
sudo apt install python3 python3-pip
```

Step 3. After the installation process completes, verify the installation of Python3 and pip3 using the following commands:
```sh
python3 --version
pip3 --version
```

Installing Pillow on Debian

Step 1. Install the required dependencies for Pillow using the following command:
```sh
sudo apt install libjpeg-dev zlib1g-dev libtiff-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk
```

Step 2. Once the dependencies are installed, install Pillow using pip3:
```sh
sudo -H pip3 install Pillow
```

Step 3. After the installation process completes, verify the installation of Pillow using the following command:
```sh
python3 -c "import PIL; print(PIL.__version__)"
```

Pillow is now successfully installed on your Debian system.


### MacOSX

Step 1. Check if Python3 is already installed on your system by typing the following command in Terminal:
```sh
python3 --version
```

Step 2. If Python3 is not installed, download the latest version from the [official Python website](https://www.python.org/downloads/)

Step 3. Once the download is complete, double-click on the downloaded file to launch the Python installer and follow the instructions to complete the installation process.

Step 4. Check if pip3 is installed by typing the following command in Terminal:
```sh
pip3 --version
```

Step 5. If pip3 is not installed, download the get-pip.py script by typing the following command in Terminal:
```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Step 6. Once the download is complete, navigate to the directory where the get-pip.py script is saved and run the following command in Terminal:
```sh
sudo python3 get-pip.py
```

Step 7. After pip3 is installed, you can use it to install Pillow by typing the following command in Terminal:
```sh
sudo pip3 install pillow
```

Step 8. Pillow should now be installed on your system. You can check its version by typing the following command in Terminal:
```sh
python3 -c "import PIL; print(PIL.version)"
```

That's it! You now have Python3, pip3, and Pillow installed on your MacOSX system.




<!-- USAGE EXAMPLES -->
## Usage

logic.py


<!-- LICENSE -->
## License [![License][License: GPL v3]][License URL]

Distributed under the GNU Public License. See `LICENSE.txt` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
[Windows 10/11]: https://img.shields.io/badge/OS-Windows%2010%2F11-ff595e?style=for-the-badge
[MacOSX]: https://img.shields.io/badge/OS-MacOSX-ff595e?style=for-the-badge
[Debian]: https://img.shields.io/badge/OS-Debian-ff595e?style=for-the-badge
[Pillow]: https://img.shields.io/badge/PYPI-PILLOW-g?style=for-the-badge&logo=data:image/png;base64,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
[Pillow URL]: https://pypi.org/project/Pillow/
[tkinter]: https://img.shields.io/badge/BUILTIN-tkinter-g?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABzElEQVQ4jYWTP28TQRDF3x6HaI8eiYgSkOyCDiS7BqREygdI0lEGJEQJ6UH2R3BN5XwC24j0vhaaIArKuMr92XlvKO5sh7NEVho9aTU7vzc7uwGd9XI06yPqo5kNXcwsRkhcWaynd8vi7Xx8srqZn3QLIPpY5DlkC5pBImiWuXRcJHcm3fS0uyEaKA5k9lAUZAYn0RbLuvk7DihOaPaL0rloZxJBbpzsGE4B4NXn2US0fZIZY9wS/1HCKfifd3OEMIBsiiqcpK+/zD7R7Ihbm1viDXURDgEhAVQBqg+QxDyR8UDUDnHbOyES7g4guYQVGVgCVgAqhinF3pqglihjTmolWntYgIflxYf8HlT2oBpQDbAepF3yswdX70eHP58DyIAAOAGPAKsjeMzAClBsCigilZiT1mt6ZT46/PECCPsA2oMtbSciwDpPRE63c7YVHM2sWQEsARaAWmXZRtXcgcdJigRjyvYk7tFsCai/obIGPC62tlv1CkC4DE8vxqH7MPz3mzm8HoDVuvc53Bqq13l4/O30/39hY7ta6xB2HaByAbf+rU8Zur7czHkz7+iQHEiWtxYIj74eg8UZVOTNRRkAvw8kITz5ftrN/wssndHnwE4jjAAAAABJRU5ErkJggg==
[tkinter URL]: https://docs.python.org/3/library/tkinter.html
[random]: https://img.shields.io/badge/BUILTIN-random-g?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABzElEQVQ4jYWTP28TQRDF3x6HaI8eiYgSkOyCDiS7BqREygdI0lEGJEQJ6UH2R3BN5XwC24j0vhaaIArKuMr92XlvKO5sh7NEVho9aTU7vzc7uwGd9XI06yPqo5kNXcwsRkhcWaynd8vi7Xx8srqZn3QLIPpY5DlkC5pBImiWuXRcJHcm3fS0uyEaKA5k9lAUZAYn0RbLuvk7DihOaPaL0rloZxJBbpzsGE4B4NXn2US0fZIZY9wS/1HCKfifd3OEMIBsiiqcpK+/zD7R7Ihbm1viDXURDgEhAVQBqg+QxDyR8UDUDnHbOyES7g4guYQVGVgCVgAqhinF3pqglihjTmolWntYgIflxYf8HlT2oBpQDbAepF3yswdX70eHP58DyIAAOAGPAKsjeMzAClBsCigilZiT1mt6ZT46/PECCPsA2oMtbSciwDpPRE63c7YVHM2sWQEsARaAWmXZRtXcgcdJigRjyvYk7tFsCai/obIGPC62tlv1CkC4DE8vxqH7MPz3mzm8HoDVuvc53Bqq13l4/O30/39hY7ta6xB2HaByAbf+rU8Zur7czHkz7+iQHEiWtxYIj74eg8UZVOTNRRkAvw8kITz5ftrN/wssndHnwE4jjAAAAABJRU5ErkJggg==
[random URL]: https://docs.python.org/3/library/random.html
[Python3]: https://img.shields.io/badge/Language-PYTHON%203-informational?style=for-the-badge
[License: GPL v3]: https://img.shields.io/badge/License-GPLv3-7b4b94.svg?style=for-the-badge
[License URL]: https://www.gnu.org/licenses/gpl-3.0.en.html
[MSC]: https://img.shields.io/badge/SCHOOL-Mindarie%20Senior%20Collage-292e71?style=for-the-badge&logo=data:image/png;base64,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
[laith.striegher]: https://img.shields.io/badge/STUDENT-Laith%20Striegher-39375b?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA1VJREFUWIXtll1oXEUUx39z0900hfqiUPpilzStLdm7oU2EtqggFmlA4psEGrHGJA1ipdntNkaEBMGWZDehlKYRtLbZ7JoqpWBTu/GDNvTB+pBGNrs3fiA09qGJVhr8SLOb/RgfNrPemw9Mq1GQ/b/cM2fOnP+Z/5wZLuSRx7+Ek+e+aVzML1aS1Bc0JMBDa+1M/TpbmSYTRmhoyEFPjbMSYNVKEPuDo1JSEPfWlApViCDz8gN3E/YJ+4MF5tj7LsAXilUjRT+AIlJkh+bGx3qHH04VrOkXycRzttX2D/fvr0gCyfvlBMAfGuv3BQ3ZHohuVRKbyc3j9r6YBGgPRJ//W6RmAn9obMN8wvfOG4f8oZiF3B8clQDDw9J25PT1maVyLusIuvoie9JiVdgstbmI23Fqm/c6LXOS7FFXVIgkUATQEYiEC222JxOJVOHhfa7lXQBf0JC+kPHKsoLnrVN2R280Z38w8F0jgO9MViFNTRw9M1qu7LHxO+/7gobs6ItJb02p8O4tPXGvBQB0BUaq5/tu3km0AkiRFWDF3gHDkPZLX419TCq9LSPlM80vln0J0H46skPTtM+8L+hrzf20Iug+G93qD1qbE6D34rcLfHmg624JUFbm3qZsl8vTb55T3107X5+L9eSkdDn/tFXcwQOnPrKu9yyQXjMPdN0tMxlG5gddOH6gSCUBUEYk0ikAysu9r43GOoWuu2fNuS4PGVXmPAJwOQ9airAUIIS2LhrtWvRmmP3Tv8ep2O6VqqjkbOZodr2cMsdLYd2wEBkKC208Wu7NN+Hy8cSuhXKVOF66tlT8puL6HoCNxXUzAFs2N0iAkuL6RWXP9UDJxjpLUodj3+qlSL4fP7XzrwpfACHZVFy76G/Zf4pcZzscbUvu+J+GwwFDQ21xi/Ppp1qvAbxa190TePeT8OeDI5821HbfAqip7pzZ7mraA6DrTRPPVh2RACePX7zqcrq/VjmqKt+caGkJxR5/rCUMsHt32y3n3GOm8MONnyYGzn2xRY1zPTB5+7cmgBTgPzY4Xtd4oernH6emAYJnPUWzGWHMhb6VTqRuAPS8c6UB5NsqxyOb1zdfGhg5Eb+b7bfJyV+mtXTKstFEIrnmjdbz9fcsWx7/W/wBc6BY0QeRxc4AAAAASUVORK5CYII=