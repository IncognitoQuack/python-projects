import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp as youtube_dl

def download_video():
    try:
        url = url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube video URL")
            return
        
        save_path = filedialog.askdirectory()
        if not save_path:
            messagebox.showerror("Error", "Please select a directory to save the video")
            return

        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", f"Video downloaded successfully to {save_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def create_gui():
    root = tk.Tk()
    root.title("YouTube Video Downloader")

    url_label = tk.Label(root, text="YouTube URL:")
    url_label.pack(pady=10)

    global url_entry
    url_entry = tk.Entry(root, width=50)
    url_entry.pack(padx=20, pady=5)

    download_button = tk.Button(root, text="Download Video", command=download_video)
    download_button.pack(pady=20)

    root.geometry("400x200")
    root.mainloop()

if __name__ == "__main__":
    create_gui()
