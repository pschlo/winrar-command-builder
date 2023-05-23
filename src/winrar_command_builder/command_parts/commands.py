class Command:
    def __init__(self, text:str) -> None:
        self.text = text

    def __str__(self) -> str:
        return self.text
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Command) and self.text == other.text:
            return True
        return False

    def __hash__(self) -> int:
        return hash(self.text)


# add files to an archive
ARCHIVE = Command('a')

# add an archive comment
COMMENT = Command('c')

# delete files from an archive
DELETE = Command('d')

# lock an archive
LOCK = Command('k')

# test archive files
TEST = Command('t')

# extract files from an archive with full paths
EXTRACT = Command('x')

# extract files from an archive, ignoring paths
EXTRACT_IGNORE_PATH = Command('e')
