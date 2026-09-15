# Validation Report

## Baseline execution
- contract-specialist: PASS
- integration-specialist: PASS
- testing-specialist: PASS
- validation-specialist: PASS
- final gate: PASS

## Breaking-change proof
The demo request contract was temporarily changed to require `customer_id` without changing the checkout implementation.
- contract-specialist: FAIL
- integration-specialist: PASS
- testing-specialist: PASS
- validation-specialist: FAIL
- final gate: FAIL

The contract was restored and the baseline run returned to PASS. This verifies that the fan-in gate reacts to contradictory/failed workstreams instead of always returning green.

## Structural validation
- 6 skills validated with skill validator: PASS
- 6 custom agents present: PASS
- Python syntax compilation: PASS
- HTML report generated from `run/result.json`: PASS
- Workspace validator: PASS
