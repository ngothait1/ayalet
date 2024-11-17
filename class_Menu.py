from enum import Enum, auto


class Menu(Enum):
    SAVE_NEW_ENTRY = auto()
    SEARCH_BY_ID = auto()
    PRINT_AGES_AVERAGE = auto()
    PRINT_ALL_NAMES = auto()
    PRINT_ALL_IDS = auto()
    PRINT_ALL_ENTRIES = auto()
    PRINT_ENTRY_BY_INDEX = auto()
    SAVE_ENTRY_TO_CSV_FILE = auto()
    EXIT = auto()
