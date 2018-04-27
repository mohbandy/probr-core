sudo apt-get install screen
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install apt-transport-https ca-certificates curl gnupg
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
echo "deb [arch=armhf] https://download.docker.com/linux/debian \
$(lsb_release -cs) stable" |     sudo tee /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get install docker-ce
sudo apt-get install --reinstall docker-ce
sudo apt-get install python-pip
sudo pip install docker-compose
sudo pip install virtualenv
virtualenv .env_probr
sudo pip install Django
sudo apt-get install npm
sudo npm install -g bower
sudo ln -s /usr/bin/nodejs /usr/bin/node
source .env_probr/bin/activate
git clone https://github.com/probr/probr-core.git && cd probr-core
git checkout fix/dependencies
sudo usermod -a -G docker $USER
sudo reboot
