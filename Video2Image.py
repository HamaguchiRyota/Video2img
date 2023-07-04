import cv2
import os
'''
import datetime
dt_now = datetime.datetime.now()
nt = dt_now.strftime('%Y-%m_%d-%H_%M_%S')
'''

def save_all_frames(video_path, dir_path, basename, ext='jpg', output_interval=3):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("動画ファイルが見つかりませんでした。\n")
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    # ビデオのフレームレートを取得
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    # 出力する間隔（秒数）をフレーム数に変換
    output_interval_frames = frame_rate * output_interval

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if ret:
            frame_count += 1
            if frame_count % output_interval_frames == 0:
                fname = '{}_{}.{}'.format(base_path, str(n).zfill(digit), ext)
                cv2.imwrite(fname, frame)
                n += 1
                print("Saved frame:", fname)
        else:
            break  #return

    cap.release()

#save_all_frames('input/in.mp4', 'output/'+ nt, 'img', output_interval=3)
