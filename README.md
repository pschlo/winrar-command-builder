# winrar-command-builder
[WinRAR](https://www.win-rar.com) is a file archiver utility for Windows. Its main purpose is to create, view and unpack `zip` and `rar` archives.

Additionally, WinRAR can be used to create [self-extracting archives](https://en.wikipedia.org/wiki/Self-extracting_archive) (SFX). SFX are executable files that contain an archive which they decompress upon execution. They can also be configured to then run a program from the extracted archive. This is very handy for creating easily distributable, standalone Windows applications. SFX can be created from both the WinRAR GUI and the command line. The commands are, however, quite obscure and difficult to remember.

This project provides a simple interface for constructing complex WinRAR commands. It also contains ready-to-use template functions for creating SFX archives.



## Example

Assume you have a project called `My App` and a project directory that looks like this:

```
my-app/
   README.md
   src/
   dist/
      lib/
      ...
      launch-app.exe
   build-exe.py
```

The source codes resides in `src` and is compiled to `dist`. You now want to bundle `dist` in a single `.exe` file. For this, you have created a `build-exe.py` script like this:

```python
from winrar_command_builder.sfx_template import create_exe
from pathlib import Path

project_path = Path(__file__).resolve().parent

winrar = r'C:\Program Files\WinRAR\WinRAR.exe'
source = project_path / 'dist'
program = 'launch-app.exe'
dest = project_path
title = 'My App'

create_exe(winrar, source, program, dest, title)
```

Running this script will create the file `launch-app.sfx.exe` in your project folder. If you want a different name, try modifying the `dest` argument:

```python
...
dest = project_path / 'my-app.exe'
...
```



## Additional Details

The default SFX template `create_exe` creates executables that:

* **extract** the archive to a temporary directory (usually in `%tmp%`) without asking for confirmation, but with visual feedback
* **run** the program and wait for it to finish
* **delete** the temporary directory
