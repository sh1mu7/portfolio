import os
from io import BytesIO
from PIL import Image
from django.core.files import File


def image_optimizer(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'WEBP', quality=50)
    new_image = File(im_io, name=image.name.split('.')[0] + '.webp')
    return new_image


def thumb_generator(thumbnail):
    with Image.open(thumbnail) as im:
        im.thumbnail((128, 128))
        im_io = BytesIO()
        im.save(im_io, 'webp', quality=80)
        new_thumbnail = File(im_io, name=os.path.splitext(thumbnail.name)[0] + '_thumb.jpg')
        return new_thumbnail

