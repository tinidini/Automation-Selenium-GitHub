#!/bin/bash

function create()

{   
    read -p "Numele proiectului: " fname
    python3 create.py $fname 

    
    cd /Users/adinaciubancan/Documents/MyProjects/$fname
    pwd

    git init
    git remote add origin https://github.com/tinidini/${fname}.git
    touch README.md
    echo "Am scris in readme" >> README.md
    git add *
    git commit -m "Initial commit"
    git push -u origin master
    
    #code .
    
}

"$@"
