import os
from moviepy.editor import VideoFileClip#pip install moviepy
from PIL import Image#pip install pillow
def generate_video_covers(root_folder):
    covers = []
    def generate_video_cover(video_path, output_path):
        try:
            clip = VideoFileClip(video_path)  # 打开视频文件
            duration = clip.duration  # 获取视频时长
            middle_time = duration / 2  # 计算视频中间时间

            frame = clip.get_frame(middle_time)  # 获取中间时间的帧
            clip.close()  # 关闭视频剪辑

            image = Image.fromarray(frame)  # 创建PIL图像对象
            image.save(output_path)  # 将图像保存为视频封面图片

            covers.append(output_path)
        except Exception as e:
            print(f"无法处理视频文件: {video_path}，错误: {str(e)}")

    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            extension = os.path.splitext(filename)[1].lower()
            if extension in ['.mp4', '.mov', '.avi', '.mkv']:  # 常见视频扩展名
                video_path = os.path.join(dirpath, filename)
                cover_filename = os.path.splitext(filename)[0] + '.jpg'
                cover_path = os.path.join(dirpath, cover_filename)

                generate_video_cover(video_path, cover_path)  # 为视频生成封面

    return covers

# 示例用法
root_folder = os.getcwd()  # 根文件夹路径

covers = generate_video_covers(root_folder)  # 为根文件夹下的所有视频生成封面

# 打印封面路径
for cover_path in covers:
    print(f"封面路径：{cover_path}")
