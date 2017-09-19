import webbrowser


class Movie():
    """The media.py is the file that defines
    Movie class
    """
    def __init__(self, movie_title, movie_storyline,
                 movie_image, movie_trailer):  # constructor
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer
    """ The show_triailer function in Movie opens
    the url in browser
    """
    def show_trailer(self):
        webbrowser.open(self.trialer_youtube_url)
        
    
