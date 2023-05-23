

class SfxCommand:
    def __init__(self, text:str) -> None:
        self.text = text

    def __str__(self) -> str:
        return self.text
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, SfxCommand) and self.text == other.text:
            return True
        return False

    def __hash__(self) -> int:
        return hash(self.text)



def SETUP(program:str):
    return SfxCommand(f'Setup={program}')

TEMP_MODE = SfxCommand('TempMode')

OVERWRITE = SfxCommand('Overwrite=1')

def TITLE(text:str):
    return SfxCommand(f'Title={text}')

