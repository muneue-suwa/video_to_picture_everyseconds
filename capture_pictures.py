import cv2
import os


def save_frame_range_sec(video_path, start_sec, stop_sec, step_sec,
                         dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("False")
        return
    
    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)
    
    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    for sec in range(start_sec, stop_sec, step_sec):
        n = round(fps * sec)
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return

if __name__ == "__main__":
    save_frame_range_sec('4 hour.MOV',
                         57, 15*60, 60,
                         'data/result_range_sec', 'sample_video_img')
