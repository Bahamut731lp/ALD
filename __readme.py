"""
    Skript pro generování tabulky s výsledky v README.md
"""
import sys
import os
import pytest
from tabulate import tabulate
from pylint.lint import Run

FILES = ["hello_world.py", "answer_is_42.py", "palindrome.py", "palindrome_number.py", "lifo.py", "fifo.py", "unique_numbers.py", "word_count.py", "gps.py", "regex.py"]

# Disable


def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore


def enablePrint():
    sys.stdout = sys.__stdout__


def process_file(filename):
    #blockPrint()
    pylint_results = Run([filename], do_exit=False)
    pytest_result = pytest.main(["-x", f"test_{filename}"])

    if pytest_result == 0:
        pytest_result = "✔️"
    else:
        pytest_result = "❌"

    return [filename, pytest_result, pylint_results.linter.stats.global_note]


if __name__ == "__main__":
    results = [process_file(file) for file in FILES]
    headers = ["Soubor", "Prochází testy", "Pylint skóre"]
    table = tabulate(results, tablefmt="html", headers=headers,
                     colalign=["right", "center", "center"])

    with open("./README.md", "w+", encoding="utf-8") as file_handle:
        content = file_handle.read()
        start = content.find("<table>")
        end = content.rfind("</table>")
        content = content[:start] + table + content[end+1:]
        
        file_handle.write(table)
