a, b, x, y, z = [int(d) for d in input().split()]

if (
        y<b and z<a or
        x<b and z<a or
        y<b and x<a or
        x<b and y<a or
        y<a and z<b or
        x<a and z<b or
        x<a and y<b
):
    print("1")

else:
    print("0")

