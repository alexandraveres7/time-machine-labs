capitals = {
    'Timis': 'Timisoara',
    'Bihor': 'Oradea',
    'Arad': 'Arad',
    'Hunedoara': 'Deva',
    'Caras-Severin': 'Resita',
}


def capitals_reverse(capital):
    inverted = {value: key for key, value in capitals.items()}
    print('judet(', capital, ')', '\n', inverted.get(capital))


capitals_reverse('Timisoara')
