#!/usr/bin/env bash

# pre-commit hook

# install by running the following command in repository root:
#   ln -s "$(pwd)/.github/hooks/pre-commit.sh" "$(pwd)/.git/hooks/pre-commit"

export PYTHONPATH=$PYTHONPATH:$(pwd)/src/
python3 -m resumake.builder -h >./src/resources/usage.txt
README_CHANGED=$(git diff ./src/resources/usage.txt | grep txt | head -n 1)
UPDATE=$(python3 -c "print(str('${README_CHANGED}'.endswith('usage.txt')).lower())")
if [[ $UPDATE == "true" ]]; then
    echo "Updating README usage text..."
    git add ./src/resources/usage.txt
    cat ./src/resources/readme-p1.md ./src/resources/usage.txt ./src/resources/readme-p2.md >README.md
    git add README.md
    echo "README usage text updated."
else
    echo "README usage text unchanged."
fi
