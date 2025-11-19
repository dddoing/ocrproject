"""
Helper utility functions
"""
import os
from datetime import datetime, timedelta
from pathlib import Path


def cleanup_old_files(directory: str, hours: int = 24):
    """
    Delete files older than specified hours

    Args:
        directory: Directory to clean
        hours: Age threshold in hours
    """
    path = Path(directory)
    if not path.exists():
        return

    cutoff = datetime.now() - timedelta(hours=hours)

    for file in path.iterdir():
        if file.is_file():
            if datetime.fromtimestamp(file.stat().st_mtime) < cutoff:
                file.unlink()


def ensure_directory(path: str):
    """Create directory if it doesn't exist"""
    Path(path).mkdir(parents=True, exist_ok=True)


def format_file_size(bytes: int) -> str:
    """Format bytes to human-readable file size"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024.0:
            return f"{bytes:.1f}{unit}"
        bytes /= 1024.0
    return f"{bytes:.1f}TB"
