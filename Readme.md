<code>
  <h1 align="center">TumorInsight</h1>
</code>

# Overview

<img src="https://github.com/shaurya-src/TumorInsight/blob/main/Assets/Snap.png" align="left"> <br>

## What is `TumorInsight`?

`TumorInsight` provides a powerful model for easy detection and classification of Brain Tumors right at your fingertips.
Our main aim is to provide faster diagnostic results so that treatment can be given faster to those who require.
With this application, people can easily scan the MRI images to detect a tumor, without any medical assist, thus making the process faster and more feasible.

- Check the deployed heroku app from [here](https://tumorinsight-app.herokuapp.com/)

# Features

![RepoSize](https://img.shields.io/github/repo-size/shaurya-src/TumorInsight?logo=GitHub&style=flat-square)
![License](https://img.shields.io/github/license/shaurya-src/TumorInsight?logo=GitLab&style=flat-square)
![LastCommit](https://img.shields.io/github/last-commit/shaurya-src/TumorInsight?logo=Git&style=flat-square)

<img src="https://media.giphy.com/media/xT0Gqn9yuw8hnPGn5K/giphy.gif" align="right" width="300" height="300">

- [x] Easy to use
- [x] Minimal web application
- [x] Accurate Results
- [x] Supports all image formats

# Contents

- [Project Details](#project-info)
- [Requirements](#requirements)
- [Installation](#installation)
- [Contribute](#contri)
- [Tech Stacks](#tech)
- [License](#license)
- [Author](#author)

# <a name="project-info"> Project Details

  [![Made with Python](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/shaurya-src/TumorInsight) [![Made with love](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/shaurya-src)

The project uses RESNET50 model for classification of different Brain Tumors into 3 Types. On top of that, we implemented an enhanced K-Means algorithm for segmentation of Brain Tumor from the input image and show the detected position of the Tumor. The algorithm automatically clusters different segments of the MRI image and then applies Thresholding with appropriate intensity to highlight only the tumor segment. For training the model we have used BraTS dataset.

- Download trained model from [here](https://drive.google.com/file/d/1-rIrzzqpsSg80QG175hjEPv9ilnSHmqK/view?usp=sharing)

## <a name="requirements"> Requirements

To install all requirements run: `pip install -r requirements.txt`

- numpy~=1.20.1
- pillow~=8.2.0
- torchvision~=0.8.2
- opencv-python~=4.5.2.52
- matplotlib~=3.3.4
- pandas~=1.2.4
- seaborn~=0.11.1
- scikit-learn~=0.24.1
- flask~=1.1.2
- werkzeug~=1.0.1
- scikit-image~=0.18.1
- h5py~=3.2.1
- requests~=2.25.1
- torch~=1.7.1
- selenium~=3.141.0
- flask_sqlalchemy~=2.5.1
- imutils~=0.5.4

## <a name="installation"> Installation

Follow these steps to use *this project*.

1. Clone the repository.
2. Install all the requirements.
3. Download the trained model from given link.
4. Save the model in CNN/models.
5. Run WebApp/app.py to start the backend server.
6. Run WebApp/deploy.py to run the Web Application.

## <a name="contri"> Contribute

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## <a name="tech"> Tech Stacks/Tools Used

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.x-success?style=flat-square&logo=Python&logoColor=white">
  <img src="https://img.shields.io/badge/Editor-VS_Code-success?style=flat-square&logo=Visual-Studio-Code&logoColor=white&color=blue">
  <img src="https://img.shields.io/badge/Windows-10-success?style=flat-square&logo=Windows&logoColor=white">

  <img src="https://img.shields.io/badge/Library-PyTorch-success?style=flat-square&logo=PyTorch&logoColor=white">

  [![Generic badge](https://img.shields.io/badge/Web-Application-teal.svg?style=for-the-badge)](https://github.com/shaurya-src) [![Generic badge](https://img.shields.io/badge/Framework-Flask-orange.svg?style=for-the-badge&logo=flask&logoColor=white)](https://github.com/shaurya-src)
  
</p>

## <a name="license"> License

*TumorInsight* is available under the MIT license. See the [LICENSE](https://github.com/shaurya-src/TumorInsight/blob/main/LICENSE) file for more info.

## <a name="author"> Author
<!---
```python
# Shaurya Choudhary
```
-->

<p align="center">
  <code> Shaurya Choudhary </code>
</p>
<!---
- [Gmail](mailto:shaurya.src@gmail.com)
- [GitHub](https://github.com/shoheiyokoyama)
- [LinkedIn](https://www.linkedin.com/in/shaurya-src/)
- [Instagram](https://www.instagram.com/shaurya_src/)
- [Twitter](https://twitter.com/shaurya_src)
-->

<br>

<p align="center">
  <a href="mailto:shaurya.src@gmail.com">
    <img src="https://github.com/shaurya-src/shaurya-src/blob/main/Assets/Logos/email.svg" width="30" height="30" hspace="20">
  </a>

  <a href="https://github.com/shaurya-src">
    <img src="https://github.com/shaurya-src/shaurya-src/blob/main/Assets/Logos/github.svg" width="30" height="30" hspace="20">
  </a>

  <a href="https://www.linkedin.com/in/shaurya-src/">
    <img src="https://github.com/shaurya-src/shaurya-src/blob/main/Assets/Logos/linkedin.svg" width="30" height="30" hspace="20">
  </a>

  <a href="https://www.instagram.com/shaurya_src/">
    <img src="https://github.com/shaurya-src/shaurya-src/blob/main/Assets/Logos/instagram.svg" width="30" height="30" hspace="20">
  </a>

  <a href="https://twitter.com/shaurya_src">
    <img src="https://github.com/shaurya-src/shaurya-src/blob/main/Assets/Logos/twitter.svg" width="30" height="30" hspace="20">
  </a>
</p>

<!--- BADGES -->

<!--- Dynamic Badges 

- Repo Size: https://img.shields.io/github/repo-size/shaurya-src/Web-Automation?logo=GitHub&style=flat-square

- Last Commit: https://img.shields.io/github/last-commit/shaurya-src/Web-Automation?logo=Git&style=flat-square

- License: https://img.shields.io/github/license/shaurya-src/Web-Automation?logo=GitLab&style=flat-square

-->

<!--- Tech Stacks

- Python3.x: https://img.shields.io/badge/Python-3.x-success?style=flat-square&logo=Python&logoColor=white 

- Jupyter Notebook: https://img.shields.io/badge/Notebook-Jupyter-success?style=flat-square&logo=Jupyter&logoColor=white 

- HTML: https://img.shields.io/badge/Language-HTML-success?style=flat-square&logo=HTML5&logoColor=white&color=purple

- CSS: https://img.shields.io/badge/Language-CSS-success?style=flat-square&logo=CSS3&logoColor=white&color=purple

- JavaScript: https://img.shields.io/badge/Language-JavaScript-success?style=flat-square&logo=JavaScript&logoColor=white&color=purple

-->

<!--- Python Libraries

- Pandas: https://img.shields.io/badge/Library-Pandas-success?style=flat-square&logo=Pandas&logoColor=white

- NumPy: https://img.shields.io/badge/Library-NumPy-success?style=flat-square&logo=NumPy&logoColor=white

- TensorFlow: https://img.shields.io/badge/Library-TensorFlow-success?style=flat-square&logo=TensorFlow&logoColor=white

- Keras: https://img.shields.io/badge/Library-Keras-success?style=flat-square&logo=Keras&logoColor=white

- Django: https://img.shields.io/badge/Library-Django-success?style=flat-square&logo=DJango&logoColor=white&color=orange

- Selenium: https://img.shields.io/badge/Library-Selemium-success?style=flat-square&logo=Sellfy&logoColor=white

- Matplotlib: https://img.shields.io/badge/Library-Matplotlib-success?style=flat-square&logo=GraphQL&logoColor=white&color=purple

-->

<!--- System

- Windows 10: https://img.shields.io/badge/Windows-10-success?style=flat-square&logo=Windows&logoColor=white

- Ubuntu: https://img.shields.io/badge/Linux-Ubuntu-success?style=flat-square&logo=Ubuntu&logoColor=white

- Kali: https://img.shields.io/badge/Linux-Kali-success?style=flat-square&logo=Arch-Linux&logoColor=white

- PyCharm: https://img.shields.io/badge/Editor-PyCharm-success?style=flat-square&logo=PyCharm&logoColor=white&color=blue

- VSC: https://img.shields.io/badge/Editor-VS_Code-success?style=flat-square&logo=Visual-Studio-Code&logoColor=white&color=blue

-->
