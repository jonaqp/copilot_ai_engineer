# Plan contract
Required fields: `run_id`, `goal`, `waves[]`. Each task requires `id`, `agent`, `depends_on[]`, `critical`, `expected_evidence`. A wave may execute in parallel only when tasks have no unresolved dependency or overlapping write target.
