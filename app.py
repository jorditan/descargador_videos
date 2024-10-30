from pytube import YouTube
import streamlit as st


class YoutubeDownloader():
  def __init__(self, url):
    self.url = url
    self.youtube = YouTube(self.url, on_progress_callback=YoutubeDownloader.onProgress)
    self.stream = None
  
  def showTitle(self):
    # st.write(f"Título: {self.youtube.title}")
    st.write(f"Título: {(self.youtube.thumbnail_url)}")
    self.showStreams()
    
  def showStreams(self):
    streams = self.youtube.streams
    streams_optiones= [
      f"Resolución: {
        stream.resolution or 'N/A'} / FPS: {getattr(stream, 'Fps', 'N/A')} / Tipo: {stream.mime_type}"
        for stream in streams
    ]

    choice = st.selectbox("Elija una opcion de stream:", streams_optiones)
    
    self.stream = streams[streams_optiones.index(choice)]

  def getFileSize(self):
    file_size = self.stream.filesize / 1000000
    return file_size


  def gePermissonToContinue(self, file_size):
    st.write(f"**Título** {self.youtube.title}")

    st.write(f"**Autor** {self.youtube.author}")
    st.write(f"**Tamaño** {file_size: 2.f} MB")

    if st.button("Descargar"):
      self.download()

  def downloand(self):
    self.stream.download()
    st.success("¡Descarga completada!")

  @staticmethod
  def onProgress(stream=None, chunk=None, remaining=None):
    file_size = stream.filesize / 1000000
    file_download = file_size - (remaining/1000000)
    st.progress(file_download / file_size)

  
if __name__ == "__main__":
  st.title("Descargar de videos de Youtube")
  url = st.text_input("Ingrese la URL del video:")

  if url:
    dowloader = YoutubeDownloader(url)
    dowloader.showTitle()
    if dowloader.stream:
      file_size = dowloader.getFileSize()
      dowloader.gePermissonToContinue(file_size)

