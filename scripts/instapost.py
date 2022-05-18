import image_downloader
import os

# class to track an instagram post while scraping
class InstaPost:

    # basic constructor
    def __init__(self, code, links):
        self.code = code
        self.links = links

    # simple print function
    def print_post(self):
        print("Post: " + self.code + "\n\n")
        print(self.links)

    # download all images for post using the links passed in the constructor
    def fetch_post(self, post_num):
        folder = "posts/post" + str(post_num)
        os.mkdir(folder)

        for _,link in enumerate(self.links):
            file_name = "slide_" + str(_) + ".png"
            image_downloader.download_image(link, file_name, folder)