# Install all of my hacking tools using a single script!

#########################
#       Install.sh      #
#   Author: Hifumi1337  #
#########################

echo "|####################################################|"
echo "|----------------------------------------------------|"
echo "# Author: Hifumi1337 (https://github.com/Hifumi1337) #"
echo "|----------------------------------------------------|"
echo "|####################################################|"

Python Dependencies
function python_dependencies () {
    pip3 install pynput==1.7.3
}

python_dependencies()

# Git clone repository - updates repo to make sure it's up to date
git clone https://github.com/Hifumi1337/cyber-suite.git