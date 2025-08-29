sample_space_of_dice = 6

event = {5}

outcomes = len(event)

P = outcomes / sample_space_of_dice

print(P)


data = {
    'always' : 1054,
    'often' : 613,
    'sometimes' : 417,
    'rarely' : 196,
    'never' : 171
}


total_frekuensi = sum(data.values())

print(total_frekuensi)

always = data['always']

P_ALWAYS = always / total_frekuensi

print(P_ALWAYS)