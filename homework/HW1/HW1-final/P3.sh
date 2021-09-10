grep -c "[0-9]" apollo13.txt > apollo_out.txt
grep --help |& fgrep -e --count
ls -d *.py* | wc -l
find . -type f | ls -l | grep "^-rwxrwx--x"
find . -maxdepth 1 | ls -l | grep "^-rwxrwx--x"
 
