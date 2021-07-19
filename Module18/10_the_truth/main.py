input_text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -./\'(,*+!\""

list_input_text = input_text.split(' ')
cesar_crypt_shift = 1
shift_word = -3

for word in list_input_text:
    decrypt_word = ''
    for symbol in word:
        decrypt_word += letters[letters.index(symbol) - cesar_crypt_shift]
    if len(decrypt_word) >= abs(shift_word):
        print(decrypt_word[shift_word:] + decrypt_word[:shift_word], end=' ')
    else:
        print(decrypt_word[shift_word % len(decrypt_word):] + decrypt_word[:shift_word % len(decrypt_word)], end=' ')

    if '.' in decrypt_word:
        shift_word -= 1
        print()


# Для вывода Дзена Python также можно использовать
# import this
