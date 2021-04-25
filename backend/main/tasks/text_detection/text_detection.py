# USAGE
# python text_detection.py --image images/lebron_james.jpg --east frozen_east_text_detection.pb

# import the necessary packages
from imutils.object_detection import non_max_suppression
import numpy as np
import argparse
import time
import cv2

class detect_img:
	def __init__(self, img):
		self.args = vars()
		self.img = img
		self.net = None
		self.image = None
		self.orig = None
		self.layerNames = None
		self.H, self.W = None, None
		self.scores, self.geometry = None, None

	def set_args(self):
		# construct the argument parser and parse the arguments
		ap = argparse.ArgumentParser()
		ap.add_argument("-east", "--east", type=str, default="frozen_east_text_detection.pb",
			help="path to input EAST text detector")
		ap.add_argument("-c", "--min-confidence", type=float, default=0.5,
			help="minimum probability required to inspect a region")
		ap.add_argument("-w", "--width", type=int, default=320,
			help="resized image width (should be multiple of 32)")
		ap.add_argument("-e", "--height", type=int, default=320,
			help="resized image height (should be multiple of 32)")
		self.args = vars(ap.parse_args())

	def load_img(self):
		# load the input image and grab the image dimensions
		self.image = cv2.imread(self.img)
		self.orig = self.image.copy()
		(self.H, self.W) = self.image.shape[:2]

		# set the new width and height and then determine the ratio in change
		# for both the width and height
		(newW, newH) = (self.args["width"], self.args["height"])
		self.rW = self.W / float(newW)
		self.rH = self.H / float(newH)

		# resize the image and grab the new image dimensions
		self.image = cv2.resize(self.image, (newW, newH))
		(self.H, self.W) = self.image.shape[:2]

	def load_model(self):
		# define the two output layer names for the EAST detector model that
		# we are interested -- the first is the output probabilities and the
		# second can be used to derive the bounding box coordinates of text
		self.layerNames = [
			"feature_fusion/Conv_7/Sigmoid",
			"feature_fusion/concat_3"]

		# load the pre-trained EAST text detector
		print("[INFO] loading EAST text detector...")
		self.net = cv2.dnn.readNet(self.args["east"])

	def predict(self):
		# construct a blob from the image and then perform a forward pass of
		# the model to obtain the two output layer sets
		blob = cv2.dnn.blobFromImage(self.image, 1.0, (self.W, self.H),
			(123.68, 116.78, 103.94), swapRB=True, crop=False)
		start = time.time()
		self.net.setInput(blob)
		(self.scores, self.geometry) = self.net.forward(self.layerNames)
		end = time.time()

		# show timing information on text prediction
		print("[INFO] text detection took {:.6f} seconds".format(end - start))

	def draw_board(self):
		# grab the number of rows and columns from the scores volume, then
		# initialize our set of bounding box rectangles and corresponding
		# confidence scores
		(numRows, numCols) = self.scores.shape[2:4]
		rects = []
		confidences = []

		# loop over the number of rows
		for y in range(0, numRows):
			# extract the scores (probabilities), followed by the geometrical
			# data used to derive potential bounding box coordinates that
			# surround text
			scoresData = self.scores[0, 0, y]
			xData0 = self.geometry[0, 0, y]
			xData1 = self.geometry[0, 1, y]
			xData2 = self.geometry[0, 2, y]
			xData3 = self.geometry[0, 3, y]
			anglesData = self.geometry[0, 4, y]

			# loop over the number of columns
			for x in range(0, numCols):
				# if our score does not have sufficient probability, ignore it
				if scoresData[x] < self.args["min_confidence"]:
					continue

				# compute the offset factor as our resulting feature maps will
				# be 4x smaller than the input image
				(offsetX, offsetY) = (x * 4.0, y * 4.0)

				# extract the rotation angle for the prediction and then
				# compute the sin and cosine
				angle = anglesData[x]
				cos = np.cos(angle)
				sin = np.sin(angle)

				# use the geometry volume to derive the width and height of
				# the bounding box
				h = xData0[x] + xData2[x]
				w = xData1[x] + xData3[x]

				# compute both the starting and ending (x, y)-coordinates for
				# the text prediction bounding box
				endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
				endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
				startX = int(endX - w)
				startY = int(endY - h)

				# add the bounding box coordinates and probability score to
				# our respective lists
				rects.append((startX, startY, endX, endY))
				confidences.append(scoresData[x])

		# apply non-maxima suppression to suppress weak, overlapping bounding
		# boxes
		boxes = non_max_suppression(np.array(rects), probs=confidences)

		# loop over the bounding boxes
		for (startX, startY, endX, endY) in boxes:
			# scale the bounding box coordinates based on the respective
			# ratios
			startX = int(startX * self.rW)
			startY = int(startY * self.rH)
			endX = int(endX * self.rW)
			endY = int(endY * self.rH)

			# draw the bounding box on the image
			self.orig = cv2.rectangle(self.orig, (startX, startY), (endX, endY), (0, 255, 0), 2)

	def predict_and_draw(self):
		self.set_args()
		self.load_img()
		self.load_model()
		self.predict()
		self.draw_board()

		return self.orig

# show the output image
# cv2.imshow("Text Detection", orig)
# cv2.waitKey(0)
# cv2.imwrite("test.jpg", orig)

if __name__ == '__main__':
	img_path = "images/lebron_james.jpg"
	a = detect_img(img_path)
	img = a.predict_and_draw()
	cv2.imwrite("test2.jpg", img)
