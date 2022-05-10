import argparse

from vistrings.strings import get_vi_plaintext

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", action="store")
    options = parser.parse_args()
    print(get_vi_plaintext(options.file))


if __name__ == "__main__":
    main()
