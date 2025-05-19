# Robotic-Gambit
<p align="center">
    <img src="https://i.imgur.com/waxVImv.png">
</p>

#### [Abdulqadir Alssaggaff](https://www.linkedin.com/in/abdulqadir-alssaggaff-049899285/), [Wadie Shibli](https://www.linkedin.com/in/wadie-shibli/), [Ammar Alharbi](), and [Ahmed Alssaggaff](https://www.linkedin.com/in/ahmed-hussien-alsaggaf/) Supervisor [Dr.Raed Abdulbasit Alsini](https://www.kau.edu.sa/CVEn.aspx?Site_ID=0014414&Lng=EN)

![chess version](https://img.shields.io/badge/chess-1.10.0-blue)
![TensorFlow version](https://img.shields.io/badge/TensorFlow-2.9.1-orange)
![OpenCV version](https://img.shields.io/badge/OpenCV-4.8.1.78-green)
![Flask version](https://img.shields.io/badge/Flask-3.0.2-white)
![Flutter SDK](https://img.shields.io/badge/Flutter%20SDK-3.1.2%20%3C%204.0.0-blue?logo=flutter)

<p align="center">
    <img src="https://i.imgur.com/s9Hj2Wl.png" width="350" height="350">
</p>

## 📢 Latest Updates
- 📦 model and datasets coming soon! 🚀
---

## 	♟️ Overview
**Robotic Gambit** combines robotics, computer vision, and machine learning to revolutionize chess play. The project features a robotic arm programmed to interact with a physical chessboard, using advanced computer vision to detect and respond to changes in real-time. At its core, an AI leverages deep learning to improve its chess strategies and gameplay.

---

## ⚡ Model and Dataset

the convolutional neural network contain many layers and end with fully connected layer
which is the normal neural network, it start with input layer normally it take 2D diminutions
input in our case we take the input as 3D diminutions.

<p align="center">
    <img src="https://i.imgur.com/nX86gCH.png" width="550">
</p>

then it go to the convolutional layer and moving the filter to the right then multiply and sum the values based on the padding space, then using max pooling to get the biggest value only then finally in the final layer using flatten operation to make it a victor and being ready to used with fully connected layer.

<p align="center">
    <img src="https://i.imgur.com/1xVNh0E.png" width="550">
</p>


### CNN layers of this project :

| Layer (type)          | Input Shape     | Output Shape    |
|-----------------------|-----------------|-----------------|
| InputLayer            | [None, 14, 8, 8] | [None, 14, 8, 8] |
| Conv2D (Convolutional)| [None, 14, 8, 8] | [None, 12, 6, 32]|
| Conv2D (Convolutional)| [None, 12, 6, 32]| [None, 10, 4, 64]|
| Conv2D (Convolutional)| [None, 10, 4, 64]| [None, 9, 3, 64] |
| Flatten               | [None, 9, 3, 64] | [None, 1728]     |
| Dense (Fully connected)| [None, 1728]   | [None, 64]       |
| Dense (Fully connected)| [None, 64]     | [None, 1]        |


### The model and dataset

| File            | Link                                 |
|-----------------------------------------------------|----------------------------------------------------------------------|
| CNN   | [![Run in Colab](https://img.shields.io/badge/Google%20Colab-Run%20in%20Colab-orange?logo=googlecolab)](https://colab.research.google.com/drive/?) |
| Saved Model | [![Google Drive](https://img.shields.io/badge/Google%20Drive-Download%20Model-blue?logo=googledrive)](https://drive.google.com/file/d/modelgambitnameforlater/?) |
| Data Set | [![Google Drive](https://img.shields.io/badge/Google%20Drive-Access%20Dataset-blue?logo=googledrive)](https://drive.google.com/drive/folders/?) |


---

## 	👁️ Computer Vision
In the project, we take two different frames the grayscale of first frame and final frame, then get the difference using absdiff to find the move with multiple filters ( Threshold, Dilated, Eroded), then locate all changed frames with filters above using Contours.

<p align="center">
  <img src="https://i.imgur.com/djNN7CR.png" alt="Simulation" width="550"> 
</p>

Finally, with located square board, the pointPolygonTest will return true if any change is located in the squares, otherwise return false.

<p align="center">
  <img src="https://i.imgur.com/lSdeyFY.png" alt="Simulation" width="550"> 
</p>

---

## 🕹️ Simulation

In the above scenario, the camera records the state of the chess game and uses it as input. After that, this data is sent to an Arduino device. The primary laptop that contains the core processing routines receives the information from the Arduino, which serves as an intermediary. With the required algorithms installed, the laptop calculates the best course of action for the robotic arm. The laptop notifies the Arduino of the chosen motion after the calculation is finished.


<p align="center">
  <img src="https://i.imgur.com/qZDbA6Q.gif" alt="Simulation" width="550"> 
</p>

The Arduino thereafter acts as a bridge to send the output to the robotic arm. Lastly, using the data it has analyzed, the robotic arm carries out the command. This complex system combines computational decision-making, physical robotic movement, and real-time image processing to enable an automated and interactive chess playing experience.

---
