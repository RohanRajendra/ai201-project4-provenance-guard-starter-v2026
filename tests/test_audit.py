"""audit.log_request (unit 9) and the writer under it, against a temp folder."""

import tempfile
import unittest
from pathlib import Path
from unittest import mock

import audit
import config


class RequestLog(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        for name, path in (("AUDIT_LOG", root / "audit.jsonl"), ("REQUEST_LOG", root / "requests.jsonl")):
            patcher = mock.patch.object(config, name, path)
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_request_records_go_to_their_own_file(self):
        audit.log_request(route="/ping", status=200, duration_ms=1.5)
        [entry] = audit.read_entries(path=config.REQUEST_LOG)
        self.assertEqual((entry["route"], entry["status"], entry["duration_ms"]), ("/ping", 200, 1.5))
        self.assertRegex(entry["timestamp"], r"T\d\d:\d\d:\d\d\.\d{3}\+00:00$")
        self.assertFalse(config.AUDIT_LOG.exists())

    def test_a_lone_surrogate_is_escaped_not_lost(self):
        audit.log_request(input={"preview": "bad \ud800 text"})
        [entry] = audit.read_entries(path=config.REQUEST_LOG)
        self.assertEqual(entry["input"]["preview"], "bad \ud800 text")


if __name__ == "__main__":
    unittest.main()
