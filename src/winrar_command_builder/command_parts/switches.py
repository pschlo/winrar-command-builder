from typing import Any, Literal


class Switch:
    def __init__(self, text:str) -> None:
        self.text = text

    def __str__(self) -> str:
        return self.text
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Switch) and self.text == other.text:
            return True
        return False

    def __hash__(self) -> int:
        return hash(self.text)




# set compression method
# must be value between 0 and 5
# 0.. Store (fastest)
# 5.. Best (slowest)
def COMPRESSION_METHOD(n: int):
    if not (0 <= n <= 5):
        raise ValueError('Compression method must be between 0 and 5')
    return Switch(f'-m{n}')

# specify archive format
def ARCHIVE_FORMAT(type:Literal['rar']|Literal['zip'] = 'zip'):
    return Switch(f'-af{type}')

# ignore default profile and environment variable
# according to a stackoverflow comment:
# 
# "Using Mofi's sugestion, you should use -cfg- switch in order to avoid WinRAR's default settings dependency.
# Otherwise, WinRAR default settings might override your -zOptions.txt file content.
# Cheers!"

IGNORE_DEFAULT_PROFILE = Switch('-cfg-')

# do not add empty folders
EXCLUDE_EMPTY_DIRS = Switch('-ed')

# exclude base folder from names
EXCLUDE_BASE_DIR = Switch('-ep1')

# lock archive
LOCK_ARCHIVE = Switch('-k')

# recurse subfolders
RECURSE_SUBFOLDERS = Switch('-r')

# set archive time to newest file
ARCHIVE_TIME_AS_NEWEST_FILE = Switch('-tl')

# specify SFX icon
def ICON(path:str):
    return Switch(f'-iicon{path}')

# create self-extracting (SFX) archive
def SELF_EXTRACTING(sfx_module_path:str=''):
    return Switch(f'-sfx{sfx_module_path}')

# read archive comment from file
# the comment can be relevant for e.g. SFX archive
# it can be copied from the GUI "comment" field
def COMMENT(file:str):
    return Switch(f'-z{file}')

# request administrative access for SFX archive
REQUIRE_ADMIN = Switch('-iadm')