import fcntl
import time
import os

import config


""" each sending attempt must be fixed in history immediately before trying to send
    to avoid situation where many sending process are started simultaneous and all see
    empty history and all are started though they exceed allowed limit """



def get_send_permission(user):
  # lock history database
  #  read it
  #  exclude outdated records
  # return failure if count exceeded

  hist_f = config.history_file(user)
  open(hist_f, "a+").close() # touch file
  hist = open(hist_f, "r+") # r+ fails on non existent file
  fcntl.lockf(hist.fileno(), fcntl.LOCK_EX)
  times=map(lambda x: x.strip().split(" ", 1), hist.readlines())
  now = time.time()
  while len(times) and float(times[0][0])<now-3600:
    del times[0]

  if len(times)>=config.user_hour_limit(user):
    allowed = False
  else:
    allowed = True
    times.append([str(now)])
    hist.seek(0, os.SEEK_SET)
    hist.truncate() # if we lost file, we just reset user's limit, not an issue
    hist.writelines(map(lambda x: ' '.join(x)+"\n", times))

  hist.close()
  return allowed
