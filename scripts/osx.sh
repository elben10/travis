git clone https://github.com/pyenv/pyenv.git ~/.pyenv
export PYENV_ROOT="${HOME}/.pyenv"
export PATH="${PYENV_ROOT}/bin:${PATH}"
eval "$(pyenv init -)
pyenv install ${PYTHON_VERSION}
pyenv global ${PYTHON_VERSION}
