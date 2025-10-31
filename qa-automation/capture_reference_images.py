#!/usr/bin/env python3
# Copyright 2024. The Tari Project
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
# disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Helper script to capture reference images for image recognition tests

This script helps you interactively capture UI element screenshots
for use in image recognition-based tests.
"""

import sys
import time
import pyautogui
from pathlib import Path


def main():
    """Interactive reference image capture"""
    print("=" * 60)
    print("Reference Image Capture Tool")
    print("=" * 60)
    print()
    print("This tool helps you capture reference images for testing.")
    print()
    print("Instructions:")
    print("1. Make sure Tari Universe is running and visible")
    print("2. Position your mouse over the UI element you want to capture")
    print("3. Press Enter when ready")
    print("4. You'll have 5 seconds to position your mouse")
    print("5. Click and drag to select the region to capture")
    print()
    print("Press Ctrl+C to exit at any time")
    print()
    
    images_dir = Path(__file__).parent / "images"
    images_dir.mkdir(exist_ok=True)
    
    suggested_images = [
        ("mining_button.png", "Main mining start/stop button"),
        ("cpu_tile.png", "CPU mining tile in sidebar"),
        ("gpu_tile.png", "GPU mining tile in sidebar"),
        ("settings_icon.png", "Settings icon/button"),
        ("logo.png", "Tari Universe logo"),
    ]
    
    print("Suggested images to capture:")
    for i, (filename, description) in enumerate(suggested_images, 1):
        print(f"  {i}. {filename} - {description}")
    print()
    
    try:
        while True:
            print("-" * 60)
            filename = input("Enter filename (or 'quit' to exit): ").strip()
            
            if filename.lower() in ['quit', 'exit', 'q']:
                break
            
            if not filename:
                continue
            
            if not filename.endswith('.png'):
                filename += '.png'
            
            filepath = images_dir / filename
            
            print(f"\nCapturing: {filename}")
            print("You have 5 seconds to position your mouse...")
            
            for i in range(5, 0, -1):
                print(f"  {i}...", end='\r')
                time.sleep(1)
            
            print("\nMove mouse to top-left corner and click...")
            print("Then drag to bottom-right corner and release")
            print("(Or press Ctrl+C to cancel this capture)")
            
            try:
                print("\nWaiting for region selection...")
                print("Alternative: Enter coordinates manually (x,y,width,height)")
                print("Or press Enter to use current mouse position for a 100x100 region")
                
                coords_input = input("Coordinates (or Enter to skip): ").strip()
                
                if coords_input:
                    try:
                        x, y, w, h = map(int, coords_input.split(','))
                        region = (x, y, w, h)
                    except ValueError:
                        print("Invalid coordinates format. Skipping...")
                        continue
                else:
                    x, y = pyautogui.position()
                    region = (x - 50, y - 50, 100, 100)
                    print(f"Using region around mouse: {region}")
                
                screenshot = pyautogui.screenshot(region=region)
                screenshot.save(str(filepath))
                
                print(f"✓ Saved: {filepath}")
                print(f"  Region: {region}")
                
            except KeyboardInterrupt:
                print("\nCapture cancelled")
                continue
            
    except KeyboardInterrupt:
        print("\n\nExiting...")
    
    print("\nCaptured images saved to:", images_dir)
    print("\nYou can now run image recognition tests:")
    print("  pytest tests/test_image_recognition.py -v")


if __name__ == "__main__":
    main()
