from pytube import YouTube
import os

link = input("İndirilecek bağlantının linkini giriniz: ")
yt_mp3 = YouTube(str(link))
video_sesi = yt_mp3.streams.filter(only_audio=True).first()
dizin = 'Müzikler'
mp3_dosyasi=video_sesi.download(output_path = dizin)

base , ext = os.path.splitext(mp3_dosyasi)
new_file = base +'.mp3'
os.rename(mp3_dosyasi,new_file)
print(yt_mp3.title + " Başarı ile indirildi ")

#Created by Arda DOĞRUL