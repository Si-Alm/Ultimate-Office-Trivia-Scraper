import cv2
import pytesseract as pt
import os
import re

class Question:
    def __init__(self, question = "", options = [], answer = "", answer_letter = ""):
        self.question = question
        self.options = options
        self.answer = answer
        self.answer_letter = answer_letter
        self.difficulty = 0

    def __str__(self):
        ret_str = f"Question: {self.question}\nOptions: {self.options}\nAnswer: {self.answer}\nLetter: {self.answer_letter}\nDifficulty: {self.difficulty}"
        return ret_str

    def parse_question(self,text_dump):
        for slide_text in text_dump:
            print(slide_text)

        # difficulty regex: /THREAT LEVEL:\s\d{1,2}/g
        return 0
        
class Post:
    OUTPUT_DIR_BASE = os.environ.get("HOME") + "/Final/" 

    def __init__(self, post_num = -1, paths = [], post_folder = ""):
        self.post_num = post_num
        self.paths = paths

        if not "" == post_folder:
            self.season = -1
            self.episode = -1
            self.episode_name = ""
            self.post_from_text_dump(post_folder)

    
    def __str__(self):
        ret_str = f"Season {self.season}\nEpisode {self.episode}\nName: {self.episode_name}"
        return ret_str

    
    def post_from_text_dump(self,post_folder):
        # do filewalk and get text from all slide files - they will be unordered
        # find slide with best match for pattern "<SEASON N EPISODE M: EPISODE NAME>"
        # note relevant info in instance field
        # parse question

        text_dump = []

        for root, dirs, files in os.walk(post_folder):
            for file in files:
                path = os.path.join(root, file)
                f = open(path)
                text_dump.append(f.read())

        self.get_episode_info(text_dump)
        print("\n\n")
        self.question = Question()
        self.question.parse_question(text_dump)

        print(self)
        print(self.question)

        return 0

    def get_episode_info(self,text_dump):
        for slide_text in text_dump:
            found_season = re.search("SEASON\s\d{1,2}", slide_text)
            found_episode = re.search("EPISODE\s\d{1,2}", slide_text)

            found_name = False

            if not None == found_episode:
                e_num = found_episode.group().split(" ")[1]
                self.episode = e_num

                found_name = self.parse_name(slide_text, found_episode.span())


            if not None == found_season:
                s_num = found_season.group().split(" ")[1]
                self.season = s_num

                if False == found_name:
                    found_name = self.parse_name(slide_text, found_season.span())
                    
        return 0
    
        
    def parse_name(self, slide_text, range):
        name_cover = slide_text[range[1]:range[1]+50]
        name_cover = name_cover.split("\n")[0]

        unformatted = name_cover.split(":")[1]
        formatted = unformatted[1:]

        if not None == formatted:
            self.episode_name = formatted
            return True

        return False


    def extract_post_text(self):
        output_dir = self.OUTPUT_DIR_BASE + self.post_num + "/"
        os.mkdir(output_dir)
        
        for i,path in enumerate(self.paths):
            img = cv2.imread(path)
            img = cv2.resize(img, None, fx=2, fy=2)
            extracted_text = pt.image_to_string(img)

            text_dump_path = output_dir + "slide_" + str(i) + "dump.txt"
            text_dump = open(text_dump_path, "wb")
            text_dump.write(extracted_text)

        


def main():
    test_path = "./final_stuff/output/891"
    np = Post(post_folder=test_path)


main()