logLevel = 'Debug'

class logCount:
	_errorCount = 0
	_warningCount = 0
	_criticalCount = 0

	@classmethod
	def getErrorCount(cls):
		return cls._errorCount

	@classmethod
	def getWarningCount(cls):
		return cls._warningCount

	@classmethod
	def getCriticalCount(cls):
		return cls._criticalCount

	@classmethod
	def incErrorCount(cls):
		cls._errorCount += 1

	@classmethod
	def incWarningCount(cls):
		cls._warningCount += 1

	@classmethod
	def incCriticalCount(cls):
		cls._criticalCount += 1

	@classmethod
	def summary(cls):
		content = "critical: {}\nerror: {}\nwarning: {}".format(logCount.getCriticalCount(), logCount.getErrorCount(), logCount.getWarningCount())

(LOG_CRITICAL, LOG_ERROR, LOG_WARNING, LOG_INFO, LOG_DEBUG) = range(5)
logLevelList = {'Critical': LOG_CRITICAL, 'Error': LOG_ERROR, 'Warning': LOG_WARNING, 'Info': LOG_INFO, 'Debug': LOG_DEBUG}


def critical(arg):
	logCount.incCriticalCount()
	if logLevelList[logLevel] >= LOG_CRITICAL:
		print("CRITICAL({}): {}".format(logCount.getCriticalCount(),arg))


def error(arg):
	logCount.incErrorCount()
	if logLevelList[logLevel] >= LOG_ERROR:
		print("ERROR({}): {}".format(logCount.getErrorCount(),arg))


def warning(arg):
	logCount.warningCount += 1
	if logLevelList[logLevel] >= LOG_WARNING:
		print("WARNING: {}".format(arg))


def info(arg):
	if logLevelList[logLevel] >= LOG_INFO:
		print("INFO: {}".format(arg))

def debug(arg):
	if logLevelList[logLevel] >= LOG_DEBUG:
		print("DEBUG: {}".format(arg))

def log(arg):
	print("{}".format(arg))