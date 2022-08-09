sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}
while True:
    eng_input = input('Enter a word in English or EXIT: ')
    if eng_input in sample_dict:
        print('Translation: ', sample_dict[eng_input])
        continue
    elif eng_input == 'EXIT':
        print('Bye!')
        break
    else:
        print('No match!')
        continue

