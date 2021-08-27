sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
sed -i 's/robbyrussell/agnoster/g' ~/.zshrc
echo 'startx' >> ~/.zshrc\nexit
su $1
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
sed -i 's/robbyrussell/agnoster/g' /home/$1/.zshrc
echo 'startx' >> /home/$1/.zshrc\nexit