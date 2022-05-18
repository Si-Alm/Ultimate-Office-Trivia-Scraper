import json
import os
import instapost

# function to extract image links from json representation of post
def parse_links(json_string):
    try:
        # pull the first "item" object from json
        sub_str = json_string['items'][0]

        # we need to pull links from a carousel media array, so verify that it exists
        if 'carousel_media' in sub_str:
            # get number of images in post
            num_img = int(sub_str['carousel_media_count'])

            # pull and store links for post images
            links = [0] * num_img
            for i in range(num_img):
                links[i] = sub_str['carousel_media'][i]['image_versions2']['candidates'][7]['url']

            # get post id/code from json
            code = sub_str['code']

            # save info as Instapost object and return
            cur_post = instapost.InstaPost(code,links)
            return cur_post
        else:
            # this means there's only 1 image - i.e. we can skip this post
            return -1
    except Exception as e:
        print(e)

    return -1

posts = []

# traverse whole directory
for root, dirs, files in os.walk("../artifacts/scraped_json/"):
    # select file name
    for file in files:
        # check for .json extension
        if file.endswith('.json'):
            path = os.path.join(root, file)
            f = open(path)
            data = json.load(f)
            result = parse_links(data)

            if -1 != result:
                posts.append(result)

for i,cur_post in enumerate(posts):
    print("Fetching post: " + cur_post.code)
    cur_post.fetch_post(i)
