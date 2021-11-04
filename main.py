import argparse
import os
import operator
import random

from lfsr import LFSR
from PIL  import Image

def encrypt(image_path: str, password: int, tap_code: int, _reverse: bool=False):
    
    operation = operator.sub if _reverse else operator.add

    lfsr_gen = LFSR(password, tap_code)

    img = Image.open(image_path).convert("RGB")
    img_copy = img.copy()

    for i in range(img_copy.width):
        for j in range(img_copy.height):
            red, green, blue = img_copy.getpixel((i, j))

            red   = operation(red, lfsr_gen.next_bits(8)) % 256
            green = operation(green, lfsr_gen.next_bits(8)) % 256
            blue  = operation(blue, lfsr_gen.next_bits(8)) % 256
            
            img_copy.putpixel((i, j), (red, green, blue))

    return img_copy

def save_img(img, path):
    name, ext = path.rsplit("/", maxsplit=1)[-1].rsplit(".", maxsplit=1)
    new_name  = f"{name}{random.choice(range(10))}.{ext}"

    img.save(new_name)
    return new_name

def main():

    parser = argparse.ArgumentParser()

    option = parser.add_mutually_exclusive_group(required=True)
    option.add_argument("-e", "--encrypt", action="store_true", help="encrypt image")
    option.add_argument("-d", "--decrypt", action="store_true", help="decrypt image")
    
    parser.add_argument("-i", "--image-path", type=str, required=True, help="full path of image")
    parser.add_argument("-p", "--password", type=int, required=True, help="password to encrypt/decrypt image")
    parser.add_argument("-t", "--tap-code", type=int, required=True, help="tap-code to encrypt/decrypt image")

    args = parser.parse_args()

    if not os.path.exists(args.image_path):
        print(f"error: {args.image} not found")
        return

    img     = encrypt(args.image_path, args.password, args.tap_code, args.decrypt)
    new_img = save_img(img, args.image_path) 
    print(f"info: {chr(100) * args.decrypt}e{chr(110) * args.encrypt}crypted image saved as {new_img}")
        
if __name__ == "__main__":

    main()  