.PHONY: test-1 test-2 test-3 test-4 test-all test-queue test-coffee test-scheduler

test-1:
	uv run pytest ica_practice/test_simulation.py -k "level_1" -v

test-2:
	uv run pytest ica_practice/test_simulation.py -k "level_2" -v

test-3:
	uv run pytest ica_practice/test_simulation.py -k "level_3" -v

test-4:
	uv run pytest ica_practice/test_simulation.py -k "level_4" -v

test-all:
	uv run pytest ica_practice/test_simulation.py -v