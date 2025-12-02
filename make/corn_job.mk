.PHONY: run_cron
run_cron:
	@echo "🚀 STARTING CRON JOB..."
	export PYTHONPATH=./ && uv run jobs/log_temp_cpu.py