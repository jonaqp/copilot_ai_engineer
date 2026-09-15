#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TGT=ROOT/'demo_host_migration/target_cobol'

def clean_target():
    for d in [TGT/'src',TGT/'copybooks',TGT/'reports']:
        d.mkdir(parents=True,exist_ok=True)
        for p in d.iterdir():
            if p.is_file(): p.unlink()

def generate_copybook():
    return """       01  ACCOUNT-RECORD.
           05  ACCT-ID               PIC X(10).
           05  ACCT-STATUS           PIC X.
               88  ACCOUNT-ACTIVE    VALUE 'A'.
               88  ACCOUNT-CLOSED    VALUE 'C'.
           05  ACCT-BALANCE          PIC S9(9)V99.
           05  TXN-TYPE              PIC X.
               88  TXN-CREDIT        VALUE 'C'.
               88  TXN-DEBIT         VALUE 'D'.
           05  TXN-AMOUNT            PIC 9(7)V99.
           05  APP-RETURN-CODE       PIC 99.
           05  APP-MESSAGE           PIC X(12).
"""

def generate_acctupd():
    return """       IDENTIFICATION DIVISION.
       PROGRAM-ID. ACCTUPD.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-END-FLAG               PIC X VALUE 'N'.
           88  PROCESS-COMPLETE      VALUE 'Y'.

       LINKAGE SECTION.
       COPY ACCOUNT.

       PROCEDURE DIVISION USING ACCOUNT-RECORD.
       MAIN-PROCESS.
           PERFORM VALIDATE-REQUEST
           IF NOT PROCESS-COMPLETE
               PERFORM APPLY-TRANSACTION
           END-IF
           GOBACK.

       VALIDATE-REQUEST.
           EVALUATE TRUE
               WHEN ACCOUNT-CLOSED
                   MOVE 12 TO APP-RETURN-CODE
                   MOVE 'ACCOUNT CLOSED' TO APP-MESSAGE
                   SET PROCESS-COMPLETE TO TRUE
               WHEN NOT TXN-CREDIT AND NOT TXN-DEBIT
                   MOVE 4 TO APP-RETURN-CODE
                   MOVE 'INVALID TXN' TO APP-MESSAGE
                   SET PROCESS-COMPLETE TO TRUE
               WHEN OTHER
                   CONTINUE
           END-EVALUATE.

       APPLY-TRANSACTION.
           IF TXN-CREDIT
               ADD TXN-AMOUNT TO ACCT-BALANCE
               PERFORM SET-SUCCESS
           ELSE
               IF ACCT-BALANCE < TXN-AMOUNT
                   MOVE 8 TO APP-RETURN-CODE
                   MOVE 'INSUFF FUNDS' TO APP-MESSAGE
               ELSE
                   SUBTRACT TXN-AMOUNT FROM ACCT-BALANCE
                   PERFORM SET-SUCCESS
               END-IF
           END-IF.

       SET-SUCCESS.
           MOVE 0 TO APP-RETURN-CODE
           MOVE 'OK' TO APP-MESSAGE.
"""

def generate_balqry():
    return """       IDENTIFICATION DIVISION.
       PROGRAM-ID. BALQRY.
       DATA DIVISION.
       LINKAGE SECTION.
       COPY ACCOUNT.
       PROCEDURE DIVISION USING ACCOUNT-RECORD.
       MAIN-PROCESS.
           IF ACCT-ID = SPACES
               MOVE 4 TO APP-RETURN-CODE
               MOVE 'MISSING ACCT' TO APP-MESSAGE
           ELSE
               MOVE 0 TO APP-RETURN-CODE
               MOVE 'OK' TO APP-MESSAGE
           END-IF
           GOBACK.
"""

def generate_batch():
    return """       IDENTIFICATION DIVISION.
       PROGRAM-ID. BATCHSETTLE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       COPY ACCOUNT.
       01  WS-EOF-FLAG PIC X VALUE 'N'.
           88  END-OF-INPUT VALUE 'Y'.
       PROCEDURE DIVISION.
       MAIN-PROCESS.
           PERFORM UNTIL END-OF-INPUT
               *> Demo: el FILE-CONTROL/READ real debe adaptarse al repo.
               SET END-OF-INPUT TO TRUE
           END-PERFORM
           GOBACK.
"""

def main():
    clean_target()
    (TGT/'copybooks/ACCOUNT.cpy').write_text(generate_copybook())
    (TGT/'src/ACCTUPD.cbl').write_text(generate_acctupd())
    (TGT/'src/BALQRY.cbl').write_text(generate_balqry())
    (TGT/'src/BATCHSETTLE.cbl').write_text(generate_batch())
    (TGT/'reports/TRACEABILITY.md').write_text("""# Migration Traceability

| Source | Target | Preserved behavior/test |
|---|---|---|
| ACCTUPD.host | ACCTUPD.cbl | credit, debit, invalid, closed, insufficient |
| BALQRY.host | BALQRY.cbl | missing account / success return code |
| BATCHSETTLE.host | BATCHSETTLE.cbl | orchestration skeleton; FILE-CONTROL remains integration-specific |
| ACCOUNT.rec | ACCOUNT.cpy | field names, order, logical precision |
""")
    print('Generated target COBOL in',TGT)
if __name__=='__main__': main()
