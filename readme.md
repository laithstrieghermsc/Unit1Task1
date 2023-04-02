# Shuffle 
![MSC]
![laith.striegher]
 [![License][License: GPL v3]][License URL]

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

## Installation

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

<!-- LICENSE -->
## License

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