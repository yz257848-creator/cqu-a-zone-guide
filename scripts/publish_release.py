#!/usr/bin/env python3
"""Create the v1.0 release and upload the skill zip as a release asset."""
import json
import mimetypes
import os
import pathlib
import urllib.request
import uuid

TOKEN = os.environ["GH_TOKEN"]
OWNER = "yz257848-creator"
REPO = "cqu-a-zone-guide"
ROOT = pathlib.Path(__file__).resolve().parent.parent
ZIP = ROOT / "cqu-a-zone-guide.zip"
NOTES = ROOT / ".release-notes.md"


def api(method, url, data=None, headers=None):
    h = {
        "Authorization": f"token {TOKEN}",
        "User-Agent": "workbuddy",
        "Accept": "application/vnd.github+json",
    }
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


def main():
    body = json.dumps({
        "tag_name": "v1.0",
        "name": "v1.0 首版",
        "body": NOTES.read_text(encoding="utf-8"),
        "draft": False,
        "prerelease": False,
    }).encode("utf-8")

    status, rel = api(
        "POST",
        f"https://api.github.com/repos/{OWNER}/{REPO}/releases",
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    if status not in (200, 201):
        print(f"release create failed ({status}): {rel}")
        return 1

    upload_url = rel["upload_url"].split("{")[0]
    print(f"release created: {rel['html_url']}")

    payload = ZIP.read_bytes()
    ctype = mimetypes.guess_type(ZIP.name)[0] or "application/zip"
    status, asset = api(
        "POST",
        f"{upload_url}?name={ZIP.name}",
        data=payload,
        headers={
            "Content-Type": ctype,
            "Content-Length": str(len(payload)),
        },
    )
    if status not in (200, 201):
        print(f"asset upload failed ({status}): {asset}")
        return 1

    print(f"asset uploaded: {asset['browser_download_url']}")
    print(f"size: {asset['size']:,} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
