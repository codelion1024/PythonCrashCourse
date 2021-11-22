# 字典中嵌套列表
fav_languages = {
  'jen' : ['python', 'ruby'],
  'sara' : ['c'],
  'edward' : ['ruby', 'go'],
  'phil' : ['python', 'haskell'],
  }

for name, languages in fav_languages.items():
  print(f"\n{name.title()}'s favorite languages are:")
  for language in languages:
    print(f"\t{language.title()}")

