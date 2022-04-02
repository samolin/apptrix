from PIL import Image
import os
from io import StringIO, BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

#from apptrix.settings import BASE_DIR

def watermark_with_transparency(input_image_path,
                                watermark_image_path='/Users/vlad/PycharmProjects/RESTfull/apptrix_test/apptrix/watermark.png'):
    size = (200,300)
    base_image = Image.open(input_image_path).convert('RGBA')
    watermark = Image.open(watermark_image_path).convert('RGBA')
    #watermark.putalpha(128) - прозрачность
    watermark.thumbnail(size)
    base_image.thumbnail(size) # - миниатюра, настраивается размер в пискселях 
    watermarked = Image.new('RGBA', size = size, color=(0,0,0,0))
    watermarked.paste(base_image)
    watermarked.paste(watermark, mask=watermark)
    #watermarked.show()
    #watermarked = watermarked.convert('RGBA')
    result = get_bytes_value(Image.open(watermarked))
   
    #watermarked.show()
    #transparent.paste(watermark, position, mask=watermark)
    #transparent.save(output_image_path)
    return result
    

def get_bytes_value(image):
    print(image)
    buffer = StringIO()
    print('BUFFFFFERRRRRRRRRRRR', buffer)
    image.save(buffer, "PNG")
    image_file = InMemoryUploadedFile(buffer, None, 'test.png', 'image/png', buffer.len, None)
    print(type(image_file)+'lol')
    #img_bytes_arr = io.BytesIO()
    #image.save(img_bytes_arr, format='JPEG')
    #imb_bytes_arr = img_bytes_arr.getvalue()
    return image_file


if __name__ == '__main__':
    img = 'apptrix/media/avatars/джеймс_кэмерон.jpeg'
    watermark_with_transparency(img)



