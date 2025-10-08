from enum import Enum

class ResponseSignal(str, Enum):
    FILE_VALIDATED_SUCCESS = "File Validated Success"
    FILE_UPLOADED_FAIL = "File Uploaded Fail"
    FILE_UPLOADED_SUCCESS = "File Uploaded Success"
    FILE_TYPE_NOT_SUPPORTED = "File Type Not Supported"
    FILE_SIZE_EXCEEDED = "File Size Exceeded"