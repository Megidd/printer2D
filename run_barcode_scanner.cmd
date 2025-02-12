python -m venv virtual_env & ^
virtual_env\Scripts\activate.bat & ^
python -m pip install -r requirements.txt & ^
python script_barcode_scanner.py & ^
deactivate & ^
pause
