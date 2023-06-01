import os
from itertools import repeat, starmap


from PIL import Image
from tqdm import tqdm

def convert_image(fname, out_path):
    img = Image.open(fname).convert("RGB")


    width, height = img.size
    if width > height:
        crop_size = (width - height) // 2
        img = img.crop((crop_size, 0, width - crop_size, height))
        img = img.crop((0, 0, height, height))
    elif height > width:
        crop_size = (height - width) // 2
        img = img.crop((0, crop_size, width, height - crop_size))
        img = img.crop((0, 0, width, width))

    img = img.resize((300, 300), Image.ANTIALIAS)
    img.save(os.path.join(out_path, fname.split("/")[-1].replace("png", "jpg")))


def main():
    in_path = "../assets/images/team"
    out_path = "../assets/images/team_resized"

    if not os.path.exists(out_path):
        os.mkdir(out_path)

    # get all jpg from /assets/images/team
    img_fnames = list(map(
        lambda fname: os.path.join(in_path, fname),
        filter(
            lambda fname: fname[-3:] in ["jpg", "png"],
            os.listdir(in_path)
        )
    ))

    list(starmap(
        convert_image,
        tqdm(zip(img_fnames, repeat(out_path)), total=len(img_fnames))
    ))




if __name__=="__main__":
    main()