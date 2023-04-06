[![Create PySide6 exe with Nuitka-Action](https://github.com/Erriez/pyside6-nuitka-deployment/actions/workflows/build.yml/badge.svg)](https://github.com/Erriez/pyside6-nuitka-deployment/actions/workflows/build.yml)
[![Licence MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/Erriez/pyside6-nuitka-deployment/blob/master/LICENSE)
[![Pyside6](https://img.shields.io/badge/pyside6-v6.5.0-informational)](https://github.com/Erriez/pyside6-nuitka-deployment)
[![Open issue](https://shields.io/github/issues-raw/Erriez/pyside6-nuitka-deployment)](https://github.com/Erriez/pyside6-nuitka-deployment/issues)

# Pyside6 Deployment Test

This is a Pyside6 test project using Nuitka build for Windows and linux with
Github Actions. Other operating systems are not supported by the developer of
this repository.

![Pyside6 app screenshot](screenshots/app-screenshot.png)

Qt recommends [Nuitka](https://doc.qt.io/qtforpython-6/deployment/deployment-nuitka.html) 
to create Pyside6 executables for Windows and Linux.

## Download executables from Github Actions

Visit [Actions](https://github.com/Erriez/pyside6-nuitka-test/actions), open
a build and download `Linux Build` or `Windows Build` under `Artifacts`.

## Build executable

```bash
# Clone project
$ git clone https://github.com/Erriez/pyside6-nuitka-deployment.git
$ cd pyside6-nuitka-deployment

# Install Linux system dependencies
$ sudo apt install python3-virtualenv ccache clang patchelf

# Create virtual environment
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pip install nuitka
```

## Build executable on Ubuntu/Mint 22.04/22.10 Desktop

```bash
# Build executable for Linux
$ python3 -m nuitka \
    --output-dir=output \
    --output-file=pyside6-app \
    --onefile \
    --enable-plugin=pyside6 \
    --include-data-dir=images=images \
    main.py

# Start created executable
$ ./pyside6-app
```

## Build executable on Windows 10/11 Desktop

```
# Build executable for Windows
$ python3 -m nuitka \
    --output-dir=output \
    --output-file=pyside6-app.exe \
    --onefile \
    --enable-plugin=pyside6 \
    --include-data-dir=images=images \
    --disable-console=true \
    --windows-icon-from-ico=images/app.ico \
    main.py

# Start created executable
> .\pyside6-app.exe
```


## MIT License

This project is published under [MIT license](https://github.com/Erriez/pyside6-nuitka-deployment/blob/master/LICENSE)
with an additional end user agreement (next section).


## End User Agreement :ukraine:

End users shall accept the [End User Agreement](https://github.com/Erriez/pyside6-nuitka-deployment/blob/master/END_USER_AGREEMENT.md)
holding export restrictions to Russia to stop the WAR before using this project.

