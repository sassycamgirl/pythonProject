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
    print('Your answer is: ', eng_input, '\n'
          'What your expecting: ', sample_dict['mouth'])
    if eng_input == sample_dict:
        print('this test: ', eng_input)
        break
    elif eng_input == 'EXIT':
        print('Bye!')
        break



"""
if the_input = sample_dict
    print(sample_dict.value)
    else
        print('Bye!'


"""