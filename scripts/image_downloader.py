import requests, shutil

# functioin to download and save an image from a given url
def download_image(url, file_name, folder):
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(folder + "/" + file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
    else:
        print("issue downloading image")
    return 0
