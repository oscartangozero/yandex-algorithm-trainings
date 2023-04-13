N = int(input())
languages = [[input() for _ in range(int(input()))] for _ in range(N)]
shared, all = (set(languages[0]).intersection(*languages[1:]),
               set().union(*languages))
for items in (shared, all):
    print(len(items), *items, sep='\n')
