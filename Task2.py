class Video:
    def __init__(self):
        self.name = None

    def create(self, name):
        self.name = name

    def play(self):
        print(f"Відтворення відео {self.name}")

class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_index):
        if 0 <= video_index < len(cls.videos):
            cls.videos[video_index].play()
        else:
            print("Не знайдено відео.")

if __name__ == '__main__':
    video1 = Video()
    video1.create("Основи програмування")

    video2 = Video()
    video2.create("Вивчення Python за 45 хвилин!")

    YouTube.add_video(video1)
    YouTube.add_video(video2)

    YouTube.play(0)
    YouTube.play(1)