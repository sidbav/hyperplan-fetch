#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1
fi

speed_yaml_files=`ls *speed.yaml`

for file in $speed_yaml_files
do
  echo $file
  new_file="${file/speed/$1}"
  cp $file $new_file
  sed -i '' "s/speed/$1/1" $new_file
done

