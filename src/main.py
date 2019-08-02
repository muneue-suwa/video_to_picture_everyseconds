from capture_pictures import save_frame_range_sec
import tkinter
from tkinter.filedialog import askopenfilename
from os import path
from pathlib import Path
from datetime import datetime

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
    if filename:
        start_time = int(input("start time: "))
        picture_filename = path.basename(filename).split(".")[0]

        datetimeNow = datetime.now()

        dir_name = "{}_{}".format(filename.split(".")[0],
                                  datetimeNow.strftime('%Y%m%d_%H%M%S'))
        save_frame_range_sec(filename, start_time,
                             dir_name, picture_filename)


if __name__ == "__main__":
    main()
