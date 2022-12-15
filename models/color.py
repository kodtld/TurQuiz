class Color:
    def __init__(self,name,code,shade):
        self.name = name
        self.code = code
        self.shade = shade

colors = [
        Color("Mellow Apricot","#FFC685","light"),
        Color("Beau Blue", "#BAD7F2", "light"),
        Color("Pink Lavender", "#E0B1CB","light"),
        Color("Mindaro", "#DDFF99", "light"),
        #Color("Lilac", "#C6A4CC","light"),
        #Color("Pink Lace", "#F4CDEA", "light"),
        #Color("Nadeshiko Pink", "#EEAABF", "light"),
        #Color("Mauvelous","#EB98A5","light")
            ]

title_colors = [Color("Dark Cyan","#2A8D88","dark"), Color("Medium Turquoise","#52CBC5","light")]

rank_colors = [
        Color("Bronze","#6E3D02","light"),
        Color("Silver", "#303030", "light"),
        Color("Gold", "#B79101","light"),
        Color("Platinum", "#094A73", "light"),
        Color("Diamond", "#0F347A", "light"),
        Color("Champion", "#5C30A3","light"),
        Color("Grand Champion", "#910725", "light"),
        Color("Demi God", "#3F003D", "light")
]