#!/bin/bash

# $1 - Input markdown practical (with path)
# $2 - Output filename with no extension (with path)

pandoc $1 -s --mathjax -o $2.html --metadata date="`date +%D`" -s -H css/pandoc.css

# sed is replacing (../../img/ with (img/ so the pdf build works
sed -i '' 's:(\.\./\.\./img/:(img/:g' $1

pandoc $1 -o $2.pdf --from markdown --template eisvogel --listings --metadata date="`date +%D`"

# Then we change the path back to how it was
sed -i '' 's:(img/:(\.\./\.\./img/:g' $1
