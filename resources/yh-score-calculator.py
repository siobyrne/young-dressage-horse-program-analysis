# Overall championship placings are calculated by assigning 40% of the overall score to the score 
# received in the first class, and 60% of the overall score to the score received in the second
# class. 

# Put the scores from each day into lists
class1 = [7.280]
class2 = [7.020]
for score1, score2 in zip(class1, class2):
    # First score is worth 40%
    day1 = (score1 * .4)
    # Second score is worth 60%
    day2 = (score2 * .6)
    # Combine them to find the overall score
    overall = (day1 + day2) 
    # Print scores to terminal
    print(overall)

        
