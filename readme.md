<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Shuffle</h3>

  <p align="center">
    A classic puzzle game by Laith Striegher
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#Librarys-Used">Install reqired librarys</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This simple shuffle game was created for Computer Science ATAR Unit 1, Task 1 Year 11


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Librarys Used
I used 3 major librarys for my program. These include: <br>
random (built-in) <br>
tkinter (preinstalled) <br>
pillow (needs to be installed) <br>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Prerequisites

The program is only known to run on the following operating systems:
* Windows 10/11
* MacOSX
* Debian

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Windows 10/11
This will show you how to install Python3, Pip3, and Pillow on Windows 10/11.

Step 1: Download Python3
* Go to the Python download page and click on the "Download Python 3.X.X" button (X.X.X represents the latest version).
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

You have successfully installed Python3, Pip3, and Pillow on your Windows 10/11 machine.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 