#!/bin/bash

pandoc handbook.md -o GEG6230-Handbook.pdf --from markdown --template eisvogel --listings --metadata date="`date +%D`"
