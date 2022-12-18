"""
Defines quote and quotes used by the application
"""

class Quote:
    """
    Defines quote and quotes used by the application
    """

    def __init__(self,content,author):
        self.content = content
        self.author = author

quotes = [
    Quote("It is what we know already that often prevents us from learning.",
        "Claude Bernard"),
    Quote("Tell me and I forget. Teach me and I remember. Involve me and I learn.",
        "Benjamin Franklin"),
    Quote("Question everything. Learn something. Answer nothing.",
        "Euripides"),
    Quote("I am always ready to learn although I do not always like being taught.",
        "Winston Churchill"),
    Quote("The first problem for all of us, men and women, is not to learn, but to unlearn.",
        "Gloria Steinem"),
    Quote("I am always doing that which I cannot do, in order that I may learn how to do it.",
        "Pablo Picasso")
    ]
