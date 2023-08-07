"""
    Skript pro úlohu 12 z ALD
    @author matej.hampl
    @refactor kevin.danek
"""
import re

def format_student(data, fields, i):
    """Funkce pro formátování řádku se studentem

    Args:
        data (dict): Slovník s daty studentů
        fields (dict): Slonvník s obory
        i (int): index

    Returns:
        str: Naformátovaný řetězec
    """
    obor = data["obor"][i]
    index = f'{len(fields[obor]) + 1:>2}:'
    sex = f'{data["OC"][i][0]}'
    name = f'{data["jmeno"][i]:<18}'
    field = f'{data["obor"][i]:<3}'
    personal_number = f'{data["OC"][i][1:]}'

    return " ".join([index, sex, name, field, personal_number])

def main():
    """
        Funkce realizující program
    """
    lines = []

    with open("./vstup.html", "r", encoding="utf-8") as file_handle:
        lines = file_handle.readlines()

    result = []

    data = {
        "OC": [],
        "jmeno": [],
        "prijmeni": [],
        "krestni": [],
        "obor": []
    }

    fields = {
        "AI": [],
        "AVI": [],
        "IS": [],
        "IT": []
    }

    for line in lines:
        if re.search(r"\s[A-Z]\d", line):  # Osobni cisla
            line = line.lstrip(' ')
            data["OC"].append(line[:9])

        if re.search(r"AVI|AI|IS|IT", line, ):  # Obor
            line = line.lstrip(' ')
            line = re.findall(r'\>(.[A-Z]+)\<', line)
            for match in line:
                data["obor"].append(match)

        if re.search(r"([A-Z])\w+\n", str(line)):  # Jmena
            line = line.lstrip(' ')
            line = line.strip()
            data["jmeno"].append(line)

    data["obor"].pop(0)  # vykopnout "ISP"
    data["jmeno"] = [i for i in data["jmeno"] if i != "Ne"]  # vykopnout "Ne"

    for prij in data["jmeno"][0::5]:
        data["prijmeni"].append(prij)
    data["prijmeni"] = [x.upper() for x in data["prijmeni"]]

    for kres in data["jmeno"][1::5]:
        data["krestni"].append(kres)
    sort_oc = data["OC"]
    sort_oc = [sub[1:] for sub in sort_oc]  # odebrat pismeno
    sort_oc, data["OC"], data["prijmeni"], data["krestni"], data["obor"] = zip(
        *sorted(
            zip(
                sort_oc,
                data["OC"],
                data["prijmeni"],
                data["krestni"],
                data["obor"]
            ),
            key = lambda x: (not int(x[0]) % 2, x)
        )
    )

    data["jmeno"].clear()

    for jmeno in range(len(data["krestni"])):
        data["jmeno"].append(f'{data["prijmeni"][jmeno]} {data["krestni"][jmeno]}')

    for i in range(len(data["obor"])):
        fields[data["obor"][i]].append(format_student(data, fields, i))

    for obor, studenti in fields.items():
        result.append(f"{obor}:")
        result.append("\n".join(studenti).rstrip())

    return "\n".join(result).strip()

if __name__ == "__main__":
    print(main())
