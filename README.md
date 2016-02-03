# stratalogue
git clone https://github.com/devints47/stratalogue.git
vagrant up
vagrant ssh
mysql -u root -pbacktoa
CREATE DATABASE stratalogue;create user 'rushb'@'localhost' identified by 'backtoa';GRANT ALL PRIVILEGES ON * . * TO 'rushb'@'localhost';
python manage.py migrate
