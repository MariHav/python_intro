favourite_languages = {
    'serik': ['js','type script','node.js'],
    'mariana': ['sql','python'],
    'olena': ['c#','js']
}

for name, languages in favourite_languages.items():
    print(f'\n{name.title()}\'s favourite languages are:')
    for language in languages:
        print(f'\t{language}')