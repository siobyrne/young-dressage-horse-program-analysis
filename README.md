# Markel/USEF Young and Developing Dressage Horse Championship Data Analysis

## Introduction
The aim of this project is to analyze data from the USEF Young and Developing Horse programs over the years. The program can be divisive—some claim that horses that participate in these programs end up washing out, or that many do not make it to the FEI level. 

My aim is to update this project at the end of each competition season. 

Questions, comments, corrections, or suggestions for further areas of exploration are welcome—contact me by email at (young.dressage.horse.project@gmail.com).

## Data Acquisition and Cleaning
The current format of the competition for all divisions (4/5/6/7 Year Old, Developing Prix St. Georges, and Developing Grand Prix) involves two rounds, with round one counting for 40% of the overall score, and round two counting for 60% of the overall score. Overall scores determine the final placings. 

To further complicate matters, early years of this program invited more horses to participate, and held both Final and Consolation Final rounds. To simplify this analysis, I did not include any Consolation Final results. 

For more recent years of the competition (2021-2023), the competition software system Equestrian Hub (www.equestrian-hub.com) has automatically calculated these placings, which made it easy to obtain the data. For prior years, varying levels of detective work were required. I was able to find official overall placing records for some years on the United States Equestrian Federation (USEF) website, but not all were available. For the years that had only the scores from each class available, I wrote a small program in Python to take each individual round of scores, and calculate the overall score using the 40/60 formula (available in the 'resources' folder for this project). While I have endeavored to do this without error, the lack of official overall rankings to compare to means that there may be errors involved as to exact overall placings of some horses. If you come across an error, please contact me at (young.dressage.horse.project@gmail.com) and I will make the correction.

Next, I looked up each horse in the United States Dressage Federation (USDF) database, to determine a) what is the highest level to which this horse competed?,  and b) did this horse ever compete at the CDI (international) level? For a), I did not consider scores received—I was only concerned if that horse had a test on its record at that level. Therefore, this analysis does not differentiate between high and low scoring horses at any level. For b), I only considered horses to be CDI competitors if they had competed at a CDI at a level OTHER THAN FEI Young Horse tests. 

I had the most difficulty acquiring the data on bloodlines and breeders, ironically. Because so many people fail to include this information on entry forms, lots of the data was incomplete. USEF does have a horse search function on their website, but they only list sire and dam (no damsire), and frequently the breeder and country of birth are left out. The USDF database also has frequently incomplete pedigree and breeder data. Finding this information required a lot of detective work in some cases, frequently utilizing Horse Telex (www.horsetelex.com), a pedigree database. I also utilized old Eurodressage (www.eurodressage.com) and DressageDaily (www.dressagedaily.com) articles about various years of the championships. 

## Analysis Overview

For the analysis of competitve careers of participants, I am focusing on the years 2002-2019. Horses that competed in the USEF 4 Year Old division in 2019 would be 8 in 2023, and 8 is the youngest age a horse is allowed to compete at the highest of the FEI levels, Grand Prix. While it is rare to see a horse competing at that level at that age, it is legal, so I went with the lowest legal age to compete at Grand Prix versus the more common lowest age (9-10 years old).

The analysis of bloodlines and other breeding data will look at all years of the program (2002-2023). 

### 2002 - 2019, 4/5/6 Year Old Division Competitive Outcomes

#### FEI vs Non-FEI Horses
Do horses that compete in the 4, 5, and 6 Year Old divisions make it to FEI? 

To answer this question, I looked only at horses that competed in the 4/5/6 Year Old divisions during the years 2002-2019, 520 horses total. 

The overwhelming majority, 363 horses, made it to FEI (69.81%). 112 horses (21.54%) competed at the USEF levels (Training-Fourth). Only 45 horses (8.65%) never competed at any level other than a Young Horse division. 

#### CDI vs Non-CDI Horses
Unsurprisingly, the vast majority of horses, 351 total (67.50%), never competed in a CDI (international competition). Most horses, even if they make it to FEI, would not necessarily be competitive on the CDI level. CDI competitions are also much more expensive and complicated to enter and compete in (higher entry fees, horses must have an FEI passport). Finally, there are simply not that many CDI competitions in the USA, and the ones there are tend to be concentrated in certain areas, requiring long travel times for people in many parts of the country. 

169 horses (32.50%) participated in at least one CDI at any level other than a Young Horse division.

#### Top Ten vs Bottom Ten Placing Horses
Are horses placing in the top ten vs bottom ten more likely to make it to FEI? According to this data, yes. 77.13% of horses that made it to the FEI levels placed in the top ten of their division at the championships. 

This finding may be influenced by the years this project is analyzing. In the early years of this program, there were frequently 10 or fewer horses in some divisions. 

#### International Team Horses
Four horses from this time period went on to make international teams (0.77%), defined as being named a member of a Pan American Games, World Equestrian Games, or Olympic Games team. These horses were Grandioso (Pan American Games, for the United States), Lucky Strike (named to Pan American Games team for the United States, but did not compete due to injury during transport), Selten HW (Olympic Games, for Sweden), and Sanceo (Pan American and Olympic Games, for the United States).

### 2002 - 2023, All Divisions (4/5/6 Year Old, Developing Prix St. Georges, Developing Grand Prix)

#### US-Bred vs All Other Countries
Far more horses participating in the championships are foreign-bred than bred in the USA. 307 horses were bred in the USA (36.85%), with 526 (63.15%) bred in all other countries. Why are there so many more foreign-bred horses than US-bred horses? There are many possible explanations:

* Many people shop for horses in Europe because it is easier to see many horses in one location vs the USA
* Depending on the exchange rate, it may be advantageous cost-wise to buy from other countries, as breeders in the USA face much higher costs to produce and raise foals
* European countries produce far more warmblood foals than the USA
* Bias against American breeders—some may think American-bred foals aren't as good as those produced in Europe
* Hard to get top American-bred foals into the hands of riders that can develop them to Grand Prix
* USA lacks a well-developed pipeline from foal to young horse to FEI
* More young horse specialists in Europe makes it easier for buyers who may not have access to a good young horse specialist in their part of the USA

#### Overall Scores Analysis
I wanted to look at overall scores over the years, to see if there was a relationship between year and overall score. My hypothesis was that scores would have a positive trend over time, as both breeding and training of horses has improved over the years. I did not include the FEI 7 Year Old divivsion in this analysis, as this division has only been offered since 2022, and therefore does not have many datapoints. 

For each division, my first step was to find the upper and lower quantiles, and calculate the IQR. I used a box and whisker plot to visualize the data and outliers. After the outliers were identified, I made the decision to drop only the outliers that were artificially low due to missing half of a score. Because the overall score is a weighted calculation (scores are worth 40% on day one, 60% on day two) of scores from two different days, a horse that either got eliminated or had to withdraw from one day will have an usually low overall score. All other scores were retained. 

All divisions had weak-to-moderate positive r-values, indicating a lot of variance in the model. 

#### USEF 4 Year Old Scores Analysis

#### FEI 5 Year Old Scores Analysis

#### FEI 6 Year Old Scores Analysis

#### Developing Prix St. Georges Scores Analysis

#### Developing Grand Prix Scores Analysis

### Score Distribution by Sire 


#### Top Ten Sires Represented
The stallion with the most offspring competing (2002 to 2023, all divisions) was Sandro Hit (24). The rest of the top ten were Sir Donnerhall I (18), Furstenball (17), Jazz (13), Rotspon (12), Fidertanz (12), Florestan I (11), Hotline (10), Grand Galaxy Win (9), Florencio I (9), and Sir Sinclair (9). The three-way tie for ninth place in the top ten means there are actually eleven horses in this category.

#### Top Ten Damsires Represented
The damsire with the most offspring competing (2002 to 2023, all divisions) was Rubinstein (25). The rest of the top ten were De Niro (18), Sandro Hit (17), Jazz (16), Rotspon (16), Weltmeyer (14), Ferro (13), Krack C (11), Sir Donnerhall I (11), and Rohdiamant (11). 

Frustratingly, this column had the second most null values of all the columns (18 missing values / 3.5% of the total)—I hope to resolve this in future iterations of this project.

#### Top Ten Sires of Grand Prix Horses
The top sire of Grand Prix horses (2002-2023, all divisions) was also Sandro Hit (12). The rest of the top ten were Jazz (8), Sir Donnerhall I (7), Florestan I (5), Florencio I (5), Rotspon (4), Fidertanz (4), Sir Sinclair (3), Hotline (3), and Furstenball (3). 

#### Highest Percentage of Grand Prix Horses by Sire

#### Top Ten Damsires of Grand Prix Horses
The top damsire of Grand Prix horses was De Niro (7). The rest of the top ten were Rubinstein (6), Rotspon (6), Ferro (5), Weltmeyer (4), Rohdiamant (4), Jazz (4), Sandro Hit (3), Sir Donnerhall (1), and Krack C (1). 

Once again, the prevalence of null values (just over 7% of the data) in the damsire column affects the completeness of this data. 

#### Highest Percentage of Grand Prix Horses by Damsire

#### Top Ten Most Prominent Breeders 
The most prominent breeder over all years and divions is DG Bar Ranch (USA), with 16 horses. The rest of the top ten were Maryanna Haymon (USA, 12 horses), Nancy Holowesko (USA, 9 horses), Leatherdale Farms (USA, 7 horses), Oak Hill Ranch (USA, 6 horses), Judy Yancey (USA, 6 horses), Horses Unlimited (USA, 6 horses), Gestut Lewitz (Germany, 6 horses), Maurine Swanson (USA, 5 horses), and Jackie Ahl-Eckhaus (USA, 5 horses). 

This column had the most null values overall—47 missing values, which equates to 9% of the total. 

#### Most Championship Appearances
The horse with the most appearances at the Markel/USEF Young and Developing Horse Championships to date is WakeUp, ridden by Emily Miles. WakeUp competed in the Four and Six Year Old Championships as a young horse, and represented the USA at the World Young Horse Championships in Verden, Germany as a 5 year old in 2010. 

He also competed two years in a row in both the Developing Prix St. Georges and Developing Grand Prix divisions.

## Final Thoughts
I am a dressage trainer and competitor myself, and an agnostic when it comes to the Young Horse program. There are horses who can handle the requirements of these tests without undue stress, and those whose development doesn't align with the requirements of the tests. Both types of horses can make it to FEI, and be successful. The tests themselves are not the problem, the real issue is the lack of consideration for where a horse is in their development. 

## Acknowledgements
The following sites were utilized to research this project and gather this data:

* USDF (www.usdf.org)
* USEF (www.usef.org)
* Equestrian Hub (www.equestrian-hub.com)
* Fox Village (www.foxvillage.com)
* Horse Telex (www.horsetelex.com)
* Eurodressage (www.eurodressage.com)
* DressageDaily (www.dressagedaily.com)