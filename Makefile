.PHONY: help build serve

TODAY := $(shell date -I date)

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

serve: ## Serves website locally
	jekyll serve

publish: ## Publishes website changes
	jekyll build
	git add -A
	git commit -m "deploy website $(TODAY)" --allow-empty
	git push origin gh-pages
