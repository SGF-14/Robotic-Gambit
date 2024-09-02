# Robotic-Gambit
<p align="center">
    <img src="https://i.imgur.com/waxVImv.png">
</p>

#### [Abdulqadir Alssaggaff](https://www.linkedin.com/in/abdulqadir-alssaggaff-049899285/), [Wadie Shibli](https://www.linkedin.com/in/wadie-shibli/), [Ammar Alharbi](), and [Ahmed Alssaggaff](https://www.linkedin.com/in/ahmed-hussien-alsaggaf/) Supervisor [Dr.Raed Abdulbasit Alsini](https://www.kau.edu.sa/CVEn.aspx?Site_ID=0014414&Lng=EN)
#### King Abdulziz University (KAU), KSA
![chess version](https://img.shields.io/badge/chess-1.10.0-blue)
![TensorFlow version](https://img.shields.io/badge/TensorFlow-2.9.1-orange)
![Flask version](https://img.shields.io/badge/Flask-3.0.2-blue)
![OpenCV version](https://img.shields.io/badge/OpenCV-4.8.1.78-green)

<p align="center">
    <img src="https://i.imgur.com/s9Hj2Wl.png" width="350" height="350">
</p>



## 📢 Latest Updates
- 📦 Code and datasets coming soon! 🚀
---

## 	♟️ Overview
Robotic Gambit will involve programming the robotic arm's movements and interactions with the chessboard, using computer vision and Machine learning techniques to enable the AI to learn chess games and make informed decisions. The AI's performance will be enhanced through continuous learning and optimization

---

## ⚡ Model and Dataset

the convolutional neural network contain many layers and end with fully connected layer
which is the normal neural network, it start with input layer normally it take 2D diminutions
input in our case we take the input as 3D diminutions, then it go to the convolutional layer
and moving the filter to the right then multiply and sum the values based on the padding
space, then using max pooling to get the biggest value only then finally in the final layer using
flatten operation to make it a victor and being ready to used with fully connected layer

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

| Model            | Google Colab Link                                 |
|-----------------------------------------------------|----------------------------------------------------------------------|
| CNN   | [![Run in Colab](https://img.shields.io/badge/Google%20Colab-Run%20in%20Colab-orange?logo=googlecolab)](https://colab.research.google.com/drive/?) |
| Saved Model | [![Google Drive](https://img.shields.io/badge/Google%20Drive-Download%20Model-blue?logo=googledrive)](https://drive.google.com/file/d/your_model_id/?) |
| Data Set | [![Google Drive](https://img.shields.io/badge/Google%20Drive-Access%20Dataset-blue?logo=googledrive)](https://drive.google.com/drive/folders/?) |


---


