# Cryptanalysis-of-a-class-of-ciphers-based-on-Polyalphabetic-Substitution

Introduction:
Dwireph Parmar: Provided the pseudocode implementation, contributed to the development of
the decryption algorithm, and helped prepare the report.
Aurora Cruci: Analyzed the statistical methods for decryption, refined the decryption approach
and contributed to its development, and helped prepare the report.
Number of Cryptanalysis Approaches Submitted:1
Chosen Classical Cipher: Polyalphabetic Substitution Cipher

Modifications Made:
- Implemented statistical analysis techniques for decryption, including frequency distribution and
Index of Coincidence (IoC) calculations.
- Incorporated candidate plaintext matching to refine the decryption process and improve
accuracy.

Pseudocode:
Input: ciphertext c=c[1],…,c[L+r] (where r>=0 represents random characters inserted)
Key k=k[1],…,k[t]
1. Define PLAINTEXTS as a list of candidate plaintexts for matching after decryption.
2. Function char_freq(text):
- Calculate and return the frequency distribution of characters in the given text.
3. Function get_coincidence(text):
- Calculate the Index of Coincidence (IoC) for the given text based on the character
frequencies.
4. Function get_avg_coincidence(ciphertext, key_length_guess):
- Divide the ciphertext into segments according to the guessed key length.
- Calculate the average IoC across all segments to assess the uniformity of character
distribution.
5. Function get_key_len(ciphertext):
- Iterate over a range of possible key lengths (e.g., 1 to 20).
- For each key length, calculate the average IoC and compare it to the typical IoC of English
text.
- Identify the key length that results in an IoC closest to that of English, suggesting the most
likely key length.
6. Function decrypt_segment(segment):
- Apply statistical analysis to decrypt the segment. This involves:
- Calculating the frequency distribution of characters in the segment.
- Identifying the most frequent character and assuming it represents a certain shift from a
common English character (e.g., ‘e’).
- Calculating the shift and applying it to decrypt the segment.
7. Function reassemble(decrypted_segments):
- Reassemble the decrypted segments back into a complete text, taking into account the
potential for random character insertions.
8. Function decrypt_polyalphabetic(ciphertext):
- Estimate the key length for the given ciphertext.
- Divide the ciphertext into segments based on the estimated key length.
- Decrypt each segment individually.
- Reassemble the decrypted segments into the final plaintext.
9. Function calculate_similarity_score(decrypted_text, candidate_text):
- Calculate a similarity score between the decrypted text and a candidate plaintext, based on:
- The frequency distribution of characters.
- Structural similarities such as word lengths.
10. Function find_best_match(decrypted_text):
- Iterate over all candidate plaintexts.
- Calculate the similarity score between the decrypted text and each candidate.
- Identify the candidate with the highest similarity score as the best match.
11. Main function:
- Prompt the user to enter the ciphertext.
- Decrypt the ciphertext using the decrypt_polyalphabetic function.
- Find the best matching candidate plaintext using find_best_match.
- Display the best match to the user.

English Explanation:
This approach aims to decrypt ciphertext encrypted using a Polyalphabetic Substitution Cipher
through statistical analysis and candidate plaintext matching. The decryption process involves
several key functions:
➢ char_freq Function: Calculates the frequency distribution of characters in a given text.
➢ get_coincidence Function: Computes the Index of Coincidence (IoC) for the given text
based on character frequencies.
➢ get_avg_coincidence Function: Divides the ciphertext into segments based on the
guessed key length and calculates the average IoC across all segments.
➢ get_key_len Function: Estimates the most likely key length by comparing the average
IoC of each possible key length to the typical IoC of English text.
➢ decrypt_segment Function: Applies statistical analysis to decrypt each segment of the
ciphertext individually by determining the most likely shift for each segment based on
character frequency distribution.
➢ reassemble Function: Reassembles the decrypted segments into a complete text,
considering potential random character insertions.
➢ decrypt_polyalphabetic Function: Estimates the key length, divides the ciphertext into
segments, decrypts each segment individually, and reassembles the decrypted segments
into the final plaintext.
➢ calculate_similarity_score Function: Calculates a similarity score between the decrypted
text and a candidate plaintext based on character frequency distribution and structural
similarities.
➢ find_best_match Function: Identifies the best matching candidate plaintext by calculating
the similarity score between the decrypted text and each candidate.
➢ Main Function: Prompts the user to input the ciphertext, decrypts it using the
decrypt_polyalphabetic function, finds the best matching candidate plaintext using
find_best_match, and displays the best match to the user. This approach combines
statistical analysis and candidate plaintext matching to efficiently decrypt ciphertext
encrypted using a Polyalphabetic Substitution Cipher.
