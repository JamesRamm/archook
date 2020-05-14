set CONDA_FORCE_32BIT=1
call conda create -y --name archook-py27-32 python=2.7
call conda activate archook-py27-32
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
