import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment
import os
import numpy as np

class VideoEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Logiciel de Montage Vidéo")
        self.root.geometry("800x600")
        
        self.video_path = ""
        self.video_clip = None
        self.audio_clip = None
        self.output_path = ""

        self.create_widgets()

    def create_widgets(self):
        # Charger vidéo
        self.load_button = tk.Button(self.root, text="Charger Vidéo", command=self.load_video)
        self.load_button.pack(pady=10)

        # Couper vidéo
        self.cut_button = tk.Button(self.root, text="Couper la vidéo", command=self.cut_video)
        self.cut_button.pack(pady=10)

        # Ajouter audio
        self.add_audio_button = tk.Button(self.root, text="Ajouter Audio", command=self.add_audio)
        self.add_audio_button.pack(pady=10)

        # Sauvegarder vidéo
        self.save_button = tk.Button(self.root, text="Sauvegarder Vidéo", command=self.save_video)
        self.save_button.pack(pady=20)

    def load_video(self):
        """ Charger une vidéo depuis le disque """
        self.video_path = filedialog.askopenfilename(filetypes=[("Fichiers vidéo", "*.mp4 *.avi *.mov")])
        if self.video_path:
            self.video_clip = cv2.VideoCapture(self.video_path)
            self.show_message(f"Vidéo chargée avec succès!")

    def cut_video(self):
        """ Couper la vidéo entre deux temps """
        if self.video_clip:
            start_time = float(filedialog.askstring("Début", "Entrer le temps de début (en secondes) :"))
            end_time = float(filedialog.askstring("Fin", "Entrer le temps de fin (en secondes) :"))
            self.create_video_clip(start_time, end_time)
            self.show_message(f"Vidéo coupée entre {start_time}s et {end_time}s.")

    def create_video_clip(self, start_time, end_time):
        """ Créer un clip vidéo en fonction du temps de début et de fin """
        fps = int(self.video_clip.get(cv2.CAP_PROP_FPS))
        start_frame = int(start_time * fps)
        end_frame = int(end_time * fps)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.output_path = "output_video.mp4"
        out = cv2.VideoWriter(self.output_path, fourcc, fps, (int(self.video_clip.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                                                int(self.video_clip.get(cv2.CAP_PROP_FRAME_HEIGHT))))

        self.video_clip.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        while True:
            ret, frame = self.video_clip.read()
            if not ret or self.video_clip.get(cv2.CAP_PROP_POS_FRAMES) > end_frame:
                break
            out.write(frame)

        out.release()

    def add_audio(self):
        """ Ajouter un fichier audio à la vidéo """
        audio_path = filedialog.askopenfilename(filetypes=[("Fichiers audio", "*.mp3 *.wav")])
        if audio_path:
            self.audio_clip = AudioSegment.from_file(audio_path)
            self.show_message(f"Audio ajouté avec succès!")

    def save_video(self):
        """ Sauvegarder la vidéo modifiée """
        if self.output_path and self.audio_clip:
            video_clip = cv2.VideoCapture(self.output_path)
            audio_path = "output_audio.wav"
            self.audio_clip.export(audio_path, format="wav")

            video_fps = int(video_clip.get(cv2.CAP_PROP_FPS))
            video_width = int(video_clip.get(cv2.CAP_PROP_FRAME_WIDTH))
            video_height = int(video_clip.get(cv2.CAP_PROP_FRAME_HEIGHT))

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            output_file = "final_output.mp4"
            out = cv2.VideoWriter(output_file, fourcc, video_fps, (video_width, video_height))

            while True:
                ret, frame = video_clip.read()
                if not ret:
                    break
                out.write(frame)

            out.release()
            video_clip.release()

            self.show_message(f"Vidéo sauvegardée avec succès sous {output_file}")

    def show_message(self, message):
        """ Afficher un message """
        messagebox.showinfo("Information", message)

# Exécution de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = VideoEditorApp(root)
    root.mainloop()
