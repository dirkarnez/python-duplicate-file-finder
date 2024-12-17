import duplicates as dup
from pathlib import Path

folder_of_interest_1 = 'C:\\a'
folder_of_interest_2 = 'C:\\b'
df = dup.compare_folders(folder_of_interest_1, folder_of_interest_2, to_csv=True)