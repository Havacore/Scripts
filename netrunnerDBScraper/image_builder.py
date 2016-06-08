from PIL import Image


def generate_deck_image():

    im = Image.open("andy.png")

    new_im = Image.new('RGB', map(lambda x: x*3, im.size))

    for i in xrange(0, im.size[0]*3, im.size[0]):
        for j in xrange(0, im.size[1]*3, im.size[1]):
            new_im.paste(im, (i, j))

    new_im.save("andy3.png")