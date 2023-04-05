# Pyside6 Deployment Test

This is a test project and is **not working**.

Qt recommends to use Nuitka for Pyside6 application deployment. This works on a
Desktop computer, but cannot be executed via Github Actions. Reported in 
[Nuitka issue #2138](https://github.com/Nuitka/Nuitka/issues/2138).


## Nuitka Executable Error from Github Actions
```bash
# Download created executable from Github Actions and add executable flag
$ chmod +x main

# Start executable
$ ./main
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, vkkhrdisplay, minimal, offscreen, wayland-egl, wayland, vnc, minimalegl, linuxfb, xcb.
```

## Nuitka works from Ubuntu Desktop computer

```bash
$ cd <this project>
$ virtualenv /tmp/venv
$ source /tmp/venv/bin/activate
$ pip install pyside6
$ pyside6-deploy -c pysidedeploy.spec
...
[DEPLOY] Executed file created in <project>/main.bin

# Start created executable
$ ./main

==> Pyside6 executable starts correctly <==
```

