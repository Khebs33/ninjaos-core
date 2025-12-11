#!/bin/bash
# macOS script to zip and sync to Google Drive

DATE=$(date +"%Y-%m-%d")
ZIP_FILE="ninjaos-backup-$DATE.zip"
SRC_DIR="$(pwd)"
DEST_DIR=~/Google\ Drive/NinjaOS/Backups

echo "🔄 Zipping project..."
zip -r $ZIP_FILE . -x "*.DS_Store" "*.pyc" "__pycache__/*"

echo "📁 Moving backup to Google Drive..."
mv $ZIP_FILE "$DEST_DIR"

echo "✅ Backup complete: $DEST_DIR/$ZIP_FILE"
