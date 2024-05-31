import sys
import json

disk_svg_path = sys.argv[1]
config_path = sys.argv[2]


with open(config_path) as file:
    config = json.load(file)

with open(disk_svg_path) as file:
    svg = file.read()

lines = config["program_text"]["envelope_lines"]


def get_line(line_num):
    if line_num < len(lines):
        return lines[line_num]
    else:
        return ""


for i in range(4):
    svg = svg.replace(
        f"line_mark_{i+1}___________________",
        lines[i] if i < len(lines) else "",
    )

svg = svg.replace(
    "line_mark_6___________________",
    f"ДП.{config['student']['groupName']}{config['student']['groupNumber']}.{config['student']['card']}-{config['number']} 12 {config['version']}",
)

print(svg)
