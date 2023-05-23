from .command_parts.commands import Command
from .command_parts.switches import Switch
from .command_parts.sfx import SfxCommand



# Creates comment that contains SFX script commands
def build_sfx_comment(commands:list[SfxCommand]) -> str:
    return '\n'.join(map(str,commands))


class ConsoleCommand:
    def __init__(
            self,
            winrar_path: str,                        # path to winrar executable
            command: Command,                        # specifies the function to be performed by WinRAR
            switches: Switch|list[Switch]|None,      # define a specific type of operation, compression strength, type of archive, etc.
            archive: str,                            # name of the archive to process.
            files: str|list[str]|None = None,        # name(s) of files to be processed.
            listfiles: str|list[str]|None = None,    # plain text files that contain names of files to process.
        ) -> None:

        self._winrar_path: str = winrar_path
        self.command: Command = command

        if switches is None:
            switches = []
        if isinstance(switches, Switch):
            switches = [switches]
        self.switches: list[Switch] = switches

        self.archive: str = archive

        if files is None:
            files = []
        if isinstance(files, str):
            files = [files]
        self.files: list[str] = files

        if listfiles is None:
            listfiles = []
        if isinstance(listfiles, str):
            listfiles = [listfiles]
        self.listfiles: list[str] = listfiles

    
    
    def as_list(self):
        return \
            [self._winrar_path] +\
            [str(self.command)] +\
            [str(s) for s in self.switches] +\
            [self.archive] +\
            [str(f) for f in self.files] +\
            [str(f) for f in self.listfiles]
    
    def __str__(self) -> str:
        return ' '.join(self.as_list())