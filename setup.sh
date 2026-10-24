#!/bin/bash
pip install openai > /dev/null 2>&1
chmod +x guard.py

TARGET_DIR="/usr/local/bin"
if [ -w "$TARGET_DIR" ]; then
    cp guard.py "$TARGET_DIR/guard"
    echo "✅ 'guard' installed globally to $TARGET_DIR/guard"
else
    mkdir -p "$HOME/.local/bin"
    cp guard.py "$HOME/.local/bin/guard"
    echo "✅ 'guard' installed to $HOME/.local/bin/guard"
    export PATH="$HOME/.local/bin:$PATH"
fi
