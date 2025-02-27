import imageio as iio
filenames=['gif using python\dog bottom.png','gif using python\dog top.png']
images=[]
for i in filenames:
    images.append(iio.imread(i))
iio.mimsave('dog.gif',images,duration=500,loop=0)
