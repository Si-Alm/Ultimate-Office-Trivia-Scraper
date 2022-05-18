# Ultimate Office Trivia Instagram Scraper - Script Manifest

## Script List

scripts with classes denoted with an asterisk(*)

- [get_post_links.js](#get_post_link.js)
- [build_download_page.html](#build_download_page.html)
- [links_from_json.py](#links_from_json.py)
- [instapost.py](#instapost.py)*
- [image_downloader.py](#image_downloader.py)
- [text_scraper_single.py](#text_scraper_single.py)
- [extract_images_slurm.sbatch](#extract_images_slurm.sbatch)
- [post.py](#post.py)*
- [format_text_dumps.py](#format_text_dumps.py)

## Script Descriptions

### [get_post_links.js](../scripts/get_post_links.js)

**Function:** The purpose of this script is to scrape all of the post links from an instagram account. It can simply be executed in the console developer tool in a browser where it will save the post links in an array. This array can be copied and pasted into the `build_download_page.html`. Though the script should work in most moder browsers, it was tested and ran in Firefox 100.0.1.

### [build_download_page.html](../scripts/build_download_page.html)

**Function:** This "script" functions in a whacky way. In order to get the links to the publicly hosted images for the posts, I needed a way to mass download the json representation of all the post links that were scraped with `get_post_links.js`. Accesing the json reprsentation is simply the matter of adding an extra parameter onto the original post link. However, to access the page, you must be logged in - meaning this needs to be done in a browser. Enter the "simple mass downloader" chrome extension. The way this extension functions is the reason why this script is in a simple webpage. This extension lets you mass download web pages/resources by scanning a webpage for links, which can then be selected in bulk and downloaded. So this script takes the array of post links, appends the json retreiving paramater to them, and displays them on a simple webpage. The mass downloader extension can then be used to select the links and download them, making sure to specify the .json extension to get the correct file type. After so many requests, Instagram may block your account from sending these types of requests. It will get lifted after a while, so make sure to note the downloaded files - which can be added to an "ignore" array in the script.

### [links_from_json.py](../scripts/links_from_json.py)

**Function:** Once all of the json representatioons of the posts are downloaded, the next stpe is to pull all of the image links from them. This script just searches through every json file, finds the "carousel media", extracts the link for a middle-size version of the images, and saves them to an array of objects using the `InstaPost` class from `instapost.py`. Once all of the links are scraped, the array of objects is iterated over and each post has its images downloaded and organized into folders.

### [instapost.py](../scripts/instapost.py)

**Function:** This file holds the helper class used to store posts in the `links_from_json.py` script. It has two instance fields, one to hold the post id/code and one to hold an array of image links. It has a printing method and a method to download the links instance field into a folder of organized images. This second method uses a helper function from the `image_downloader.py` script to download the images.

### [image_downloader.py](../scripts/image_downloader.py)

**Function:** There's one helper function in this script that uses the requests and shutil libraries to download a given url to a given file/directory.

### [text_scraper_single.py](../scripts/text_scraper_single.py)

**Function:** This script was used to scrape text from images in batches, scaling across nodes of the Hyalite HPC. When running this code, the number of posts broke down into 36 batches of 29 posts. This script gets parsed a value between 1 and 36, finds the folders for the appropriate range of posts, creates object representations of the posts (using the `Post` object from `post.py`), then sequentially extracts the text from them.

### [extract_images_slurm.sbatch](../scripts/extract_images_slurm.sbatch)

**Function:** This short shell script was used in conjunction with `text_scraper_single.py` and the SLURM scheduler on Hyalite HPC to scrape all of the text from every post image.

### [post.py](../scripts/post.py)

**Function:** -*This script is still being expanded*- This class currently holds two helper classes, one to represent posts and one to represent questions. Originally, when the text dumps were being extracted from the images, the post class just held the post number and the paths of the images to pull text from. This original class also had one method that used the pytesseract Optical Character Recognition (OCR) library and opencv python library to pull the text from every image in the class instance field and save it as a .txt file. The script is currently being expanded to format these text dumps and save the posts/questions in a standardized format.

### [format_text_dumps.py](../scripts/format_text_dumps.py)

**Function:** Yet to be written, this script will use the expanded `post.py` script to extract all necesssary text in the post text dumps and save it in a standardized format. Essentially a driver for the functionality built in the post and question classes. It will also uses `post_stats_tracker.py` to log information on the questions (season distributions, number of incompletly parsed posts, etc.).

### [post_stats_tracker.py](../scripts/post_stats_tracker.py)

**Function:** This script, which is also currently unwritten, will be used to track information on posts when parsing through all of the text dumps.
