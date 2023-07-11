"""
    Skript pro úlohu 7 z ALD
    @author matej.hampl
    @refactor kevin.danek
"""
import sys
import collections

def main(lines):
    """
    Vstupní bod programu
    """

    lines = [ line.split(",") for line in lines ]
    flat_list = [item for sublist in lines for item in sublist]
    flat_list = list(map(lambda x: x.strip(), flat_list))
    occurences = collections.Counter(flat_list).items()

    uniq = [x for n, x in enumerate(flat_list) if x not in flat_list[:n]]
    uniques = ",".join(uniq)

    dupes = [item for item, count in occurences if count > 1]
    duplicates = ",".join(dupes)

    single = dupes = [item for item, count in occurences if count == 1]
    singles = ",".join(single)

    return "\n".join([
        f"all: {uniques}",
        f">1x: {duplicates}",
        f"=1x: {singles}"
    ])

if __name__ == "__main__":
    contents = []
    for line in sys.stdin:
        contents.append(line)
        if line == "\n":
            break

    print(main(contents))
