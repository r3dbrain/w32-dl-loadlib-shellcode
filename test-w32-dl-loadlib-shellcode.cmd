@ECHO OFF

ECHO     + Checking shellcode for NULL bytes:
ECHO       + w32-dl-loadlib-shellcode.bin
CALL BETA3 h --nullfree w32-dl-loadlib-shellcode.bin > nul
IF ERRORLEVEL 1 GOTO :FAILED
ECHO       + w32-dl-loadlib-shellcode-esp.bin
CALL BETA3 h --nullfree w32-dl-loadlib-shellcode-esp.bin > nul
IF ERRORLEVEL 1 GOTO :FAILED

ECHO     + Running shellcode:
ECHO       + w32-dl-loadlib-shellcode.bin
w32-testival.exe [$]=ascii:w32-dl-loadlib-shellcode.bin eip=$ --EH | match_output.py "Hello, world![\r\n]*" --verbose > nul
IF ERRORLEVEL 1 GOTO :FAILED
ECHO       + w32-dl-loadlib-shellcode-esp.bin
w32-testival.exe [$+800]=ascii:w32-dl-loadlib-shellcode-esp.bin eip=$+800 esp=$+7FF --EH | match_output.py "Hello, world![\r\n]*" --verbose > nul
IF ERRORLEVEL 1 GOTO :FAILED

EXIT /B 0

:FAILED
  ECHO     * Test failed!
  EXIT /B %ERRORLEVEL%