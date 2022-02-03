#!/bin/bash

gencsv(){
    x=0;for i in $(shuf -i 10-999 -n 10); do echo "${x}, ${i}"; (( x = x+1 )); done
}

gencsv > inputFile 
