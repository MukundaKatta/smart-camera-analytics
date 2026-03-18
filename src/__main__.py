"""CLI for smart-camera-analytics."""
import sys, json, argparse
from .core import SmartCameraAnalytics

def main():
    parser = argparse.ArgumentParser(description="Real-time video analytics with object detection, tracking, and behavior analysis")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = SmartCameraAnalytics()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.detect(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"smart-camera-analytics v0.1.0 — Real-time video analytics with object detection, tracking, and behavior analysis")

if __name__ == "__main__":
    main()
