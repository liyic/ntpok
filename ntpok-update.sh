#!/bin/bash
cd /home/ntpok/ntpok
python2 ntpok-check.py > ntpok-check-output.txt
python2 ntpok-page.py
cd /home/ntpok
git clone git@github.com:ntpok/ntpok.github.io.git
cd /home/ntpok/ntpok.github.io
rm -vf index.html
cp /home/ntpok/ntpok/ntpok-page-output.html /home/ntpok/ntpok.github.io/index.html
cd /home/ntpok/ntpok.github.io
rm -rf .git
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:ntpok/ntpok.github.io.git
git push -u --force origin master
cd ..
rm -vrf ntpok.github.io
