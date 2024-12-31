import os
import shutil

def clean_pycache():
    for root, dirs, files in os.walk('.'):
        for d in dirs:
            if d == '__pycache__':
                shutil.rmtree(os.path.join(root, d))
                print(f'Removed: {os.path.join(root, d)}')
