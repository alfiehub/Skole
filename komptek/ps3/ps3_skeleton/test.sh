#!/bin/bash
FILES=./vsl_programs/*.vsl
for f in $FILES
do
  echo "\n------------------------------------------\n"
  echo "Testing if $f produced the correct tree..."

  result=$(cat $f | src/vslc | diff ${f%.vsl}.tree.correct -)

  if [ -z "$result" ]; then
    echo "\nSucess! $f produced the correct tree."
  else
    echo "Something went wrong when producing the tree for $f, check out the diff below."
    echo "$result"
  fi

done
