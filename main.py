import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
import yt_dlp

def download_media(url, output_format, status_callback):
    # Tentukan opsi unduhan berdasarkan format output
    ydl_opts = {
        'outtmpl': '/sdcard/Download/output.%(ext)s',  # Simpan di folder Download Android
    }
    if output_format.lower() == 'mp3':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })
    elif output_format.lower() == 'wav':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }]
        })
    else:  # mp4 atau format video lainnya
        ydl_opts['format'] = 'best'

    try:
        status_callback("Mengunduh...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_callback("Unduhan selesai.")
    except Exception as e:
        status_callback(f"Error: {e}")

class DownloaderApp(App):
    def build(self):
        self.title = "Downloader App"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input URL
        self.url_input = TextInput(hint_text="Masukkan URL", size_hint_y=None, height=40)
        # Pilihan format output
        self.format_spinner = Spinner(
            text='mp4',
            values=('mp4', 'mp3', 'wav'),
            size_hint_y=None,
            height=40
        )
        # Label status
        self.status_label = Label(text="Status: Idle")

        download_button = Button(text="Download", size_hint_y=None, height=50)
        download_button.bind(on_press=self.start_download)

        layout.add_widget(self.url_input)
        layout.add_widget(self.format_spinner)
        layout.add_widget(download_button)
        layout.add_widget(self.status_label)

        return layout

    def start_download(self, instance):
        url = self.url_input.text.strip()
        output_format = self.format_spinner.text
        if url:
            # Jalankan unduhan di thread terpisah agar UI tidak freeze
            threading.Thread(target=download_media, args=(url, output_format, self.update_status)).start()
        else:
            self.update_status("Masukkan URL yang valid.")

    def update_status(self, message):
        self.status_label.text = "Status: " + message

if __name__ == '__main__':
    DownloaderApp().run()
