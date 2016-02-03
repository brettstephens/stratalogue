#!/usr/bin/env bash

apt-get update
apt-get -y upgrade

apt-get install -y git subversion curl vim screen ssh
apt-get install -y lynx links links2


######################### Python #########################
apt-get -y install python-pip python-dev build-essential python-virtualenv

######################### MySQL #########################
MYSQL_PASSWORD="backtoa"

echo "mysql-server-5.5 mysql-server/root_password password $MYSQL_PASSWORD" | debconf-set-selections
echo "mysql-server-5.5 mysql-server/root_password_again password $MYSQL_PASSWORD" | debconf-set-selections

apt-get -y install mysql-client mysql-server sqlite3 
apt-get -y install python-mysqldb libmysqlclient-dev python-mysql.connector python3-mysql.connector


######################### Django environment #########################
pip install django
pip install MySQL-python


mysql -u root -pbacktoa 
mysql -e "CREATE DATABASE stratalogue;"
mysql -e "create user 'rushb'@'localhost' identified by 'backtoa';"
mysql -e "GRANT ALL PRIVILEGES ON * . * TO 'rushb'@'localhost';"
mysql -e "exit"


deactivate