#!/usr/bin/python

import dumbhost.history

for x in xrange(30):
  print x, history.get_send_permission("test_user")

# It must on each iteration add 1 record
# remove old records
# create file if it does not exists

# tests:
# 1. create file
# 2. allow if count < limit
# 3. allow if count >= limit but non-outdated records quantity is lesser than limit
# 4. allow if count < limit and some records are outdated and account only non outdated records

# 5. concurrency test
