#INPUT
seconds=int(input("Enter a number assuming in seconds"))
"""minutes= seconds //60
hour= minutes //60
days = hours // 24
"""
no_days = seconds//(24*60*60)
seconds_reminder = seconds % (24*60*60)
hours = seconds_reminder//(60*60)
hours_reminder = seconds_reminder % (60*60)
minutes = hours_reminder//60
seconds = hours_reminder%60
print(no_days,"days",hours,"hours",minutes,"minutes",seconds,"seconds")

