class SaveImgError(Exception):
    pass

class UploadPhotoError(Exception):
    def __init__(self, *args) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None
        
    def __str__(self) -> str:
        if self.message:
            return f"{self.message}"
        return "UploadPhotoError has been raised!"