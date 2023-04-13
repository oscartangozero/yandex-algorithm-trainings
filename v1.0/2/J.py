def frequency_range(f_min, f_max, f_base, records) -> tuple[float, float]:
    for f, indication in records:
        if f != f_base:
            f_mid = (f_base + f) / 2
            if (f_base < f and indication == 'closer') or \
                    (f < f_base and indication == 'further'):
                f_min = max(f_min, f_mid)
            else:
                f_max = min(f_mid, f_max)
        f_base = f
    return f_min, f_max


n = int(input())
f0 = float(input())
records = []
for _ in range(n-1):
    frequency, indication = input().split()
    records.append((float(frequency), indication))
print(*frequency_range(30, 4000, f0, records))
