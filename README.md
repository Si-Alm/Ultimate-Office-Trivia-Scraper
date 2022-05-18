# Ultimate Office Trivia - Instagram Account Scraping

[Ultimate Office Trivia](https://www.instagram.com/ultimateofficetrivia/) is a phenomenal, but now dead Instagram account. While the account is still public and exists I want to turn this awesom page into an office trivia API/quiz website. Such an API would require an extensive question set, which I think this account can provide. Building the API itself will be simple, but will first require all of the images from the account to be scraped, parsed for text, and formatted. Instagram doesn't offer a publicly facing API to interact with the site, so this will take some hacky workarounds and scripts with a narrow scope. So this project will be maintained to document this process.

A [list and description](./docs/script_manifest.md) of the scripts used in this project can be found in the docs.

## Tech Used

## Python Libraries/Dependencies

- os
- requests
- shutil
- sys
- json
- re
- cv2
- pytesseract

## Other tools

- VSCode
- [Simple mass downloader](https://chrome.google.com/webstore/detail/simple-mass-downloader/abdkkegmcbiomijcbdaodaflgehfffed?hl=en-US) chrome extension
- [Hyalite HPC](https://www.montana.edu/rci/hyalite/) (not publicly available)
- SLURM scheduler
