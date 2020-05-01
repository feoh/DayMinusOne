import argparse
import json
from time import strptime, strftime


def add_args():
    parser = argparse.ArgumentParser(description='Convert DayOne JSON export file to Markdown')
    parser.add_argument('dayone_json_file',
                        help='DayOne journal exported JSON file to convert to a markdown directory')
    return parser.parse_args()


if __name__ == '__main__':
    args = add_args()

    with open(args.dayone_json_file, 'r') as day1jf:
        day1j = json.load(day1jf)

    entries = day1j['entries']
    for entry in entries:
        if "text" not in entry.keys():
            continue
        create_ts =  strptime(entry['creationDate'], "%Y-%m-%dT%H:%M:%SZ")
        readable_create_ts = strftime("%A, %B %d, %Y %I:%M:%S", create_ts)
        filename = f"{readable_create_ts}.md"
        with open(filename,'w') as entry_file:
            body = f"Date: {readable_create_ts}\n"
            if "tags" in entry.keys():
                body += "Tags: "
                body += ", ".join(entry['tags'])
                body += "\n\n"
            else:
                body += "\n"
            body += entry['text']
            entry_file.write(body)
