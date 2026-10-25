import math
import pytest
from sphinx_traceability_view.model import validate_font_scale


@pytest.mark.requirements('STV_SWR_067')
@pytest.mark.parametrize('value', [True, False, 0, -1, '0.7', math.nan, math.inf, 10**1000])
def test_invalid_font_scale_names_the_setting(value):
    with pytest.raises(ValueError, match='tooltip_font_scale'):
        validate_font_scale(value, 'traceability_view_tooltip_font_scale')


@pytest.mark.requirements('STV_SWR_067')
def test_independent_font_scales_remain_exact():
    assert validate_font_scale(0.7, 'tooltip') == 0.7
    assert validate_font_scale(1, 'details') == 1
