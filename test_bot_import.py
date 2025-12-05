#!/usr/bin/env python3
"""Test script that simulates running from bot directory"""
import sys
import os

# Simulate being in the bot directory
bot_dir = r'C:\Users\sa1nt\Documents\tess\projects\saint\bot'
os.chdir(bot_dir)
# The current directory is automatically added to sys.path when running a script
# But we need to make sure it's there for this test
if bot_dir not in sys.path:
    sys.path.insert(0, bot_dir)

print(f"Current directory: {os.getcwd()}")
print(f"Bot dir in sys.path: {bot_dir in sys.path}")
print(f"First few sys.path entries: {sys.path[:5]}")

print("\nImporting discord...")
try:
    import discord
    print(f"Discord module file: {discord.__file__}")
    print(f"VoiceProtocol available: {hasattr(discord, 'VoiceProtocol')}")
    if hasattr(discord, 'VoiceProtocol'):
        print(f"✓ VoiceProtocol: {discord.VoiceProtocol}")
    else:
        print("✗ VoiceProtocol NOT FOUND")
        print(f"Available Voice*: {[x for x in dir(discord) if 'Voice' in x]}")
        
    print("\nImporting wavelink...")
    import wavelink
    print(f"✓ Wavelink imported successfully! (version: {getattr(wavelink, '__version__', 'unknown')})")
except Exception as e:
    import traceback
    print(f"✗ Error: {e}")
    traceback.print_exc()

