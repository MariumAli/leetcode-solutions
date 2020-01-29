def groupIsomorphic(strs):
    def encode(s):
        d = {}
        encoded = []
        for c in s:
            if c not in d:
                d[c] = len(d)
            encoded.append(d[c])
        print('encoded: ' + s)
        print(encoded)
        return str(encoded)

    groups = {}
    for s in strs:
        encoded = encode(s)
        if encoded not in groups:
            groups[encoded] = []
        groups[encoded].append(s)
        print(groups)

    return list(groups.values())

print(groupIsomorphic(['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']))