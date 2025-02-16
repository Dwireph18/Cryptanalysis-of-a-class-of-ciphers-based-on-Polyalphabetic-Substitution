import sys

# plaintext dictionary
PLAINTEXTS = [
    "unconquerable tropical pythagoras rebukingly price ephedra barmiest hastes spades fevers cause wisped overdecorates linked smitten trickle scanning cognize oaken casework significate influenceable precontrived clockers defalcation fruitless splintery kids placidness regenerate harebrained liberalism neuronic clavierist attendees matinees prospectively bubbies longitudinal raving relaxants rigged oxygens chronologist briniest tweezes profaning abeyances fixity gulls coquetted budgerigar drooled unassertive shelter subsoiling surmounted frostlike jobbed hobnailed fulfilling jaywalking testabilit",
    "protectorates committeemen refractory narcissus bridlers weathercocks occluding orchectomy syncoms denunciation chronaxy imperilment incurred defrosted beamy opticopupillary acculturation scouting curiousest tosh preconscious weekday reich saddler politicize mercerizes saucepan bifold chit reviewable easiness brazed essentially idler dependable predicable locales rededicated cowbird kvetched confusingly airdrops dreggier privileges tempter anaerobes glistened sartorial distrustfulness papillary ughs proctoring duplexed pitas traitorously unlighted cryptographer odysseys metamer either meliorat",
    "incomes shoes porcine pursue blabbered irritable ballets grabbed scything oscillogram despots pharynxes recompensive disarraying ghoulish mariachi wickerwork orientation candidnesses nets opalescing friending wining cypher headstrong insubmissive oceanid bowlegs voider recook parochial trop gravidly vomiting hurray friended uncontestable situate fen cyclecars gads macrocosms dhyana overruns impolite europe cynical jennet tumor noddy canted clarion opiner incurring knobbed planeload megohm dejecting campily dedicational invaluable praecoces coalescence dibbuk bustles flay acuities centimeters l",
    "rejoicing nectar asker dreadfuls kidnappers interstate incrusting quintessential neglecter brewage phosphatic angle obliquely bean walkup outflowed squib tightwads trenched pipe extents streakier frowning phantasmagories supinates imbibers inactivates tingly deserter steerages beggared pulsator laity salvageable bestrode interning stodgily cracker excisions quanted arranges poultries sleds shortly packages apparat fledge alderwomen halvah verdi ineffectualness entrenches franchising merchantability trisaccharide limekiln sportsmanship lassitudes recidivistic locating iou wardress estrus potboi",
    "headmaster attractant subjugator peddlery vigil dogfights pixyish comforts aretes felinities copycat salerooms schmeering institutor hairlocks speeder composers dramatics eyeholes progressives reminiscent hermaphrodism simultaneous spondaics hayfork armory refashioning battering darning tapper pancaked unaffected televiewer mussiness pollbook sieved reclines restamp cohosh excludes homelier coacts refashioned loiterer prospectively encouragers biggest pasters modernity governorships crusted buttoned wallpapered enamors supervisal nervily groaning disembody communion embosoming tattles pancakes"
]

def char_freq(input):
    """
    Calculate the frequency of each character in a given text.
    """
    freq = {}
    for char in input: 
        if char in freq:
            freq[char] += 1 # increase frequency each time char is read
        else:
            freq[char] = 1 # if first time char is read, freq=1
    total_chars = sum(freq.values()) # len of input
    for char in freq: 
        freq[char] /= total_chars # divide num of char appearances by total chars
    return freq 


def get_coincidence(input):
    """
    calculate Index of Coincidence (IoC) for input.
    (IoC estimates likelihood that two randomly selected characters from input are the same)
    """
    input_len = len(input)
    frequencies = char_freq(input)
    coincidence = sum(f * (f - 1) for f in frequencies.values()) / (input_len * (input_len - 1)) 
    # IoC calculation from Google
    return coincidence


def get_avg_coincidence(ciphertext, key_length_guess):
    """
    calculate average IoC across segments created by estimated key len.
    analyzes the similarity of character distribution to get a better key len estimate.
    """
    segments = ['' for _ in range(key_length_guess)] # list of emptry strings to hold segments of ciphertext thought
    # to be encrypted with dif parts of key (each string is each possible position in key)
    for i, char in enumerate(ciphertext):
        segments[i % key_length_guess] += char # for each character, determines segment the character belongs in 
        # based on the guessed key length
    return sum(get_coincidence(segment) for segment in segments) / len(segments) # avg = total coincidence/num segments


def get_key_len(ciphertext):
    """
    Estimate the key length used in the encryption by comparing the average IoC for various key lengths
    to the IoC expected in regular English text. The key length that produces an IoC closest to that
    of English text is likely to be the correct key length.
    """
    typical_ioc = 1.73 # typical IoC for english text, from Google
    min_dif = float('inf') # set min difference between IoC of dif segments to large value so it gets updates immediately
    key_len_guess = 1 # holds best guess for key len, gets updated
    for curr_key_len in range(1, 21):  # key is len 1-20 as stated in directions
        avg_ioc = get_avg_coincidence(ciphertext, curr_key_len)
        dif = abs(avg_ioc - typical_ioc) # absolute dif btwn calculated avg IoC for the curr key len and typical IoC
        if dif < min_dif:
            min_dif = dif # update min dif if needed
            key_len_guess = curr_key_len # update key len guess if needed
    return key_len_guess


def decrypt_segment(segment):
    """
    decrypts segment using most common letters in english, applying the statistical probability of each character's
    appeearance to decrypt the message
    """
    segment_freq = char_freq(segment)  # calculate frequency excluding outliers
    most_frequent = max(segment_freq, key=segment_freq.get) # find char w highest freq in that segment
    shift = (ord(most_frequent) - ord('e')) % 26 # assumes 'e' is most common, calculates shift amount

    decrypted = ""
    for char in segment:
        if char.isalpha():
            shifted = ord(char) - shift # ASCII val of shifted char-- subtracts prev shift from ASCII value of curr char
            if shifted < ord('a'): # adjusts for wrap around in alphabet
                shifted += 26
            decrypted += chr(shifted) # convert shifted ASCII back to char
        else:
            decrypted += char
    return decrypted


def reassemble(decrypted_segments):
    """
    joins decrypted segments back together
    """
    plaintext = ''.join([''.join(segment) for segment in zip(*decrypted_segments)])
    return plaintext


def decrypt_polyalphabetic(ciphertext):
    """
    decrypt input ciphertext by estimating the key length, individually decrypting segments, and reassembling
    """
    key_len = get_key_len(ciphertext)
    segments = [ciphertext[i::key_len] for i in range(key_len)]
    decrypted_segments = []

    for segment in segments:
        # adjust the decryption to account for potential random chars
        decrypted_segment = decrypt_segment(segment)
        decrypted_segments.append(decrypted_segment)

    # reassemble the plaintext, considering the possibility of random chars
    plaintext = reassemble(decrypted_segments)
    return plaintext



def calculate_similarity_score(decrypted_text, candidate_text):
    # get char frequency for potential candidate plaintext and for the decrypted ciphertext
    decrypted_freq = char_freq(decrypted_text)
    candidate_freq = char_freq(candidate_text)

    # get basic similarity score based on frequency distribution
    score = sum(min(decrypted_freq[char], candidate_freq.get(char, 0)) for char in decrypted_freq)
    # similarity score from Google

    # consider structural similarity
    decrypted_words = decrypted_text.split()
    candidate_words = candidate_text.split()
    # similarity based on the total word count and the presence of similarly long words
    score += min(len(decrypted_words), len(candidate_words)) / max(len(decrypted_words), len(candidate_words))
    long_words_decrypted = [word for word in decrypted_words if len(word) > 5]
    long_words_candidate = [word for word in candidate_words if len(word) > 5]
    score += sum(1 for word in long_words_decrypted if word in long_words_candidate) / (len(long_words_decrypted) + 1)

    return score

def find_best_match(decrypted_text):
    """
    finds best matching candidate plaintext to decrypted ciphertext
    """
    best_match_index = None
    best_match_score = 0
    
    for index, candidate in enumerate(PLAINTEXTS):
        score = calculate_similarity_score(decrypted_text, candidate)
        if score > best_match_score:
            best_match_score = score
            best_match_index = index + 1

    return best_match_index


def main():
    print("Enter the ciphertext:", end=" ")
    ciphertext = input().strip()
    decrypted_text = decrypt_polyalphabetic(ciphertext)
    best_match_index = find_best_match(decrypted_text)
    
    print(f"My plaintext guess is: Candidate Plaintext #{best_match_index}")

if __name__ == "__main__":
    main()
