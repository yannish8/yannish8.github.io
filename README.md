# yannish8.github.io

Commands to deploy to GitHub pages:

``` bash
# Run Pelican to generate the static HTML files in output
pelican content -o output -s publishconf.py

# Use ghp-import to add the contents of the output directory to the master branch
ghp-import -m "Generate Pelican site" --no-jekyll -b master output

# Push the local master branch to the remote repo
git push origin master

# Commit and push the new content to the content branch
git add content
git commit -m "A commit message"
git push origin content
```

