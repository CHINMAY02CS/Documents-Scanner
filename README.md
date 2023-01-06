# Document-Scanner

This is a smart document scanner made using Python.
<br>
<br>This scanner takes the image input of document using smartphone and scans and saves the document in PC.

## Working 
* The code is run and the camera display appears on the laptop screen.
* Tap 's' on keyboard to scan the document.
* To find the scanned image, go the the project folder where all the scanned documents will be stored.


![Alt](https://github.com/CHINMAY02CS/Documents-Scanner/blob/main/Framesample.jpg)


![Alt](https://github.com/CHINMAY02CS/Documents-Scanner/blob/main/Objectonlysample.jpg)


## STEPS TO RUN THIS PROJECT

1. Download the main.py file and place it in the project folder of desired name.
2. Install the required packages.
* OpenCV (opencv-contrib-python if using Pycharm tool)
* Numpy
* Pillow
3. Download and install 'IP Webcam' app in your smartphone.
[Link to download](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_IN&gl=US)
4. Launch the app and go to 'Start Server'
5. Copy the IP address given there in IPv4.
6. Open this IPv4 address in your web browser and press 'Javascript' in 'Video Render' option menu.
![Alt](https://github.com/CHINMAY02CS/Documents-Scanner/blob/main/ipwebcam.jpg)
7. Right click on the video screen appearing and tap 'open in new tab'. Everytime reloading the page will show latest captured image.
8. Place the copied IPv4 address in your main.py file in variable - 'url'.
9. Run the code.
10. After aligning the image press 's' on keyboard and the document will be saved in the project folder in pdf format.


### Notes
<br>
* For scanning smaller documents like driving license, passport size photo - change the 'frame' to 'object_only' in lines 42 and 45 in main.py file.
* I have used PyCharm Community Edition developer tool for this project.
* For scanning grayscale documents, change the flag value from -1 to 0 in line 21 in main.py file.
* Comment out line 36 in main.py file if you do not want a rectangluar frame appearance in the scanned small size document.

