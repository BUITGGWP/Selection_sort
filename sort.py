def itc_selection_sort(sp):
    for i in range(len(sp)):
        lowest_el = i
        for j in range(i + 1, len(sp)):
            if sp[j] < sp[lowest_el]:
                lowest_el = j
        sp[i], sp[lowest_el] = sp[lowest_el], sp[i]
        print(*sp)
    return sp


spisok = list(map(int, input().split()))
itc_selection_sort(spisok)
