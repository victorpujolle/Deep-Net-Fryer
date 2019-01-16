from PIL import Image, ImageFilter, ImageEnhance

def main():

    original_img = "input/weaboo.png"

    # Open the tmp file as an Image
    img_original = Image.open(original_img)
    img = img_original

    x,y = img.size
    # Various image processes

    #Sharpen image
    sharp = ImageEnhance.Sharpness(img)
    img = sharp.enhance(10)

    #contrast image
    contr = ImageEnhance.Contrast(img)
    img = contr.enhance(4)

    #noise
    #img = img.filter(ImageFilter.GaussianBlur(5))

    img = img.resize((x/2,y/2),Image.ANTIALIAS)
    #Save/show image
    img.show()

#Lauching the main
if __name__ == "__main__":
    main()
