#!/bin/bash

if [ "$(hostname)" = "eseverett-Inspiron-7573" ]; then
    echo "Performing actions for home..."
    cd ~/Desktop/CXFEL/CXLS_Interlocks_Docs
else
    # get actual hostname
    echo "Performing actions for work..."
    cd ~/Desktop/CXLS_Interlocks_Docs
fi

current_branch=$(git rev-parse --abbrev-ref HEAD)

if [ "$current_branch" != "development" ]; then
    echo "Changing branch."
    git checkout development
fi

git add .

echo "Commit Message: "
read message

git commit -m "$message"

echo "Pushing to development."
git push
git push gitlab development

echo "Pushed to development."

echo "Push to main (y/n): "
read push

if [ "$push" = "y" ]; then
    echo "Pushing to main."
    git checkout main
    git merge development
    git push
    git push gitlab main
    echo "Pushed to main."
fi

