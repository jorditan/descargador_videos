import streamlit as st
import yt_dlp
import os

class YouTubeDownloader():
  def __init__(self, url):
    self.url = url
    self.video = None
    self.youtube = 
  
  def showTitle(self):
    st.write(f"Título: {self.video.}")

def download_video(link, output_directory):
  ydl_opts = {
    'format': 'bestvideo + bestaudio/best',
    'outtml': os.path.join(output_directory,'%(ttitle)s.%(ext)s'),
    'merce_output_format': 'mp4', 
  }

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([link])
    print("Descarga completa")


  except Exception as e:
    print(f"Hubo un problema al descargar el video {e}")

link = str(input("Pega la URL del video a descagar: ")).strip()

output_directory = "D:/Desarrollo /Python/descargar_videos/videos_descargados".strip()

download_video(link, output_directory)
