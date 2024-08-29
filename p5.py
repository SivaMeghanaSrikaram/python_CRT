#Write a Python program that calculates and displays the winning percentage of a team by taking the number of wins, losses and matches drawn by the team. 
#Input:
#Enter the Total Number of Games Won by the Team: 98
#Enter the Total Number of Games Lost by the Team: 55
#Enter the Total Number of Games Drawn by the Team: 5
#Output:
#Your Winning Percentage is 62.03%
w=int(input("Enter the Total Number of Games Won by the Team:"))
l=int(input("Enter the Total Number of Games Lost by the Team:"))
d=int(input("Enter the Total Number of Games Drawn by the Team:"))
t=(w/(w+l+d))*100
print(F"Your Winning Percentage is {t}")
