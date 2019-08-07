import cv2
import os

"""
Copyright (c) 2017 nkmk
Released under the MIT license
https://github.com/nkmk/python-snippets/blob/master/LICENSE
"""

def save_frame_range_sec(video_path, start_sec, step_sec,
                         dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("False")
        return False

    fps = cap.get(cv2.CAP_PROP_FPS)
    end_sec = cap.get(cv2.CAP_PROP_FRAME_COUNT) * fps
    if start_sec > end_sec:
        print("start time > end time")
        return False

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    sec = start_sec
    while sec < end_sec:
        cap.set(cv2.CAP_PROP_POS_FRAMES, round(fps * sec))
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{:02.0f}m{:05.2f}s.{}'.format(base_path, sec//60, sec%60, ext), frame)
        else:
            break
        sec += step_sec
    return True

if __name__ == "__main__":
    save_frame_range_sec('4 hour.MOV', 57, 60,
                         'data/result_range_sec', 'sample_video_img')
