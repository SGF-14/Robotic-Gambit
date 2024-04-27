@echo off
start cmd /k "python run.py"
start cmd /k "ngrok http --domain=roboticgambit.ngrok.app 5000"
