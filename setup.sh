#!/bin/bash

dep=('discord' 'pandas')

echo -n "Do you want to install required dependencies for Yuki-chan? (y/n):"
read response

if [ ${response,,} == 'y' ];
then
  for el in ${dep[@]}
  do
    pip install $el
  done
  clear
  echo "Successfully installed all required dependencies ^-^"
else
  clear
  echo "No dependencies will be installed."
fi
