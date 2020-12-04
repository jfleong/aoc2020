def read_file(path="input.txt"):
    with open(path) as f:
        return f.read().splitlines()
