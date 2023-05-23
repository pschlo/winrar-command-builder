from pathlib import PurePath, Path
from .console_command import ConsoleCommand, build_sfx_comment
from .command_parts import commands, switches, sfx
import tempfile
import subprocess
from typing import Literal
import time
from .typedefs import PathType



def create_command(
        winrar: PathType,
        source: PathType,
        dest: PathType,
        comment: PathType,
        compression_strength: int = 3,
        archive_format: Literal['rar'] | Literal['zip'] = 'rar',
    ) -> ConsoleCommand:

    return \
        ConsoleCommand(
            winrar = winrar,
            command = commands.ARCHIVE,
            switches = [
                switches.EXCLUDE_BASE_DIR,
                switches.SELF_EXTRACTING(),
                switches.LOCK_ARCHIVE,
                switches.IGNORE_DEFAULT_PROFILE,
                switches.ARCHIVE_FORMAT(archive_format),
                switches.EXCLUDE_EMPTY_DIRS,
                switches.COMPRESSION_METHOD(compression_strength),
                switches.RECURSE_SUBFOLDERS,
                switches.ARCHIVE_TIME_AS_NEWEST_FILE,
                switches.COMMENT(comment)
            ],
            archive = dest,
            files = source
        )



def create_comment(program:str, title:str) -> str:
    return build_sfx_comment([
        sfx.SETUP(program),
        sfx.TEMP_MODE,
        sfx.OVERWRITE,
        sfx.TITLE(title)
    ])



def create_exe(
        winrar: PathType,
        # path to the source directory
        # note that the directory itself is excluded; only its contents are archived
        source: PathType,
        # program that gets executed after unpacking
        # temp folder gets set as working directory
        program: str,
        # if path points to directory, the output file's name is the current timestamp
        dest: PathType = '.',
        title: str = 'Self-extracting archive',
        # ranges from 0 (fastest) to 5 (slowest)
        compression_strength: int = 3,
        # some stackoverflow post recommended rar
        archive_format: Literal['rar'] | Literal['zip'] = 'rar'
    ) -> None:

    winrar = Path(winrar)
    if not winrar.exists():
        raise ValueError('WinRAR path does not exist')

    source = Path(source)
    if not source.exists():
        raise ValueError('Source path does not exist')
    if not source.is_dir():
        raise ValueError('Source must be a directory')

    # determine name of the output archive in case none was provided
    # if 'program' is a file, use its name
    program_path = source / program
    if program_path.exists():
        output_name = program_path.stem
    # otherwise, use the source directory name
    else:
        output_name = source.name

    # exclude source directory itself
    source = Path(source) / '*'

    # set output path
    dest = Path(dest)
    if dest.is_dir():
        # output path must point to file
        # timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        dest = dest / f'{output_name}.sfx.exe'
    if not dest.parent.exists():
        raise ValueError('Destination path does not exist')

    comment = create_comment(program, title)

    # create temporary file and write sfx comment
    with tempfile.NamedTemporaryFile('w', delete=False) as comment_file:
        comment_path = Path(comment_file.name)
        comment_file.write(comment)

    command = \
        create_command(
            winrar,
            source,
            dest=dest,
            comment=comment_path,
            compression_strength=compression_strength,
            archive_format=archive_format
        )
    
    # run winrar command
    process = subprocess.run(command.as_list())

    # delete temporary comment file
    comment_path.unlink()

    # raise exception if sfx creation failed
    process.check_returncode()
