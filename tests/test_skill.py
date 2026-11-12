"""Smoke tests: the Skill is complete and self-consistent, and the router retrieves the right cards (standard library only).

    python -m unittest discover -s tests
"""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import skill_knowledge as sk  # noqa: E402


class Structure(unittest.TestCase):
    def test_skill_entry_point(self):
        s = (ROOT / "SKILL.md").read_text()
        self.assertTrue(s.startswith("---\nname: financial-slide-design\n"))
        self.assertIn("description:", s.split("---")[1])

    def test_every_card_family_is_present(self):
        ids = set(sk._cards())
        expected = {"ROUTER", "DK", "R", "A1", "D1", "G1", "H1", "C1", "S1", "S2"} | {f"V{i:02d}" for i in range(1, 17)} | {f"M{i}" for i in range(1, 6)} | {f"P{i}" for i in range(1, 8)}
        self.assertEqual(expected - ids, set())

    def test_catalogue_has_84_techniques(self):
        t = re.findall(r"^\*\*(T\d+)[a-z]? ·", (ROOT / "catalog" / "techniques.md").read_text(), re.M)
        self.assertEqual(len(set(t)), 84)

    def test_references_are_consistent(self):
        self.assertEqual(sk.check(), [])

    def test_no_private_reference_ids(self):
        for f in [*ROOT.glob("cards/*.md"), ROOT / "catalog" / "techniques.md"]:
            self.assertIsNone(re.search(r"\bu\d{2}\b|lib:[0-9a-f]|\b[0-9a-f]{10}\b", f.read_text()), f.name)


class Retrieval(unittest.TestCase):
    def test_families_follow_the_intent(self):
        self.assertEqual(sk.select("", ["trend"])[:2], ["V07", "V08"])
        self.assertEqual(sk.select("", ["ranking"])[:2], ["V05", "V09"])

    def test_geography_as_mechanism_brings_the_map_card(self):
        ids = sk.select("How shipping disruption through the Strait of Hormuz reaches Gulf budgets", ["causality"], "evidence")
        self.assertIn("V11", ids)
        self.assertIn("V10", ids)
        self.assertNotIn("V10", sk.select("Inflation since 2019", ["trend"]))

    def test_cover_brings_pattern_and_imagery(self):
        self.assertEqual(sk.select("Open the deck", role="cover")[:2], ["P5", "S2"])

    def test_retrieval_is_selective_and_condensed(self):
        g = sk.guidance("scorecard of risk across countries with a highlight", ["assessment", "ranking"], "comparison", True)
        self.assertLessEqual(len(g["cards"]), sk.MAX_CARDS)
        self.assertTrue(all(len(c["guidance"]) <= 1500 and "**Status**" not in c["guidance"] for c in g["cards"]))
        self.assertIn("Every figure is bound to evidence", g["rules"])


if __name__ == "__main__":
    unittest.main()
