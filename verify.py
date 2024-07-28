from deepface import DeepFace

verification = DeepFace.verify(
  img1_path = "photo/pexels-fr3sh-19078970.jpg",
  img2_path = "photo/pexels-fr3sh-19078969.jpg"
)