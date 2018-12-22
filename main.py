import imread as imread
from PIL import Image
from collections import Counter
import os
files = []
for file in os.listdir('./input_image'):
    files.append(file)

img_data = []
for file_name in files:
    file = './input_image/'+file_name
    img_data.append(imread.open_image(file))

im = Image.open(file)
output = Image.new( im.mode, im.size)
output_data = output.load()

print("Processing......................")
i,j = img_data[0].size
for x in range(i):
    for y in range(j):
        fixel_val = [],[],[],[]
        for l in range(len(files)):
            pixel = img_data[l].getpixel((x,y))
            for k in range(len(pixel)):
                fixel_val[k].append(pixel[k])
        r = fixel_val[0]
        g = fixel_val[1]
        b = fixel_val[2]
        R = Counter(r)
        G = Counter(g)
        B = Counter(b)
        output_data[x,y] = (R.most_common(1)[0][0],G.most_common(1)[0][0],B.most_common(1)[0][0])
                

output.show()
output.save('./input_image/output.jpg')
print("process complete..!")

