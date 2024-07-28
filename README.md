# deepface
Face recognition application using DeepFace

## DeepFace

- **Face Verification**: The task of face verification refers to comparing a face with another to verify if it is a match or not. Hence, face verification is commonly used to compare a candidate’s face to another. This can be used to confirm that a physical face matches the one in an ID document.
- **Face Recognition**: The task refers to finding a face in an image database. Performing face recognition requires running face verification many times.
- **Facial Attribute Analysis**: The task of facial attribute analysis refers to describing the visual properties of face images. Accordingly, facial attributes analysis is used to extract attributes such as age, gender classification, emotion analysis, or race/ethnicity prediction.
- **Real-Time Face Analysis**: This feature includes testing face recognition and facial attribute analysis with the real-time video feed of your webcam.

Install the DeepFace package

```shell
#Repo: https://github.com/serengil/deepface
pip install deepface
```

Import the library

```python
from deepface import DeepFace
```

Run Face Verification with Deep Learning on DeepFace

```python
verification = DeepFace.verify(img1_path = "img1.jpg", img2_path = "img2.jpg")
```

## Photos
Photo by Fresh Tr: https://www.pexels.com/photo/little-asian-girl-posing-in-park-19078969/

Photo by Fresh Tr: https://www.pexels.com/photo/portrait-of-a-girl-in-a-white-blouse-19078970/

Photo by Fresh Tr: https://www.pexels.com/photo/little-asian-girl-sitting-near-green-tree-19078973/

Photo by Toàn Đỗ Công: https://www.pexels.com/photo/a-young-man-standing-by-the-souvenir-store-23109894/

Photo by Toàn Đỗ Công: https://www.pexels.com/photo/a-young-couple-standing-on-a-sidewalk-in-a-city-23109901/

Photo by Toàn Đỗ Công: https://www.pexels.com/photo/photo-of-a-young-man-wearing-a-black-tank-top-and-glasses-standing-against-the-sea-22129916/