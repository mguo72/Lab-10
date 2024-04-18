#D: Fabric Class
class Fabric:
    def __init__(words, countryOfOrigin, color):
        words.countryOfOrigin = countryOfOrigin
        words.color = color

    def __str__(words):
        return words.countryOfOrigin + "("+ str(words.color)+ ")"

c1 = Fabric("United States", "blue")        #Makes F in Caps for Fabric

print(c1)
