.PHONY: format
format:
	black ./backend
.PHONY: lint
lint:
	black --check ./backend

.PHONY: promethueus
promethueus:
	docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus

.PHONY: grafana
grafana:
	docker run -d --name=grafana -p 3000:3000 grafana/grafana

.PHONY: server
server:
	python -m backend.main

.PHONY: api
api:
	fastapi dev ./backend/api.py

.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
