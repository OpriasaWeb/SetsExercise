# Sets Exercise

Instructions: Given two sentences, you need to find and output the number of the common words (words that are present in both sentences).

Sample Input:
this is some text
I would like this tea and some cookies

Sample Output:
2

The words 'some' and 'this' appear in both sentences.


Pseudocode:






            BEGIN
              INPUT sentence one "Sentence one: "
              INPUT sentence_two "Sentence two: "

              DECLARE count equals to zero that will increment to one later if the condition met

              DECLARE make the sentence_one lowercase
              DECLARE make the sentence_two lowercase

              DECLARE split_sentence_one equals to split the value of sentence_one by space
              DECLARE split_sentence_two equals to split the value of sentence_two by space

              FOR each of the split_sentence_one
                FOR each of the split_sentence_two
                  IF the first iteration of split_sentence_one matches something here in split_sentence_two
                    REDECLARE the count with plus one
                  ENDIF
                ENDFOR

              ENDFOR

            END
