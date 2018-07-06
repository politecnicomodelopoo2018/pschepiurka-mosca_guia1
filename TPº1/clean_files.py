lines = []
with open('carga_json.py', 'r') as f:
    for line in f:
        line = line.replace('\t', '    ')
        lines.append(line)

with open('carga_json.py', 'w') as f:
    f.writelines(lines)