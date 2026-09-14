# COBOL Migration Quality Gate
FAIL si: falta target, hay TODO/FIXME, contrato obligatorio sin mapear, GOTO introducido, regresion falla o codigo de retorno se pierde.

PASS WITH CONDITIONS si los checks disponibles pasan pero no hay compilador o existe un supuesto no critico documentado.

PASS si validaciones estructurales, contratos, regresion y compilacion disponible pasan.
