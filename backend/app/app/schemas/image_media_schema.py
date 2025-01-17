from app.models.image_media_model import ImageMediaBase
from .media_schema import IMediaRead
from app.utils.partial import optional
from typing import Optional

# Image Media
class IImageMediaCreate(ImageMediaBase):
    pass


# All these fields are optional
@optional
class IImageMediaUpdate(ImageMediaBase):
    pass


class IImageMediaRead(ImageMediaBase):
    media: Optional[IMediaRead]
