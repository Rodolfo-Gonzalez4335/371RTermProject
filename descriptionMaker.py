import cv2
import numpy as np
import os
import urllib.request

def storeNegativeImageOnline():

	negativeImageLink = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808"
	negativeImageUrl = urllib.request.urlopen(negativeImageLink).read().decode()

	picNum= len(os.listdir('negative/'))+1;
	for i in negativeImageUrl.split('\n'):
		try:
			urllib.request.urlretrieve(i,"negative/"+str(picNum)+".jpg");
			img = cv2.imread('negative/'+str(picNum)+'.jpg',cv2.IMREAD_GRAYSCALE)
			resizeImage = cv2.resize(img,(100,100));
			cv2.imwrite('negative/'+str(picNum)+'.jpg',resizeImage);
			picNum+=1;
		except Exception as e:
			print(str(e));

def storePositiveImageOnline():

	ImageLink = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07753592"
	ImageUrl = urllib.request.urlopen(ImageLink).read().decode()

	picNum= len(os.listdir('positive/'))+1;
	for i in ImageUrl.split('\n'):
		try:
			urllib.request.urlretrieve(i,"positive/"+str(picNum)+".jpg");
			img = cv2.imread('positive/'+str(picNum)+'.jpg',cv2.IMREAD_GRAYSCALE)
			resizeImage = cv2.resize(img,(100,100));
			cv2.imwrite('positive/'+str(picNum)+'.jpg',resizeImage);
			picNum+=1;
		except Exception as e:
			print(str(e));

def changeToGrayScaleAndResize(width,height):
	for i in os.listdir("./Test4"):
		try:
			if(str(i)!=".DS_Store"):
				imagepath = os.path.join("./Test4",i)
				if os.path.exists(imagepath):
					img = cv2.imread(imagepath,cv2.IMREAD_GRAYSCALE);
					# resizeImg = cv2.resize(img,(width,height))
					cv2.imwrite(imagepath,img);
				else:
					print(imagepath + " not found")
		except Exception as e:
			print(e);

def remove_not_found_images():
	for fileType in ['negative', 'positive']:
		for img in os.listdir(fileType):
			for notFound in os.listdir('notfound/'):
				try:
					currentImagePath = str(fileType)+'/'+str(img);
					notFoundImage = cv2.imread('notfound/'+str(notFound));
					importedImage = cv2.imread(currentImagePath);
					if notFoundImage.shape == importedImage.shape and not(np.bitwise_xor(notFoundImage,importedImage).any()):
						print('removing an image');
						os.remove(currentImagePath)
				except Exception as e:
					print(str(e));

def add_negative_and_positive_descriptors():
	#	bg.txt contains all the bad files that are not the object to clasify
	#	'positive' 'negative'
	for directoryName in ['negative']:
		for img in os.listdir(directoryName):
			if directoryName=='negative':
				line = directoryName + '/'+img+'\n';
				with open("bg.txt",'a') as f:
					f.write(line)

			elif directoryName == 'positive':
				line = directoryName + '/' + img + ' 1 0 0 ' + str(img.shape[0])+ str(img.shape[1] + ' \n');
				with open("info.dat","a") as f:
					f.write(line)

#Buggy
def resizeImage(width,height):
	#'negative',d
	# for directoryName in ['positive']:
		for i in os.listdir('./positive'):
			try:
				if (str(i)!=".DS_Store"):
					imagepath = os.path.join("positive/",i)
					if os.path.exists(imagepath):

						img = cv2.imread(imagepath)
						# print(str(i));
						resizeImage = cv2.resize(img,(width,height));
						cv2.imwrite(imagepath,resizeImage);
					else:
						print("path not found")
						print(imagepath);
				else:
					print("DS STORE found");
			except Exception as e:
				print(str(e));

#makepositivieitive_and_negatives();
#remove_not_found_images();
# resizeImage(200,200);
# changeToGrayScaleAndResize(200,200)
add_negative_and_positive_descriptors();
# store_negative_image_online();
# store_positivieitive_image_online();
