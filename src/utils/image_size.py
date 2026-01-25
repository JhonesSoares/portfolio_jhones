import os

from django.conf import settings
from PIL import Image

# REDIMENSIONAMENTO DE IMAGEM


class imageSize:
    def resize_image(self, img, new_width):
        img_full_path = os.path.join(
            settings.MEDIA_ROOT,
            img.name,
        )
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width >= new_width:
            new_height = round((new_width * original_height) / original_width)
            new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
            new_img.save(img_full_path, optimize=True, quality=50)
            return

        img_pil.close()
        return
