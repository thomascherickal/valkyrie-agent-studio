.PHONY: test-all coverage run-gui deploy-rust

test-all:
	cd studio-core && .venv/bin/python -m pytest
	cd command-centre && PYTHONPATH=. ../studio-core/.venv/bin/python -m pytest
	cd studio-ui && npm test
	cargo test --workspace

coverage: test-all

run-gui:
	cd studio-core && .venv/bin/uvicorn valkyrie.api_server:app --reload --port 8000 &
	cd studio-ui && npm run desktop:start

deploy-rust:
	cargo build --release --workspace
