#!/usr/bin/python

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as nup

def main():
	img=mpimg.imread("FacSalud.png")
	imgplot = plt.imshow(img,zorder=0, extent=[0, 100, 0, 100])
	plt.show()

if __name__ == '__main__':
	main()
