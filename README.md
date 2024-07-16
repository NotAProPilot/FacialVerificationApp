Tired of manually verifying faces aganist ID manually? Here, as a part of the Image Processing and Recognition class, we improvise an advanced facial recognition that could be deployed quickly on any machine with a Python enviroment.
# Features
This script can automatically verifying in real-time a face and comparing against an uploaded photo ID (passport, driver license, student ID, etc). 
# How the script works
The script works in 3 stages:
1. Automatically detecting facial features from photo ID using OpenCV built-in classifier
2. Automatically capturing and extracting real-time facial data
3. Comparing extracted facial features from photo ID and real-time data using [[DeepFace]](https://github.com/serengil/deepface)
![image](https://github.com/NotAProPilot/IPR-Final-Projects-Facial-Verification-App/assets/113848893/eedb3539-5467-4130-9426-480aa99cba99)
# Installation guide
1. Clone the repo or download the repo as zip file. (***IMPORTANT:*** Running only the Main.py or GUI.py will result in error, see Program Structure for more information)
2. Install the following librabies:
- [[DeepFace]](https://github.com/serengil/deepface)
- [[OpenCV]](https://opencv.org/releases/)
- [[Pillow]](https://pypi.org/project/pillow/)
# Usage guide
1. Run the program from `GUI.py`.
2. A pop-up will appear as follows: ![image](https://github.com/user-attachments/assets/3407d3c1-0328-461b-ba01-83991ddfb378)
3. Click on the "Upload Photo" button to upload a photo ID. ![image](https://github.com/user-attachments/assets/fa13db5e-91de-4992-9118-063069477f0d)

4. Click on the "Capture Photo from Webcam" to continue.
5. The webcam will open. Look straight at the webcam. When ready, press Enter to continue.
6. Press "Verify" to complete the process. 

   
