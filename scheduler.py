#This script will be the code to automate the process every day

env EDITOR=nano crontab -e

0 7 * * *  cd ~/my/backup/folder && ./backup.sh