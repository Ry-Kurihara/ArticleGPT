#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 prefix"
  exit 1
fi

prefix="$1"
base_dir="./render/output/"

find "$base_dir" -type f -name "${prefix}_of_*" -exec rm -f {} \;

echo "All files with prefix '${prefix}' have been removed."