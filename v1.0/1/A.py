def will_work(mode: str, t1: int, t2: int) -> bool:
    return mode == 'auto' or (mode == 'freeze' and t2 < t1) \
        or (mode == 'heat' and t2 > t1)


t_room, t_cond = map(int, input().split())
mode = input()
print(t_cond if will_work(mode, t_room, t_cond) else t_room)
