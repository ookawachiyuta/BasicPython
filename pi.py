text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
textlist = text.replace(",","").replace(".","").replace("    ","").replace("\n"," ").replace(",","").strip().split(" ")
numList = tuple(map(len, textlist))
answer = str(numList[0])
answer += str(numList[1])
answer += str(numList[2])
answer += str(numList[3])
answer += str(numList[4])
answer += str(numList[5])
answer += str(numList[6])
answer += str(numList[7])
answer += str(numList[8])
answer += str(numList[9])
answer += str(numList[10])
answer += str(numList[11])
answer += str(numList[12])
answer += str(numList[13])
answer += str(numList[14])
answer += str(numList[15])
answer += str(numList[16])
answer += str(numList[17])
answer += str(numList[18])
answer += str(numList[19])
answer += str(numList[20])
answer += str(numList[21])
answer += str(numList[22])
answer += str(numList[23])
print(answer)