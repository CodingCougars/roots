class Artifact:

    def __init__(self, name, type, media, comments, hashtags):

        self.name = name
        self.type = type
        self.media = media
        self.comments = comments
        self.hashtags = hashtags

    def getName(self):

        return self.name
    
    def getType(self):

        return self.type

    def getMedia(self):

        return self.media

    def getComments(self):

        return self.comments
    
    def getHashtags(self):

        return self.hashtags