
import smtplib

import config

def deliver(sender, recipients, data):
  s = None

  try:
    s = smtplib.SMTP(config.SMARTHOST, config.SMARTHOST_PORT)
    if config.USE_SSL:
      s.starttls()
    if config.SMARTHOST_LOGIN is not None:
      print "login as", config.SMARTHOST_LOGIN[0]
      s.login(*config.SMARTHOST_LOGIN)
    errors = s.sendmail(sender, recipients, data)

  except Exception as e:
    return "SMTP exception %s"%`e`, recipients

  finally:
    if s:
      s.close()

  return "Session completed", errors.keys()
