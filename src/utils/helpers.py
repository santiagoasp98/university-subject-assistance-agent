from pathlib import Path
import shutil

def ensure_directory(directory: str) -> Path:
    '''Ensure a directory exists and return its Path object'''
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    return path

def cleanup_directory(directory: str):
    '''Remove all files in a directory'''
    path = Path(directory)
    if path.exists():
        shutil.rmtree(path)
        path.mkdir()