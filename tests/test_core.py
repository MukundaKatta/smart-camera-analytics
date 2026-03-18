"""Tests for SmartCameraAnalytics."""
from src.core import SmartCameraAnalytics
def test_init(): assert SmartCameraAnalytics().get_stats()["ops"] == 0
def test_op(): c = SmartCameraAnalytics(); c.detect(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = SmartCameraAnalytics(); [c.detect() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = SmartCameraAnalytics(); c.detect(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = SmartCameraAnalytics(); r = c.detect(); assert r["service"] == "smart-camera-analytics"
