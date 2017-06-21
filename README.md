A library to fetch news from various sources.
 
===
Development on Fedora 25

Required rpms:
sudo yum -y install libxml2-devel libxslt-devel libxml-devel openjpeg2-devel
 libjpeg-turbo-devel zlib-devel libtiff-devel libfreetype-devel freetype-devel 
 littlecms-devel libwebp-devel libimagequant-devel



The requirements use a clone of newspaper from master on github. 

Install Pillow from github.

git clone https://github.com/python-pillow/Pillow.git
cd Pillow 
python setup.py install 

Install newspaper from github

https://github.com/codelucas/newspaper.git
cd newspaper
python setup.py install

Test
---
    make test7        

You can also test with a specific version of Python:
    make PYTHON_VERSION=2.7.11 test

