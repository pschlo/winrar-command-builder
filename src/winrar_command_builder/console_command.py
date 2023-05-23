from .command_parts.commands import Command
from .command_parts.switches import Switch
from .command_parts.sfx import SfxCommand
from pathlib import Path
from .typedefs import PathType, AnyPathType



# Creates comment that contains SFX script commands
def build_sfx_comment(commands:list[SfxCommand]) -> str:
    return '\n'.join(map(str,commands))


class ConsoleCommand:
    def __init__(
            self,
            winrar: PathType,                                   # path to winrar executable
            command: Command,                                   # specifies the function to be performed by WinRAR
            switches: Switch | list[Switch] | None,             # define a specific type of operation, compression strength, type of archive, etc.
            archive: PathType,                                  # name of the archive to process.
            files: PathType | list[PathType] | None = None,     # name(s) of files to be processed.
            listfiles: PathType| list[PathType] | None = None,  # plain text files that contain names of files to process.
        ) -> None:

        self.winrar: Path = Path(winrar)
        self.command: Command = command

        if switches is None:
            switches = []
        if isinstance(switches, Switch):
            switches = [switches]
        self.switches: list[Switch] = switches

        self.archive: Path = Path(archive)

        if files is None:
            files = []
        if isinstance(files, AnyPathType):
            files = [files]
        self.files: list[Path] = [Path(f) for f in files]

        if listfiles is None:
            listfiles = []
        if isinstance(listfiles, AnyPathType):
            listfiles = [listfiles]
        self.listfiles: list[Path] = [Path(f) for f in listfiles]


    def as_list(self) -> list[str]:
        return \
            [str(self.winrar)] +\
            [str(self.command)] +\
            [str(s) for s in self.switches] +\
            [str(self.archive)] +\
            [str(f) for f in self.files] +\
            [str(f) for f in self.listfiles]
    
    def __str__(self) -> str:
        return ' '.join(self.as_list())