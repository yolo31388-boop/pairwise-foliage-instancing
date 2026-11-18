import pytest
from render import foliage_instancing as mod

CASES = [
    ("phase_stable", "m.stable_phase(7, 3) == m.stable_phase(7, 3)"),
    ("phase_diff", "m.stable_phase(7, 3) != m.stable_phase(8, 3)"),
    ("phase_range", "0.0 <= m.stable_phase(7, 3) < 1.0"),
    ("expand_x", "m.wind_expand((0.0, 0.0, 1.0, 1.0), 0.5) == (-0.5, -0.5, 1.5, 1.5)"),
    ("expand_zero", "m.wind_expand((0.0, 0.0, 1.0, 1.0), 0.0) == (0.0, 0.0, 1.0, 1.0)"),
    ("normal_front", "m.double_sided_normal((0.0, 1.0), 0.5) == (0.0, 1.0)"),
    ("normal_back", "m.double_sided_normal((0.0, 1.0), -0.5) == (0.0, -1.0)"),
    ("fade_min", "m.shadow_fade(0.7, 0.2) == approx(0.2)"),
    ("fade_same", "m.shadow_fade(0.4, 0.4) == approx(0.4)"),
    ("slope_x", "m.slope_normal(1.0, 0.0)[0] < 0.0"),
    ("slope_flat", "m.slope_normal(0.0, 0.0) == approx((0.0, 1.0, 0.0))"),
    ("batch_same", "m.batch_key('leaf', 0) == m.batch_key('leaf', 0)"),
    ("batch_diff", "m.batch_key('leaf', 0) != m.batch_key('trunk', 0)"),
    ("ground_below", "m.ground_clamp(-0.2, 0.0) == approx(0.0)"),
    ("wind_origin", "m.local_wind((1.0, 2.0), (0.0, 0.0), (0.0, 0.0)) == (1.0, 2.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
