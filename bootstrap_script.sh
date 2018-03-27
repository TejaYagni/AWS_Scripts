#!/bin/bash
sudo yum upgrade -y
sudo yum install gcc -y
sudo yum install wget -y
cd /opt
wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz
tar xzf Python-3.5.1.tgz
cd Python-3.5.1
./configure
make altinstall
cd
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-7.0.tar.gz --no-check-certificate
tar xzf setuptools-7.0.tar.gz
cd setuptools-7.0
python setup.py install
cd
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo pip install awscli
sudo printf 'AKIAJX5NOBMPQW4XUZ5Q\nI/0Euv6Cx7a4LSDgExdUDURDpIWOxzf6FePpyoNS\nus-east-1\njson'|aws configure
