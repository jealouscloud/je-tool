#!/usr/bin/python3
# json.py
# Generate json using command line arguments.
# It accepts either list or dictionary (object) mode
# It will attempt to auto detect, but you can be explicit by specifying
# -l | --list or -a | --array for list mode
# -d | --dict or -o | --object for object mode
import sys
import json
import re


def parse_object(object_str):
    # Attempt to parse an object as json, else literal
    try:
        return json.loads(object_str)
    except:
        pass
    return object_str


def print_help():
    print(
        f"Usage: {sys.argv[0]} [-l|-d] [value1] [value2] ... \n"
        "Generate json using command line arguments. \n"
        "It accepts either list or dictionary (object) mode \n"
        "It will attempt to auto detect, but you can be explicit by specifying \n"
        "-l | --list or -a | --array for list mode \n"
        "-d | --dict or -o | --object for object mode \n"
    )
    sys.exit(0)


def main():
    values = []
    force_array = False
    force_object = False
    ignore_flags = False
    if len(sys.argv) == 1:
        print_help()

    # Dependency free quick and dirty argument parsing
    for arg in sys.argv[1:]:
        if ignore_flags:
            values.append(arg)
            continue
        if arg in ("-h", "--help"):
            print_help()
        if arg == "--":
            ignore_flags = True
            continue
        elif arg in ("-l", "--list", "-a", "--array"):
            if not force_object:
                force_array = True
        elif arg in ("-d", "--dict", "-o", "--object"):
            if not force_array:
                force_object = True
        else:
            values.append(arg)

    dict_result = {}
    array_result = []
    object_mode = force_object or False
    array_mode = force_array or False
    for val in values:
        if object_mode or (re.search(r"^[\w]+=", val) and not array_mode):
            object_mode = True
            partitioned = val.partition("=")
            dict_result[partitioned[0]] = parse_object(partitioned[2])
        else:
            array_mode = True
            array_result.append(parse_object(val))

    print(json.dumps(dict_result if dict_result else array_result))


if __name__ == "__main__":
    main()
