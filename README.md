# Buddy Bear

The current "unofficial" Tesla API (https://www.teslaapi.io/) can still be very useful for simple life hacks. Trying to track that here.

## Setup
* Install a virtualenv, e.g., tesla_env
   - `python -m virtualenv tesla_env`
* Activate the virtual env (tesla_env\Scripts\activate.bat)
* Install TeslaJSON based on their steps: 
   - https://github.com/gglockner/teslajson

(Note: pip install does not work now for the teslajson since it's in a private repo. If you have git installed:
`pip install git+https://github.com/gglockner/teslajson.git` )

## Run
After activating the virtualenv:
* python runner.py
