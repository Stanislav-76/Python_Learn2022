import tkinter as tk
import tkinter.ttk as ttk
from pytube import YouTube


def progress(stream=None, chunk=None, remaining=0):    
    file_downloaded = (file_size - remaining)
    per = (file_downloaded / file_size) * 100         
    progress_bar.config(value=format(per))
    window.update()

def load():
    global file_size
    global yt    
    progress_bar.config(value=0)
    link = ent_link.get()
    path = ent_path.get()
    yt = YouTube(link, on_progress_callback=progress) # on_progress_callback=progress_func
    yt.streams.filter(progressive=True, file_extension='mp4')
    yt.streams.order_by('resolution')
    yt.streams.desc()
    file_size = yt.streams.first().filesize
    yt.streams.first().download(path)


window = tk.Tk()
window.title("Скачай видео с Ютуба!")
lbl_link = tk.Label(text="Вставьте ссылку на видео, которое хотите скачать", font=30, relief=tk.RIDGE , borderwidth=10)
lbl_link.pack(fill=tk.X, padx=5, pady=5)
ent_link = tk.Entry(bg='Azure', font=30, relief=tk.SUNKEN, borderwidth=10)
ent_link.pack(fill=tk.X, padx=5, pady=5)
lbl_path = tk.Label(text="Укажите папку куда скачать файл", font=30, relief=tk.RIDGE, borderwidth=10)
lbl_path.pack(fill=tk.X, padx=5, pady=5)
ent_path = tk.Entry(bg='Azure', font=30, relief=tk.SUNKEN, borderwidth=10)
ent_path.pack(fill=tk.X, padx=5, pady=5)
progress_bar = ttk.Progressbar(orient="horizontal", mode="determinate", maximum=100, value=0)
progress_bar.pack(fill=tk.X, padx=5, pady=5)
btn = tk.Button(text="Загрузить видео!", font=100, command=load)
btn.pack(padx=5, pady=5)
window.mainloop()