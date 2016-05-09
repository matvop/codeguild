from PIL import Image

img = Image.open('C:\\Users\\Matt\\codeguild\\javascript\\mole.png')
roated_image = img.rotate(45).save('rotated.png')
