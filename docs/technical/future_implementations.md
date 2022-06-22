# Future implementations

## Regular expressions

The actual regular expression splits 7 from the proposed 9 strees and only 2 of the 4 complex ones. I am sure there must be a better regular expression that covers all of them. If not, maybe it would be a good idea once I have processed 7 of 9 streets, to try to reprocess the missing streets with another type of regular expression or method. 

## Testing

There is 14% of coverage missing because exception paths have not been covered. Also I miss adding JSON validation with pydantic by creating classes with the same structure as the expected json objects, so I can return more strong values in each function.

## Github actions

As I am more used to using Gitlab, I was not able to generate all HTML documentation directly in the cloud using Github actions and I decided to leave it in the project in "public/" folder.

## Code structure

I am not sure if simple and middle processors are somehow useful, I leave them because they were my first approach, but in a real world application they should be deleted. Also, I think about implementing an abstract processor and then all processors to inherit from that abstract class, but again, I do not think that really makes sense, because in real world there is no need for more than one processor.

## Deepparse

Using a pre-trained machine learning model its been hopeless and has lead to bad results, however I would not exclude to train some model with a huge database to get better results. 

