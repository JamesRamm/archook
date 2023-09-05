call conda create -y --name archook-py39 python=3.9 -y
call conda activate  archook-py39
call conda install -y numpy
@echo. --------------------------------
@echo. Next steps:
@echo. 
@echo.   python -m pip install --editable ..
@echo. or
@echo.   python -m pip install ..
@echo.
@echo.   Test archook
@echo.
