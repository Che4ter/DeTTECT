import sys

from generic import *


def main():
    n = len(sys.argv)

    if n < 2:
        return

    filename = sys.argv[1]
    ucid = None

    if n > 2:
        ucid = sys.argv[2]

    list_usecases(filename, ucid)


def list_usecases(filename, uc_id=None):
    """
    Parses all detection locations from technique files
    :param filename: the filename of the YAML file containing the techniques administration
    :param uc_id: use case id or name to filter for
    """
    my_techniques, name, platform = load_techniques(filename)
    my_techniques = dict(sorted(my_techniques.items(), key=lambda kv: kv[0], reverse=False))

    uc_list = {}
    for technique in my_techniques.items():
        for item in technique[1]['detection']:
            for uc in item['location']:
                if uc_id is None or uc_id in uc:
                    if uc not in uc_list:
                        uc_list[uc] = []
                    uc_list[uc].append(technique[0])
    uc_list = dict(sorted(uc_list.items()))
    uc_pretty_print(uc_list)


def uc_pretty_print(uc_list):
    """
    Pretty prints use case lists and techniques
    :param uc_list: uc list
    """
    for uc in uc_list.items():
        print(uc[0])

        techniques = uc[1]
        techniques.sort()
        for technique in techniques:
            print(" - " + technique)


if __name__ == "__main__":
    main()
