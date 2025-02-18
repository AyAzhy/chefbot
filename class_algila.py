## Made By AyAzhy
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def detect_bird(img_path, model_path, labels_path):
  # Disable scientific notation for clarity
  np.set_printoptions(suppress=True)

  # Load the model
  model = load_model(model_path, compile=False)

  # Load the labels
  class_names = open(labels_path, "r").readlines()

  # Create the array of the right shape to feed into the keras model
  # The 'length' or number of images you can put into the array is
  # determined by the first position in the shape tuple, in this case 1
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

  # Replace this with the path to your image
  image = Image.open(img_path).convert("RGB")

  # resizing the image to be at least 224x224 and then cropping from the center
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  # turn the image into a numpy array
  image_array = np.asarray(image)

  # Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

  # Load the image into the array
  data[0] = normalized_image_array
## Made By AyAzhy
  # Predicts the model
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]

  # Print prediction and confidence score
  #print("Class:", class_name[2:], end="")
  #print("Confidence Score:", confidence_score)

  return  class_name[2:], confidence_score

if __name__ == "__main__":
  image_path = "images/indir.jpeg"
  model_path = "model/keras_model.h5"
  label_path = "model/labels.txt"

  name, score = detect_bird(image_path, model_path, label_path)
  if name.strip() == "Tavada Pratik Pizza":
    print(
      "1) Lavaşı tavaya koyup üzerine domates sosu sürün.",
      "2) Malzemeleri ekleyin ve kaşarı serpin.",
      "3) Kapağını kapatıp kısık ateşte 5-7 dakika pişirin.",
      "4) Dilimleyip sıcak servis edin."
    )
  if name.strip() == "Tavuklu Kremalı Makarna":
    print(
      "1) Makarnayı haşlayıp süzün.",
      "2) Tavukları tereyağında kavurun, sarımsağı ekleyin.",
      "3) Krema, tuz, karabiber ve pul biber ekleyip 5 dakika pişirin.",
      "4) Makarnayı ekleyip karıştırın, kaşar serpip servis yapın."
    )
  if name.strip() == "Karnabahar Köftesi":
    print(
      "1) Karnabaharı haşlayıp ezin.",
      "2) İçine yumurta, galeta unu, baharatlar ve kaşarı ekleyip yoğurun.",
      "3) Küçük köfteler yapıp kızgın yağda kızartın.",
      "4) Yoğurtla servis yapın."
    )
  if name.strip() == "Fırında Kaşarlı Mantar":
    print(
      "1) Mantarları temizleyip saplarını çıkarın.",
      "2) İçlerine biraz tereyağı ve tuz ekleyin.",
      "3) Üzerine rendelenmiş kaşar koyup 180°C’de 15 dakika fırınlayın.",
      "4) Sıcak servis yapın."
    )
  if name.strip() == "Çikolatalı Muzlu Krep":
    print(
      "1) Süt, un, yumurta, şeker ve kakaoyu çırpın.",
      "2) Tavada ince krep yapıp iki tarafını da pişirin.",
      "3) İçine çikolata sürüp muz ekleyin.",
      "4) Rulo yapıp dilimleyerek servis edin."
    )
  if name.strip() == "Peynirli ve Ispanaklı Börek":
    print(
      "1) Ispanağı ince doğrayın ve beyaz peynirle karıştırın.",
      "2) Yumurtayı, sütü ve yağı çırpın.",
      "3) Yufkayı serip sos sürün, iç harcı ekleyip rulo yapın.",
      "4) Üzerine yumurta sarısı sürüp 180°C’de 30 dakika pişirin."
    )
  if name.strip() == "Yoğurtlu Mercimek Köftesi":
    print(
      "1) Mercimeği haşlayıp bulgurla karıştırın, demlenmeye bırakın.",
      "2) Soğanı kavurup salçayı ekleyin, mercimekle karıştırın.",
      "3) Baharatları ekleyip yoğurun ve küçük köfteler yapın.",
      "4) Üzerine sarımsaklı yoğurt dökerek servis yapın."
    )
    ## Made By AyAzhy
  if name.strip() == "Peynirli ve Ispanaklı Börek":
    print(
      "1) Ispanağı ince doğrayın ve beyaz peynirle karıştırın.",
      "2) Yumurtayı, sütü ve yağı çırpın.",
      "3) Yufkayı serip sos sürün, iç harcı ekleyip rulo yapın.",
      "4) Üzerine yumurta sarısı sürüp 180°C’de 30 dakika pişirin."
    )
  if name.strip() == "Fırında Sebzeli Tavuk":
    print(
      "1) Sebzeleri doğrayıp fırın kabına alın.",
      "2) Tavukları ekleyip baharatları serpin.",
      "3) Zeytinyağını gezdirip 200°C’de 40 dakika pişirin."
    )
  if name.strip() == "Çıtır Soğan Halkaları":
    print(
      "1) Soğanları halka şeklinde doğrayın.",
      "2) Yumurtayı, sütü ve yağı çırpın.",
      "3) Yufkayı serip sos sürün, iç harcı ekleyip rulo yapın.",
      "4) Üzerine yumurta sarısı sürüp 180°C’de 30 dakika pişirin."
    )
  if name.strip() == "Ballı Susamlı Tavuk":
    print(
      "1) Tavukları un, tuz ve karabibere bulayıp kızartın.",
      "2) Ayrı bir tavada bal ve soya sosunu karıştırıp ısıtın.",
      "3) Tavukları sosun içine atıp iyice harmanlayın.",
      "4) Üzerine susam serperek servis edin."
    )
  if name.strip() == "Hamburger":
    print(
      "1) Köfteyi hazırlayın: Kıyma, sarımsak, tuz, karabiber, kimyon ve zeytinyağını bir kaba alıp güzelce yoğurun.",
      "2) Karışımdan 4 eşit parça alıp yuvarlak hamburger köftesi şekli verin.  ",
      "3) Köfteleri pişirin: Tavayı orta ateşte ısıtın ve az yağ ekleyin. Köfteleri 3-4 dakika önlü arkalı pişirin.",
      "4) Köfteler pişerken üzerlerine cheddar peyniri koyup erimesini bekleyin.",
      "5) Ekmekleri ısıtın: Hamburger ekmeklerini tavada hafifçe kızartın."
      "4) Hamburgeri hazırlayın:",
        "Ekmeklerin alt kısmına mayonez sürün.",
        "Üzerine marul, köfte, domates ve soğan ekleyin.",
        "Ketçap ve hardal ekleyip üst ekmeği kapatın."
    )
## Made By AyAzhy
