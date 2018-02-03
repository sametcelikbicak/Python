from PIL import Image, ImageFilter


image = Image.open("PillowTestImageOriginal.jpg")

image.show()

#image.save("PillowSave.jpg")

#image.rotate(180).save("Pillow180Rotate.jpg")

#image.convert(mode = "L").save("PillowBlackWhite.jpg")

#degistir = (490,190)
#image.thumbnail(degistir)
#image.save("PillowThumbnail.jpg")

#image.filter(ImageFilter.GaussianBlur(5)).save("PillowBlur.jpg")

#kirpilacak_alan = (340,0,680,100)
#image.crop(kirpilacak_alan).save("PillowCrop.jpg")