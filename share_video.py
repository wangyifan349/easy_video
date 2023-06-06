from flask import Flask, render_template
import os
import numpy as np
from PIL import Image
from moviepy.editor import VideoFileClip
app = Flask(__name__)
VIDEO_FOLDER = os.path.join(os.getcwd(), 'static')
def extract_thumbnail(image_path, output_path):
    image = Image.open(image_path)  # 打开封面图片
    image.save(output_path)  # 将封面图片保存为缩略图
def generate_video_list(folder_path):
    videos = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp4'):  # 仅处理以.mp4结尾的文件
            video_path = os.path.join(folder_path, filename)  # 视频文件路径
            thumbnail_path = os.path.join(folder_path, f'{os.path.splitext(filename)[0]}.jpg')  # 缩略图文件路径
            extract_thumbnail(video_path, thumbnail_path)  # 提取视频缩略图
            videos.append({'title': filename, 'thumbnail': thumbnail_path})  # 存储视频和缩略图信息
    return videos#返回一个列表，里面是视频。
@app.route('/')
def index():
    videos = generate_video_list(VIDEO_FOLDER)  # 生成视频列表
    return render_template('index.html', videos=videos)  # 渲染模板并传递视频列表

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)  # 启动应用
