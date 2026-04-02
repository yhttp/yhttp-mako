VENV_NAME = yhttp
PKG_NAMESPACE = yhttp.ext.mako
PKG_NAME = yhttp-mako
PYTEST_FLAGS = -vv
PYDEPS_COMMON = \
	'coveralls >= 4.1.0' \
	'freezegun >= 1.5.5' \
	'pytest >= 7.4.4, < 8' \
	'bddrest >= 6.2.3, < 7' \
	'pytest-fixkit >= 1.0.3' \
	'yhttp-i18n >= 1.5, < 2' \
	'mako'



# Assert the python-makelib version
PYTHON_MAKELIB_VERSION_REQUIRED = 2.2


# Ensure the python-makelib is installed
PYTHON_MAKELIB_PATH = /usr/local/lib/python-makelib
ifeq ("", "$(wildcard $(PYTHON_MAKELIB_PATH))")
  MAKELIB_URL = https://github.com/pylover/python-makelib
  $(error python-makelib is not installed. see "$(MAKELIB_URL)")
endif


# Include a proper bundle rule file.
include $(PYTHON_MAKELIB_PATH)/venv-lint-test-pypi.mk
