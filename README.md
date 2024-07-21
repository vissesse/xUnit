RUN
find . -name "*.py" | entr -r python3 -m unittest discover