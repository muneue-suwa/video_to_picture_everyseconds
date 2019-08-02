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
    if not filename:
        print("File was not selected")
        return False

    start_time = input("start time(sec): ")
    try:
        start_time = int(start_time)
    except ValueError:
        print("Input integer for the start time")
        return False

    step_time = input("step time(sec)[default is 60sec]: ")
    if step_time == "":
        step_time = 60
    else:
        try:
            step_time = int(step_time)
        except ValueError:
            print("Input integer for the step time")
            return False

    picture_filename = path.basename(filename).rsplit(".", 1)[0]

    datetimeNow = datetime.now()

    dir_name = "{}_{}".format(filename.rsplit(".", 1)[0],
                                datetimeNow.strftime('%Y%m%d_%H%M%S'))
    save_frame_range_sec(filename, start_time, step_time,
                            dir_name, picture_filename)

    return True


if __name__ == "__main__":
    if not main():
        print("Failed")
