import numpy as np
import imageio
import sys
import matplotlib.pyplot as plt
from PIL import Image

pixSize = int(sys.argv[1])

#print(new)
def splitup(img):
	new = []
	for i in range(int(img.shape[0]/pixSize)):
		new.append([])
		for j in range(int(img.shape[1]/pixSize)):	
			new[-1].append([])
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			blocki = int(i/pixSize)-1
			blockj = int(j/pixSize)-1
			new[blocki][blockj].append(img[i,j])
	return np.array(new)

def averageout(img):
	img1 = np.array(img)
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			img[i][j]=np.mean(img1[i][j],axis=0)
	return img

#new = np.ones(new1.shape)
def blowup(img,new_size):
	blowup = np.zeros((new_size))
	for i in range(blowup.shape[0]):
		for j in range(blowup.shape[1]):
			blocki = int(i/pixSize)
			blockj = int(j/pixSize)
			blowup[i][j] = img[blocki-1][blockj-1]
	return blowup

def deletePixel(coord):
	pass

def main():
	img = Image.open('nc.jpeg')
	img = np.array(img)
	img = blowup(averageout(splitup(img)),img.shape)
	img = np.array(img,dtype=np.uint8)
	fig = plt.figure()
	plt.imshow(img)
	'''
	def onclick(event):
		global click 
		i ,j = event.xdata, event.ydata
		click = (i,j)
		fig.canvas.mpl_disconnect(clicker)
		plt.close()
	while True:
		clicker = fig.canvas.mpl_connect('button_press_event',onclick)
		plt.show()
		print(click)
		deletePixel(click)
	'''
	i = Image.fromarray(img,mode="RGB")
	i.show()
	i.save("ncc.png")

main()

