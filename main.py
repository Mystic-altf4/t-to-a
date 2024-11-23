import pyttsx3

def metni_sese_donustur(metin):
    # pyttsx3 motorunu başlat
    engine = pyttsx3.init()

    # Ses hızını ve tonunu ayarlayabilirsiniz (isteğe bağlı)
    engine.setProperty('rate', 150)  # Hız
    engine.setProperty('volume', 1)  # Ses yüksekliği (0.0 ile 1.0 arasında)

    # Metni sesli olarak oku
    engine.say(metin)

    # Sesin bitmesini bekleyin
    engine.runAndWait()

# Kullanıcıdan metin al
metin = input("Metninizi girin: ")
metni_sese_donustur(metin)
