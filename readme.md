# md_numbers

md_numbers is a simple python script that creates a number hierarchy for your markdown headlines.

## 1 Usage

> python md_numbers.py test.md

- tested with python 2.7 and python 3.8
- there shouldn't be any compatibility problem

## 2 Issues

- There are no security checks if the file is really a markdown file
- The file gets overwritten by the script, so make sure to make a copy beforehand
- Numbers at the beginning of a headline will get removed
- Headlines like "1headline" will be recognized as number and removed as well
