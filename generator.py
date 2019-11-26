from random import choice
from copy import deepcopy

dictionary = {
    'verbs': ('galloping crying enlightening darkening fly rise reflects ' +
              'climb burn redeem power guide standing blazing reaching ' +
              'searching').split(),
    'adverbs': ('triumphantly quickly eternally brightly vengefully ' +
                'courageously defiantly gracefully solemnly viciously ' +
                'sorrowfully bravely mysteriously violently frantically ' +
                'wildly').split(),
    'prepositions': ('through into above beneath beyond amongst below under ' +
                     'in against within inside before outside').split(),
    'adjectives': ('snowy shining glowing ancient rising crystal ' +
                   'fantastical soulful aggresive courageous defiant bloody ' +
                   'cloudy graceful misty icy').split(),
    'nouns': ('moonlight darkness defendors wings light fields destiny sun ' +
              'heavens souls sunlight battle cry night skies dream clouds ' +
              'path ice mountain plains hearts stars fire lands abyss').split()
}



def generate_title():

    title = ''

    nouns = deepcopy(dictionary['nouns'])
    adjectives = deepcopy(dictionary['adjectives'])
    of_nouns = ('moonlight darkness light destiny sun night skies dream ' +
                'ice stars fire abyss').split()

    mode = choice(['two_adj', 'two_nouns'])

    if mode == 'two_adj':
        title = '{} {} {}'.format(choice(adjectives),
                                  choice(adjectives),
                                  choice(nouns)).capitalize()
    else:
        title = '{} {} of {}'.format(choice(adjectives),
                                     choice(nouns),
                                     choice(of_nouns)).capitalize()

    return title + '\n'



def generate_song():

    song = ''

    verbs = deepcopy(dictionary['verbs'])
    adverbs = deepcopy(dictionary['adverbs'])
    prepositions = deepcopy(dictionary['prepositions'])
    adjectives = deepcopy(dictionary['adjectives'])
    nouns = ['moonlight light sunlight night path'.split(),
             ('darkness heavens hearts stars ladns abyss defendors wings ' +
              'fields souls clouds plains').split(),
             'destiny battle sun dream mountain'.split(),
             'fire skies cry ice'.split()]


    def generate_chorus():

        chorus = ''
        gnouns = choice(nouns)

        for i in range(2):
            chorus += '{} {} {} {} {} {} {}\n'.format(choice(adjectives),
                                                      choice(gnouns),
                                                      choice(verbs),
                                                      choice(adverbs),
                                                      choice(prepositions),
                                                      choice(adjectives),
                                                      choice(gnouns)).capitalize()
        chorus += '{} {} {}'.format(choice(prepositions),
                                    choice(adjectives),
                                    choice(choice(nouns))).capitalize()
        return chorus + '\n'


    def generate_verse():

        verse = ''
        first_gnouns = choice(nouns)
        second_gnouns = choice(nouns)

        for i in range(2):
            verse += '{} {} {} {} {}\n'.format(choice(verbs),
                                               choice(adverbs),
                                               choice(prepositions),
                                               choice(adjectives),
                                               choice(first_gnouns)).capitalize()

            verse += '{} {} {} {} {}\n'.format(choice(verbs),
                                               choice(adverbs),
                                               choice(prepositions),
                                               choice(adjectives),
                                               choice(second_gnouns)).capitalize()

        return verse + '\n'

    chorus = generate_chorus()
    song = '{}\n{}{}{}\n{}{}{}'.format(generate_title(), generate_verse(),
                                       generate_verse(), chorus, generate_verse(),
                                       generate_verse(), chorus)

    return song + '\n'


def generate_album():

    album = generate_title() + '\n\n'

    for i in range(6):
        album += generate_song() + '\n\n'

    return album
