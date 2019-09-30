class Codec:
    
    def __init__(self):
        self.urls = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        encoded_string = self.randomStringwithDigitsAndSymbols(len(longUrl.rsplit('/', 1)[-1]))
        self.urls[encoded_string] = longUrl
        return 'http://tinyurl.com/'+ encoded_string

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urls[shortUrl.rsplit('/', 1)[-1]]
        
    def randomStringwithDigitsAndSymbols(self, l):
        """Generate a random string of letters, digits and special characters."""
        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(l))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
