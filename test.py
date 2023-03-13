import sys

lines = set()

total = 0
n = int(sys.argv[1])
print(n)

for line in sys.stdin:
    lines.add(line)
    total += 1
    print(lines)
    if len(lines) == n:
        print(f"{n} distinct lines after {total} lines read")
        sys.exit()