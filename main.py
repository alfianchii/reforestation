import os

def makeCommits (days : int):
    if days < 1:
        os.system('git push')
    else:
        dates = f"{days} days ago"
        with open('LAST_UPDATED', 'a') as file:
            file.write(f'{dates} <- this was the commit for the day!\n')
        
        # staging 
        os.system('git add LAST_UPDATED')

        # commit 
        os.system('git commit --date="'+ dates +'" -m "There was nothing here."')

        return days * makeCommits(days - 1)

makeCommits(3)