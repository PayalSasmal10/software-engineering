def create_gene(n):
    for i in range(3):
        yield i

a = create_gene(5)
for j in a:
    print(j)

