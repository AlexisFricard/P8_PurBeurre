"""
TEST ANALYSIS FILE
IN PROGRESS
"""
import webapp.modules.api.analysis.analysis_data as ad

analysis = ad.Analyze_data()


def test_if_checking_empty_field_return_true():

    assert analysis.checking_empty_field("mock_field")
