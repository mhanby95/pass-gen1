def Swap_Case(xyz):
    str_value = ""
    for word in xyz:
        if word.isupper():
            str_value += word.lower()
        else:
            str_value += word.upper()
    return str_value

print(Swap_Case('HElLO'))
print(Swap_Case('heLlo'))

