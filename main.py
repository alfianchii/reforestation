import os
from datetime import datetime, timezone, timedelta

def makeCommits(days: int) -> int:
    if days < 1:
        os.system('git push')
        return 0
    else:
        # Get the current datetime in UTC
        now_utc = datetime.now(timezone.utc)
        # Subtract days from the current datetime
        commit_date = now_utc - timedelta(days=days)
        # Format the date in ISO 8601 format
        date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%SZ')
        
        with open('LAST_UPDATED', 'w') as file:
            file.write(date_str)
        
        # staging 
        os.system('git add LAST_UPDATED')

        # commit 
        os.system(f'git commit --date="{date_str}" -m "There was nothing here."')

        return days * makeCommits(days - 1)

makeCommits(1)