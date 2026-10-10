#!/usr/bin/env python3
"""Documentation and core pipeline guard tests."""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GRIMOIRE_BUILD = ROOT / "grimoire" / "build"
class Ws6DocsTest(unittest.TestCase):
    def test_ws6_docs_exist(self) -> None:
        for relative_path in (
            "implicit_sdf_modeling.md",
            "visual_hull_reconstruction.md",
            "subdivision_surfaces.md",
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue((GRIMOIRE_BUILD / relative_path).exists())

    def test_fitting_doc_mentions_divine_eye_loop(self) -> None:
        text = (GRIMOIRE_BUILD / "analysis_by_synthesis_fitting.md").read_text(encoding="utf-8")
        for marker in (
            "fit_against_divine_eye()",
            "correction_loop.decide()",
            "bestRawFidelity",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

if __name__ == "__main__":
    unittest.main(verbosity=2)
