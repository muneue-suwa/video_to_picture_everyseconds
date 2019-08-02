from capture_pictures import save_frame_range_sec
import tkinter
from tkinter.filedialog import askopenfilename
from os import path
from pathlib import Path

def get_filename():
    root = tkinter.Tk()
    root.withdraw()
    filename = askopenfilename(filetypes=[("Video", "*.MOV")],
                               initialdir=path.join(str(Path.home()),
                               "Desktop"))

    if filename == "":
        print("no file")
        return False

    print(filename)
    return filename

def main():
    filename = get_filename()
    start_time = input("start time:")
    picture_filename = path.basename(filename).split(".")[0]
    save_frame_range_sec(filename, start_time, 
                         filename.split(".")[0], picture_filename)


if __name__ == "__main__":
    main()
