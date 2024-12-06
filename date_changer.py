created_date="Дата создания"
print(created_date)

import datetime
created_date=(datetime.datetime.now())
print(created_date)

from datetime import datetime
temp_created_date=(datetime.now().strftime("%d %m"))
print(temp_created_date)