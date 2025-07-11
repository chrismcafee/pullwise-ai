#!/bin/bash

set -euo pipefail

REPO="chrismcafee/pullwise-ai"
VERSION=$(git describe --tags --abbrev=0)
TARBALL_URL="https://github.com/$REPO/releases/download/$VERSION/pullwise-macos.tar.gz"
TARBALL_PATH="/tmp/pullwise.tar.gz"

echo "Downloading release tarball..."
curl -L "$TARBALL_URL" -o "$TARBALL_PATH"

SHA256=$(shasum -a 256 "$TARBALL_PATH" | awk '{print $1}')

cat > Formula/pullwise.rb <<EOF
class Pullwise < Formula
  desc "AI-powered pull request reviewer CLI"
  homepage "https://github.com/$REPO"
  url "$TARBALL_URL"
  sha256 "$SHA256"
  version "$VERSION"

  def install
    bin.install "pullwise"
  end
end
EOF

echo "Updated Formula/pullwise.rb with SHA256: $SHA256"
