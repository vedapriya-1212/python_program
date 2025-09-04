def notes(amount):
    denominations = [500, 100, 50, 20, 10]
    note_count = {}
    c=0
    for denom in denominations:
        if amount >= denom:
            count = amount // denom
            c+=count
            note_count[denom] = count
            amount=amount % denom
    return note_count, "Total notes:",c
print(notes(1000))
print(notes(1100))
print(notes(2280))
print(notes(2560))