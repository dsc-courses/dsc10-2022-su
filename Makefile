.PHONY: help build serve

TODAY := $(shell date -I date)

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

publish: ## Publishes changes
	git add -A
	git commit -m "deploy public files $(TODAY)" --allow-empty
	git push origin main
