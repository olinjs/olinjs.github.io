# Olin.js 2015

## Dependencies
Ensure that jade is installed (`npm install -g jade`).

If the file `token.txt` does not exist in the root of the directory, create it, then follow [these instructions](https://help.github.com/articles/creating-an-access-token-for-command-line-use/) to create an access token. Paste the token into the file `token.txt`.

## Updating content
To update the content of the site, edit `content/input.json`.

Then, to generate `index.html`:
```bash
$ ./watch.sh
```
...and save any file in the repository to trigger the watch script.
