import inflect

p = inflect.engine()
array = []
while True:
    try:
        array.append(input())
    except EOFError:
        break

output = p.join(array)
print(f"Adieu, adieu, to {output}")
