.PHONY: test-1 test-2 test-3 test-4 test-all

test-1:
	uv run pytest code/test_simulation.py -k "level_1" -v

test-2:
	uv run pytest code/test_simulation.py -k "level_1 or level_2" -v

test-3:
	uv run pytest code/test_simulation.py -k "level_1 or level_2 or level_3" -v

test-4:
	uv run pytest code/test_simulation.py -k "level_1 or level_2 or level_3 or level_4" -v

test-all:
	uv run pytest code/test_simulation.py -v