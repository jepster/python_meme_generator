import os
import textwrap

from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """ The engine behind meme generation """
    def __init__(self, output_dir):
        """ Save and create the output directory path """
        self.output_dir = output_dir
        self.count = 1
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500):
        """ Create a meme using the given image, text and author """
        img = Image.open(img_path)
        outfile = os.path.join(self.output_dir, f"temp-{self.count}.jpg")
        self.count += 1
        real_width, real_height = img.size
        height = int(real_height * width / real_width)
        img.thumbnail((width, height))

        # Select font-family, font-size, color and position to draw text
        font1 = ImageFont.truetype("./_data/Fonts/Roboto-Bold.ttf", 22)
        font2 = ImageFont.truetype("./_data/Fonts/Roboto-Medium.ttf", 18)
        text_position = 25
        fill = (0, 0, 0)
        stroke_fill = (255, 255, 255)

        # Draw the text on image
        draw = ImageDraw.Draw(img)

        my_wrap = textwrap.TextWrapper(width=25)
        wrap_list = my_wrap.wrap(text)

        for text_chunk in wrap_list:
            draw.text((30, text_position), text_chunk, fill, font1,
                      stroke_width=1, stroke_fill=stroke_fill)
            text_position += 35

        draw.text((30, text_position + 25), f"- {author}", fill, font2,
                  stroke_width=1, stroke_fill=stroke_fill)

        img.save(outfile, "JPEG")
        return outfile

    def create_text_chunks(self, text):
        x = 20
        text_pieces = [text[y - x:y] for y in range(x, len(text) + x, x)]
        return text_pieces