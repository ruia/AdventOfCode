with open("input.txt") as f:
    cur_cal = 0
    max_top_3 = 0
    cals = []

    input = f.readlines()
    last = input[-1].strip()

    for line in input:
        line = line.strip()

        if (line != ""):
            cur_cal += int(line)
        else:
            cals.append(cur_cal)
            cur_cal = 0

        if (line == last):
            cals.append(cur_cal)
        
    for i in sorted(cals,reverse=True)[:3]:
        max_top_3 += i

    print(f"Top 1:  {sorted(cals,reverse=True)[:1][0]}")
    print(f"Top 3:  {max_top_3}")
