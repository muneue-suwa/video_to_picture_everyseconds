from os import path
from pathlib import Path
from datetime import datetime
import sys
sys.path.append(path.dirname(path.abspath(sys.argv[0])))
from capture_pictures import save_frame_range_sec

def get_filename():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        import tkinter
        from tkinter.filedialog import askopenfilename
        root = tkinter.Tk()
        root.withdraw()
        filename = askopenfilename(filetypes=[("Video", "*.MOV;*.MP4;*.AVI")],
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
        start_time = float(start_time)
        if start_time < 0:
            raise ValueError
    except ValueError:
        print("Input float(>=0) for the start time")
        return False

    step_time = input("step time(sec)[default is 60sec]: ")
    if step_time == "":
        step_time = 60
    else:
        try:
            step_time = float(step_time)
            if step_time <= 0:
                raise ValueError
        except ValueError:
            print("Input float (>0) for the step time")
            return False

    picture_filename = path.basename(filename).rsplit(".", 1)[0]
    datetimeNow = datetime.now()
    dir_name = "{}_{}".format(filename.rsplit(".", 1)[0],
                              datetimeNow.strftime('%Y%m%d_%H%M%S'))
    print("Start converting...")
    if save_frame_range_sec(filename, start_time, step_time,
                            dir_name, picture_filename):
        print("Successfully completed")
        return True
    else:
        print("Failed")
        return False


if __name__ == "__main__":
    main()
