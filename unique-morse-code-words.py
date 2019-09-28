        morse = {'a':".-",
                 'b':"-...",
                 'c':"-.-.",
                 'd':"-..",
                 'e':".",
                 'f':"..-.",
                 'g':"--.",
                 'h':"....",
                 'i':"..",
                 'j':".---",
                 'k':"-.-",
                 'l':".-..",
                 'm':"--",
                 'n':"-.",
                 'o':"---",
                 'p':".--.",
                 'q':"--.-",
                 'r':".-.",
                 's':"...",
                 't':"-",
                 'u':"..-",
                 'v':"...-",
                 'w':".--",
                 'x':"-..-",
                 'y':"-.--",
                 'z':"--.."}
        
        transformations = set()
        for word in words:
            transformation = ''
            for c in word:
                transformation += morse[c]
            transformations.add(transformation)
            
        return len(transformations)
