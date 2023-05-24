# winrar-command-builder
Constructs WinRAR CLI commands



### Example

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

Launching this script will create the file `launch-app.sfx.exe` in your project folder. If you want a different name, try modifying the `dest` argument:

```python
...
dest = project_path / 'my-app.exe'
...
```

