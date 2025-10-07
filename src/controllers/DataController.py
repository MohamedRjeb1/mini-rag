from .BaseController import BaseController
from fastapi import UploadFile

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_limit = 1048576
    
    def validate_uploaded_file(self, file: UploadFile):
        
        if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSIONS:
            return False, f"File type {file.content_type} is not allowed."
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_limit:
            return False

        return True