@echo off

mkdir "Infos\"
cd "Infos\"
curl "-o" "ip.txt" "http:/\monip.outils-rezo.info\text"
cat "ip.txt"