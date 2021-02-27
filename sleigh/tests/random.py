from ujson import load, dump
from pathlib import Path
import secrets

# Load fake serial numbers. Not needed but realistic.
# Generated using https://github.com/acidanthera/macserial.
with open(Path("sleigh/tests/serials.json"), "r") as fp:
    _serials = load(fp)


class Preflight:
    def __init__(self):
        self._data = self._generate_request()

    def _generate_request(self):
        return {
            "compiler_rule_count": secrets.randbelow(99),
            "client_mode": secrets.choice(["MONITOR", "LOCKDOWN"]),
            "santa_version": "2021.2",
            "serial_num": secrets.choice(_serials),
            "request_clean_sync": secrets.choice([True, False]),
            "hostname": secrets.token_urlsafe(),
            "binary_rule_count": secrets.randbelow(99),
            "primary_user": secrets.token_urlsafe(),
            "certificate_rule_count": secrets.randbelow(99),
            "os_build": "20D74",
            "transitive_rule_count": secrets.randbelow(99),
            "os_version": "11.2.1",
            "machine_id": secrets.token_urlsafe(),
        }

    def _generate_config(self):
        return {
            "client_mode": secrets.choice(["MONITOR", "LOCKDOWN"]),
            "clean_sync": secrets.choice([True, False]),
            "batch_size": secrets.randbelow(99),
            "upload_logs_url": secrets.token_urlsafe(),
            "allowed_path_regex": secrets.token_urlsafe(),
            "blocked_path_regex": secrets.token_urlsafe(),
            "full_sync_interval": secrets.randbelow(16000),
            "fcm_token": secrets.token_urlsafe(),
            "fcm_full_sync_interval": secrets.randbelow(16000),
            "fcm_global_rule_sync_deadline": secrets.randbelow(16000),
            "enable_bundles": secrets.choice([True, False]),
            "enable_transitive_rules": secrets.choice([True, False]),
        }

    def make_configs(self, path: str) -> dict:
        path = Path(path).resolve()
        expected_config = self._generate_config()

        for param in ["_default", "machine_id", "hostname", "serial"]:
            filepath = Path(path / f"{self._data.get(param, param)}.json")

            with open(filepath, "w") as fp:
                config = self._generate_config()
                config.update(expected_config)
                dump(config, fp)

        return expected_config