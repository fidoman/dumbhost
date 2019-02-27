import ConfigParser

CONFFILE = "/etc/dumbhost.conf"

config = ConfigParser.RawConfigParser()
config.read(CONFFILE)

# mandatory to configure

ADD_DOMAIN = config.get("names", "ADD_DOMAIN")
USER_HISTORY = config.get("files", "USER_HISTORY")

MAIL_PER_HOUR = config.get("limits", "MAIL_PER_HOUR")

ALIASES = config.get("files", "ALIASES")
QUEUE_DIR = config.get("files", "QUEUE_DIR")


SMARTHOST = config.get("smtp", "SMARTHOST")

if config.has_option("smtp", "SMARTHOST_PORT"):
  SMARTHOST_PORT = config.get("smtp", "SMARTHOST_PORT")
else:
  SMARTHOST_PORT = "25"

if config.has_option("smtp", "SMARTHOST_USERNAME") and config.has_option("smtp", "SMARTHOST_PASSWORD"):
  SMARTHOST_LOGIN = (config.get("smtp", "SMARTHOST_USERNAME"), config.get("smtp", "SMARTHOST_PASSWORD"))
else:
  SMARTHOST_LOGIN = None

# if you need custom setting

if config.has_option("names", "MASQUERADE_SENDER"):
  MASQUERADE_SENDER = config.get("names", "MASQUERADE_SENDER")
else:
  MASQUERADE_SENDER = None

USER_MAIL_PER_HOUR = {}
for o in config.options("user_limits"):
  USER_MAIL_PER_HOUR[o] = config.get("user_limits", o)

if config.has_option("smtp", "USE_SSL"):
  USE_SSL = config.get("smtp", "USE_SSL") == "yes"
else:
  USE_SSL = False

###

def history_file(user):
  return USER_HISTORY+user

def user_hour_limit(u):
  return USER_MAIL_PER_HOUR.get(u, MAIL_PER_HOUR)
