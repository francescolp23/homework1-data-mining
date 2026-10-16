cd ~/Desktop/homework1-data-mining
cat > README.md <<'EOF'
# Homework 1 - Algorithmic Methods of Data Mining

This is my repo for homework 1 of the data mining course. All the exercises are python challenges from HackerRank, I did them last year so the submissions are from my profile.

## What's inside

- `scripts.py` : the code of my solutions, one block for each challenge. They are in the order of the homework (problem 1 first, then problem 2). The code is the same I submitted on HackerRank, so some of them read from input() and wont run alone
- `printouts/` : pdf with the screenshots of my accepted submissions

## Notes

- Problem 1 covers intro, data types, strings, sets, collections, date and time, exceptions, built-ins, map and lambda, regex, xml, closures and decorators and numpy
- Problem 2 is the six algorithm challenges (birthday cake candles, kangaroo, strange advertising, recursive digit sum and the two insertion sorts)
- The Tuples challenge is not included, I only had it accepted in python 2 so I left it out

Francesco La Piana
EOF
git add README.md
git commit -m "update readme"
git push
