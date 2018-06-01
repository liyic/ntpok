#!/bin/bash
cd /home/ntpok/ntpok
python2 ntpok-check.py > ntpok-check-output.txt
python2 ntpok-page.py
cd /home/ntpok
git clone https://github.com/ntpok/ntpok.github.io.git
cd /home/ntpok/ntpok.github.io
rm -vf index.html
cp /home/ntpok/ntpok/ntpok-page-output.html /home/ntpok/ntpok.github.io/index.html
cd /home/ntpok/ntpok.github.io
git add --all
git commit -m "Update"
git push -u origin master
cd ..
rm -vrf ntpok.github.io