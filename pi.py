text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
textlist = text.replace(",","").replace(".","").replace("    ","").replace("\n"," ").replace(",","").strip().split(" ")
numList = list(map(len, textlist))
strList = list(map(str, numList))
print("".join(strList))