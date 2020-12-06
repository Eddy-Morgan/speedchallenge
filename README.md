Welcome to the comma.ai Programming Challenge!
======

Your goal is to predict the speed of a car from a video.

- data/train.mp4 is a video of driving containing 20400 frames. Video is shot at 20 fps.
- data/train.txt contains the speed of the car at each frame, one speed on each line.
- data/test.mp4 is a different driving video containing 10798 frames. Video is shot at 20 fps.

Evaluation
-----

evaluate your test.txt using mean squared error. <10 is good. <5 is better. <3 is heart.


Attempt 1
-----

Optical Flow
Optical flow is the pattern of apparent motion of image objects between two consecutive frames caused by the movemement of object or camera. It is 2D vector field where each vector is a displacement vector showing the movement of points from first frame to second. Consider the image below (Image Courtesy: Wikipedia article on Optical Flow).


Lucas-Kanade Optical Flow Method is adopted in this attempt
-----

Lucas-Kanade Optical Flow in OpenCV
OpenCV provides all these in a single function, cv2.calcOpticalFlowPyrLK(). Here, we create a simple application which tracks some points in a video. To decide the points, we use cv2.goodFeaturesToTrack(). We take the first frame, detect some Shi-Tomasi corner points in it, then we iteratively track those points using Lucas-Kanade optical flow. For the function cv2.calcOpticalFlowPyrLK() we pass the previous frame, previous points and next frame. It returns next points along with some status numbers which has a value of 1 if next point is found, else zero. We iteratively pass these next points as previous points in next step. See the code below:
