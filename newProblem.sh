if [ $# -lt 3 ]; then
 echo "Failed - 1"
elif [ $2 != '-' ]; then
 echo 'Failed - 2'
else
 problemDesc=$3
 declare -i i
 i=1
 for var in $@; do
  if [ $i -gt 3 ]; then
   problemDesc+=" "$var
  fi
  i+=1
 done
 mkdir "$1 - $problemDesc"
 cd "$1 - $problemDesc"
 touch rosalind_${1,,}.txt
 touch ${1,,}.py
 touch output
 echo "dataset = open('rosalind_${1,,}.txt').read().split('\n')" > ${1,,}.py
 gedit ${1,,}.py &
 gedit rosalind_${1,,}.txt
fi
