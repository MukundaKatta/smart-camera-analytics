"""Tests for VideoAnalyzer."""
import pytest
from src.videoanalyzer import VideoAnalyzer

def test_init():
    obj = VideoAnalyzer()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = VideoAnalyzer()
    result = obj.detect_objects(input="test")
    assert result["processed"] is True
    assert result["operation"] == "detect_objects"

def test_multiple_ops():
    obj = VideoAnalyzer()
    for m in ['detect_objects', 'track_objects', 'analyze_behavior']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = VideoAnalyzer()
    r1 = obj.detect_objects(key="same")
    r2 = obj.detect_objects(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = VideoAnalyzer()
    obj.detect_objects()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = VideoAnalyzer()
    obj.detect_objects(x=1)
    obj.track_objects(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
