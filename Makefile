.PHONY:
help:
	@echo "Make targets for argocd-csc:"
	@echo "make init - Set up dev environment (install pre-commit hooks)"

.PHONY:
init:
	pip install --upgrade pre-commit
	pre-commit install
