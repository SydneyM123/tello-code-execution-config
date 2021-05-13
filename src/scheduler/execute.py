'''
    1. Add all ready-files to list

    2. Get first created ready-file
    
    3. List running Docker containers
    
    4. Stop executing this file if there is already a python script running

    5. Execute ready-file

    6. Remove ready-file from ready-files directory
'''

import os
from pathlib import Path


paths = sorted(Path("./ready-files/").iterdir(), key=os.path.getmtime)
print(paths)
