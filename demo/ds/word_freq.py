st = "An old man lived in the village He was one of the most unfortunate people in the world. The whole village was tired of him he was always gloomy he constantly complained and was always in a bad mood"

words = st.split(' ')
# print(words)

uwords = set(words)
for w in sorted(uwords):
    print(f"{w:15}  {words.count(w):3}")
