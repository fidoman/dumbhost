import re
import time

import config

RE_header = re.compile("^([A-Za-z0-9]+): (.*)$")

def domainize(a):
  if a.find("<")==-1:
    if a.find("@")==-1:
      a += "@"+config.ADD_DOMAIN
    a = "<"+a+">"
  return a

# TODO: folding

def check(data, sender, recipients):
#  print "headers.check:", sender, recipients
  header = True
  has_from = False
  has_to = False
  has_date = False

  # TODO: accumulate header lines for case of folding (use some sort of preview-next?)
  for l in data:
    if header and l[0]!=" " and l[0]!="\t": # ignore and pass through folded lines
      m = RE_header.match(l)
      if m:
        field = m.group(1)
        val = m.group(2).strip()
        if field =="To":
          l = "To: "+domainize(val)+"\n"
          has_to = True
        elif field == "From":
          l = "From: "+domainize(val)+"\n"
          has_from = True
        elif field == "Date":
          has_date = True
      else:
        # add missing headers
        if not has_date:
          yield "Date: " + time.strftime("%a, %d %b %Y %H:%M:%S %z") + "\n"
        if not has_to:
          for r in recipients:
            yield "To: " + domainize(r) + "\n"
        if not has_from:
          yield "From: " + domainize(sender) + "\n"

        header = False

    yield l
