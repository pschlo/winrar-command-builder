from pathlib import PurePath, Path
from .console_command import ConsoleCommand, build_sfx_comment
from .command_parts import commands, switches, sfx
import tempfile
import subprocess
from typing import Literal


def create_command(
        winrar_path:str,
        source_path:str,
        output_path:str,
        comment_path:str,
        compression_strength: int = 3,
        archive_format: Literal['rar'] | Literal['zip'] = 'rar',
    ) -> ConsoleCommand:

    return \
        ConsoleCommand(
            winrar_path = winrar_path,
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
                switches.COMMENT(comment_path)
            ],
            archive = output_path,
            files = source_path
        )



def create_comment(exe_path:str, title:str) -> str:
    return build_sfx_comment([
        sfx.EXECUTE_FILE(exe_path),
        sfx.TEMP_MODE,
        sfx.OVERWRITE,
        sfx.TITLE(title)
    ])



def create_exe(
        winrar_path: str,
        # note that if path points to a folder, the folder itself is also included in the archive
        # use <path_to_dir>/* to only include the files
        source_path: str,
        # exe file that gets executed after unpacking
        exe_path: str,
        # gets put in current working directory if None
        # if path points to directory, the exe_path filename is used
        output_path: str|None = None,
        title: str = 'Self-extracting archive',
        # ranges from 0 (fastest) to 5 (slowest)
        compression_strength: int = 3,
        # some stackoverflow post recommended rar
        archive_format: Literal['rar'] | Literal['zip'] = 'rar',
    ) -> None:

    if output_path is None:
        # output to working directory and choose same name as the file that gets executed internally
        output_path = Path(exe_path).name
    if Path(output_path).is_dir():
        # output path must point to file
        output_path = str(Path(output_path) / Path(exe_path).name)

    # create temporary file with comment
    comment = create_comment(exe_path, title)

    with tempfile.NamedTemporaryFile('w', delete=False) as comment_file:
        comment_path = comment_file.name
        comment_file.write(comment)

    command = \
        create_command(
            winrar_path,
            source_path,
            output_path=output_path,
            comment_path=comment_path,
            compression_strength=compression_strength,
            archive_format=archive_format
        )
    
    subprocess.run(command.as_list())
    # delete temporary comment file
    Path(comment_path).unlink()
