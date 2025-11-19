"""
Validation utilities
"""
from typing import List

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'pdf'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

SUPPORTED_LANGUAGES = {
    'en': 'English',
    'ko': 'Korean',
    'ja': 'Japanese',
    'zh': 'Chinese',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
}


def validate_file_extension(filename: str) -> bool:
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def validate_file_size(size: int) -> bool:
    """Check if file size is within limit"""
    return size <= MAX_FILE_SIZE


def validate_language_code(code: str) -> bool:
    """Check if language code is supported"""
    return code in SUPPORTED_LANGUAGES


def get_supported_languages() -> List[dict]:
    """Get list of supported languages"""
    return [
        {"code": code, "name": name}
        for code, name in SUPPORTED_LANGUAGES.items()
    ]
