import os,sys
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from Video2Image import save_all_frames
from RemoveDuplicateImg import remove_duplicate_images

dt_now = datetime.datetime.now()
nt = dt_now.strftime('%Y-%m_%d-%H_%M_%S')

# フォルダ指定の関数
def dirdialog_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    entry2.set(iDirPath)
    entry3.set(iDirPath)

# ファイル指定の関数
def filedialog_clicked():
    fTyp = [("", "*")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
    entry1.set(iFilePath)

# 実行ボタン押下時の実行関数
def conductMain():
    filePath = entry1.get()
    dirPath = entry2.get() 
    removePath = entry3.get()

    if not filePath or not dirPath:
        messagebox.showinfo("エラー","必要な動画ファイル又は出力パスが未指定です。")
    else:
        #intervalはフレームレートに対して1秒間に何枚出力するか
        save_all_frames(filePath, dirPath + nt, 'img', output_interval=3)
        remove_duplicate_images(removePath)

if __name__ == "__main__":

    # rootの作成(Window部分)
    root = Tk()
    root.title("Video2Img")
    root.geometry('600x400')

    '''==================================================================== '''

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=1, sticky=E)

    # 「ファイル参照」ラベルの作成
    IFileLabel = ttk.Label(frame1, text="動画ファイル:", padding=(5, 2))
    IFileLabel.pack(side=LEFT)

    # 「ファイル参照」エントリーの作成
    entry1 = StringVar()
    IFileEntry = ttk.Entry(frame1, textvariable=entry1, width=45)
    IFileEntry.pack(side=LEFT)

    # 「ファイル参照」ボタンの作成
    IFileButton = ttk.Button(frame1, text="参照", command=filedialog_clicked)
    IFileButton.pack(side=LEFT)

    '''==================================================================== '''
    
    # Frame2の作成
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid(row=2, column=1, sticky=E)

    # 「フォルダ参照」ラベルの作成
    IDirLabel = ttk.Label(frame2, text="出力先:", padding=(5, 2))
    IDirLabel.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry2 = StringVar()
    IDirEntry = ttk.Entry(frame2, textvariable=entry2, width=45)
    IDirEntry.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    IDirButton = ttk.Button(frame2, text="参照", command=dirdialog_clicked,)
    IDirButton.pack(side=LEFT)

    '''==================================================================== '''
    
    # Frame3の作成
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=4, column=1, sticky=E)

    # 「フォルダ参照」ラベルの作成
    IDirLabel = ttk.Label(frame3, text="削除の実行先:", padding=(5, 2))
    IDirLabel.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry3 = StringVar()
    IDirEntry = ttk.Entry(frame3, textvariable=entry3, width=45)
    IDirEntry.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    IDirButton = ttk.Button(frame3, text="参照", command=dirdialog_clicked,)
    IDirButton.pack(side=LEFT)

    '''==================================================================== '''

    # Frame4の作成
    frame4 = ttk.Frame(root, padding=10)
    frame4.grid(row=6,column=1,sticky=W)

    # 実行ボタンの設置
    button1 = ttk.Button(frame4, text="実行", command=conductMain)
    button1.pack(fill = "x", padx=60, side = "left")

    # キャンセルボタンの設置
    button2 = ttk.Button(frame4, text=("閉じる"), command=quit)
    button2.pack(fill = "x", padx=60, side = "left")

    root.mainloop()
