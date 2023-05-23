# winrar-command-builder
Constructs WinRAR CLI commands



### Example

```python
from winrar_command_builder.sfx_template import create_exe

winrar = r'C:\Program Files\WinRAR\WinRAR.exe'
source = r'./dist/my-app/*'
exe = 'launch-app.exe'
title = 'My App'

create_exe(winrar, source, exe_path=exe, output_path='.', title=title)
```

