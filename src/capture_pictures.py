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
        return
    
    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)
    
    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
    
    fps = cap.get(cv2.CAP_PROP_FPS)

    stop_sec = round(cap.get(cv2.CAP_PROP_FRAME_COUNT) * fps)

    for sec in range(start_sec, stop_sec, step_sec):
        n = round(fps * sec)
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{:02d}{:02d}.{}'.format(base_path, sec//60, sec%60, ext), frame)
            n += 1
        else:
            return

if __name__ == "__main__":
    save_frame_range_sec('4 hour.MOV', 57, 60,
                         'data/result_range_sec', 'sample_video_img')
