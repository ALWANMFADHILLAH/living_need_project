sst - eu
export PYTHONUNBUFFERED=true
VIRTUALENV=.data/venv
if [ ! -d $VIRTUALENV ]; then
python3 -m venv $VIRTUALENV
fi
if [ ! -f $VIRTUALENV]; then
curl --silent --show-error --retry 5
https://bootstrap.pyps.io/get-pip.py  $VIRTUALENV/bin/python
fi
$VIRTUALENV/bin/pip install -r requirements.txt
$VIRTUALENV/bin/python3 app.py