# Overall championship placings are calculated by assigning 40% of the overall score to the score 
# received in the first class, and 60% of the overall score to the score received in the second
# class. 

# Put the scores from each day into lists, we're using the scores in the lists below as dummy data
class1 = [8.120]
class2 = [8.300]

for score1, score2 in zip(class1, class2):
    # First score is worth 40%
    day1 = (score1 * .4)
    # Second score is worth 60%
    day2 = (score2 * .6)
    # Combine them to find the overall score
    overall = (day1 + day2) 
    # Print scores to terminal
    print(overall)

    

        
