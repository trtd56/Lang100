Text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

word_list = Text.split()

print([len(w.strip(",.")) for w in word_list])
