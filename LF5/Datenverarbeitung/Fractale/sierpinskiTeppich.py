def incarpet(x, y):
    while x != 0 and y != 0:
        if x % 3 == 1 and y % 3 == 1:
            return "black"
        x /= 3
        y /= 3
    return "white"


def main(stufe):
    stufe = int(stufe)
    canvasesize = 180
    header = "<?xml version=\"1.0\"?>\n<svg xmlns=\"http://www.w3.org/2000/svg\">\n"
    footer = "</svg>"

    filename = "output/Sierpinksi_Teppich_Stufe_" + str(stufe) + ".svg"
    file = open(filename, "w+")
    file.write(header)

    k = 0
    while k <= stufe:
        fieldsize = canvasesize / pow(3, k)
        i = 0
        while i < pow(3, k):
            j = 0
            while j < pow(3, k):
                color = incarpet(i, j)
                if color == "black":
                    line = "    <rect x=\"" + str(fieldsize * i) + "\" y=\"" + str(fieldsize * j) + "\" width=\"" + str(
                        fieldsize) + "\" height=\"" + str(fieldsize) + "\" fill=\"" + color + "\"/>\n"
                    file.write(line)
                j += 1
            i += 1
        k += 1
    file.write(footer)
    file.close()
    print("Sierpinksi_Teppich_Stufe_" + str(stufe) + ".svg generiert!")
