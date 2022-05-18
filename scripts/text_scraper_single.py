import os
from post import Post
from multiprocessing import Pool
import sys

# local system test path
POSTS_PATH = "./posts/"

#POSTS_PATH = os.environ.get("HOME") + "/Final/posts/"

# get job array value
job_num = int(sys.argv[1])

# set bounds of posts to parse on this job
lower_range = (job_num - 1)*29
upper_range = lower_range + 29

# get all the posts in the directory
post_dirs = os.listdir(POSTS_PATH)

# sort posts - os.listdir is unordered
post_dirs = sorted(post_dirs, key = lambda k: int(k.split('post')[1]))

# set up trackers
posts_to_parse = []
post_counter = lower_range

# iterate over every post within the bounds
for dir in post_dirs[lower_range:upper_range]:
    post_path = os.path.join(POSTS_PATH,dir)

    # accumulate files to examine for current post
    cur_post_files = []
    for filename in os.listdir(post_path):
        f = os.path.join(post_path, filename)

        if os.path.isfile(f):
            cur_post_files.append(f)

    # add post with files and increment tracker
    posts_to_parse.append(Post(post_counter, cur_post_files))
    post_counter += 1


# get text dumps for all posts in this batch
for post in posts_to_parse:
    post.extract_post_text()