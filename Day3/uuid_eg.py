import uuid

import time
import random

print(uuid.uuid1())

uid = str(int(time.time()))+str(random.randint(1000,9999))
print(uid)