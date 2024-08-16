from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from ffpyplayer.player import MediaPlayer
from threading import Thread


class StreamPlayerApp(MDApp):
    def build(self):
        self.player = None
        self.playback_thread = None
        self.is_playing = False
        return Builder.load_file('main.kv')

    def play_stream(self):
        if self.is_playing:
            return  # Prevent starting the stream multiple times

        stream_url = "http://uk1.internet-radio.com:8004"
        self.player = MediaPlayer(stream_url)
        self.root.ids.status_label.text = "Playing stream"
        self.is_playing = True

        # Run the audio playback in a separate thread
        self.playback_thread = Thread(target=self.play_audio)
        self.playback_thread.start()

    def play_audio(self):
        while self.is_playing:
            frame, val = self.player.get_frame()
            if val == 'eof':  # End of file, stop playback
                break
            if frame is None:
                continue

        self.is_playing = False
        self.root.ids.status_label.text = "Stream stopped"

    def stop_stream(self):
        if self.is_playing:
            self.is_playing = False
            if self.player:
                self.player.close_player()
            self.player = None
            self.root.ids.status_label.text = "Stream is stopped"
            if self.playback_thread:
                self.playback_thread.join()  # Ensure the playback thread has finished

if __name__ == '__main__':
    StreamPlayerApp().run()
