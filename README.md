[//]: # (Image References)

[image1]: ./images/key_pts_example.png "Facial Keypoint Detection"

# Facial Keypoint Detection
[![Udacity Computer Vision Nanodegree](http://tugan0329.bitbucket.io/imgs/github/cvnd.svg)](https://www.udacity.com/course/computer-vision-nanodegree--nd891)

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Content](#content)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

About the Project
---

In this project, computer vision techniques and deep learning architectures are combined to build a 
facial keypoint detection system. Facial keypoints include points around the eyes, nose, and mouth on a face and are 
used in many applications. These applications include: facial tracking, facial pose recognition, facial filters, and
 emotion recognition. A proper trained model is able to process any image, detect faces, and predict the locations 
 of facial keypoints on each face; examples of these keypoints are displayed below.

![Facial Keypoint Detection][image1]

<!-- GETTING STARTED -->
## Getting Started

The software is written in Python 3.7 and tested on Windows 10. The usage of the Miniconda Python distribution is strongly recommended.

### Prerequisites

* Miniconda (https://docs.conda.io/en/latest/miniconda.html)

### Installation

1. Clone this repo
```sh
git clone https://github.com/sebkaster/Facial_Keypoints.git
```

2. Create Anaconda environment
```sh
conda create -n facial_env anaconda python=3
```

3. Activate environment
```sh
conda activate facial_env
```

4. Install pip package manager
```sh
conda install pip
```

5. Install required python modules
```
python -m pip install -r requirements.txt
```

<!-- CONTENT -->
## Content

__Notebook 1__ : Loading and Visualizing the Facial Keypoint Data

__Notebook 2__ : Defining and Training a Convolutional Neural Network (CNN) to Predict Facial Keypoints

__Notebook 3__ : Facial Keypoint Detection Using Haar Cascades and your Trained CNN

__Notebook 4__ : Fun Filters and Keypoint Uses

<!-- USAGE EXAMPLES -->
## Usage

In order to use this project start jupyter by typing `jupyter notebook` in your Anaconda environment. 

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License.

<!-- CONTACT -->
## Contact

Sebastian Kaster - sebastiankaster@googlemail.com

Project Link: [https://github.com/sebkaster/Facial_Keypoints](https://github.com/sebkaster/Facial_Keypoints)
