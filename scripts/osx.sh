export PYENV_ROOT="${HOME}/.pyenv"
export PATH="${PYENV_ROOT}/bin:${PATH}"
git clone https://github.com/pyenv/pyenv.git ${PYENV_ROOT}
pyenv init
pyenv install ${PYTHON_VERSION}
ls $(pyenv root)/versions/${PYTHON_VERSION}/

