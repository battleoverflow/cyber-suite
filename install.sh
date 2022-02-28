# Install all of my hacking tools using a single script!

#########################
#       Install.sh      #
#   Author: Hifumi1337  #
#########################

echo ""
echo "|####################################################|"
echo "|----------------------------------------------------|"
echo "# Author: Hifumi1337 (https://github.com/Hifumi1337) #"
echo "|----------------------------------------------------|"
echo "|####################################################|"
echo ""

# Python Dependencies
python_dependencies() {
    pip3 install pynput==1.7.3
}

python_dependencies