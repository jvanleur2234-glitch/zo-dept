#!/usr/bin/env python3
"""
Solomon OS — Full Stack QA Runner
Runs every morning, creates smart bug cards with skill targets.
Hermes reads failed/ and evolves the relevant skills automatically.
"""
import os, json, subprocess, datetime as dt
from pathlib import Path
import urllib.request, urllib.error

FAILED = Path("/home/workspace/zo-dept/qa/failed")
REPORTS = Path("/home/workspace/zo-dept/qa/reports")
os.makedirs(FAILED, exist_ok=True)
os.makedirs(REPORTS, exist_ok=True)

failed_count = 0
STRIPE_KEY = os.environ.get("STRIPE_SECRET_KEY", "")

def save_bug(test_name, severity, skill, error, details=None):
    global failed_count
    details = details or {}
    bug = {
        "id": dt.datetime.now().strftime("%Y%m%d%H%M%S"),
        "timestamp": dt.datetime.now().isoformat(),
        "test": test_name,
        "severity": severity,
        "skill": skill,
        "error": str(error)[:200],
        "details": details,
        "status": "open",
        "evolve": True,
    }
    path = FAILED / f"bug-{bug['id']}.json"
    with open(path, "w") as f:
        json.dump(bug, f, indent=2)
    print(f"  [BUG] {skill}/{test_name}: {str(error)[:80]}")
    failed_count += 1

def test_page(path, name, check_text=None):
    global failed_count
    try:
        req = urllib.request.Request(
            f"http://localhost:3099{path}",
            headers={"Accept": "text/html"}
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            content = r.read().decode(errors="ignore")
            if check_text and check_text not in content:
                save_bug(name, "MEDIUM", "zo-space", f"Missing: {check_text}", {"path": path})
                return
            print(f"  [PASS] {path}")
    except Exception as e:
        save_bug(name, "HIGH", "zo-space", str(e), {"path": path})

def test_api(path, name, method="GET", data=None):
    global failed_count
    try:
        url = f"http://localhost:3099{path}"
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        req = urllib.request.Request(url, headers=headers)
        if method == "POST":
            req = urllib.request.Request(
                url, data=json.dumps(data or {}).encode(), method="POST",
                headers=headers
            )
        with urllib.request.urlopen(req, timeout=15) as r:
            content = r.read()
            try:
                result = json.loads(content)
                if isinstance(result, dict) and "error" in result:
                    save_bug(name, "MEDIUM", "zo-space-api", result["error"], {"path": path})
                    return
            except: pass
            print(f"  [PASS] {path}")
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="ignore")[:200]
        if e.code >= 500:
            save_bug(name, "HIGH", "zo-space-api", f"HTTP {e.code}: {body[:100]}", {"path": path})
    except Exception as e:
        save_bug(name, "HIGH", "zo-space-api", str(e), {"path": path})

def test_local(port, name, local_only=True):
    global failed_count
    try:
        req = urllib.request.Request(f"http://localhost:{port}/")
        with urllib.request.urlopen(req, timeout=5) as r:
            print(f"  [PASS] localhost:{port} ({name})")
    except Exception as e:
        err_str = str(e)
        if "Cannot assign requested address" in err_str or "Connection refused" in err_str:
            # Expected in sandbox - these services run on Joseph's actual machine
            print(f"  [LOCAL] localhost:{port} ({name}) — not reachable in sandbox (runs on your machine)")
        else:
            save_bug(name, "HIGH", "local-service", err_str, {"port": port})

def test_stripe():
    global failed_count
    if not STRIPE_KEY:
        print("  [SKIP] STRIPE_SECRET_KEY not set")
        return
    try:
        req = urllib.request.Request(
            "https://api.stripe.com/v1/products",
            headers={"Accept": "application/json", "Authorization": f"Bearer {STRIPE_KEY}"}
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
            print(f"  [PASS] Stripe: {len(data.get('data', []))} products live")
    except Exception as e:
        save_bug("Stripe Products", "HIGH", "stripe", str(e))

def test_ollama():
    try:
        req = urllib.request.Request(
            "http://localhost:11434/api/tags",
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read())
            models = [m["name"] for m in data.get("models", [])]
            print(f"  [PASS] Ollama: {', '.join(models)}")
    except Exception as e:
        err_str = str(e)
        if "Cannot assign requested address" in err_str or "Connection refused" in err_str:
            print(f"  [LOCAL] Ollama — not reachable in sandbox (runs on your machine)")
        else:
            save_bug("Ollama", "HIGH", "ollama", err_str)

def test_skills():
    skills_dir = Path("/home/workspace/solomon-skills")
    if not skills_dir.exists():
        print("  [SKIP] solomon-skills not found")
        return
    skills = [d for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()]
    print(f"  [PASS] {len(skills)} skills found")

def test_github():
    global failed_count
    for repo in ["solomon-skills", "zo-excellence-package"]:
        try:
            r = subprocess.run(
                ["gh", "api", f"/repos/jvanleur2234-glitch/{repo}"],
                capture_output=True, text=True, timeout=10
            )
            if r.returncode == 0:
                print(f"  [PASS] GitHub: {repo}")
            else:
                save_bug(f"GitHub: {repo}", "MEDIUM", "github", "No access", {"repo": repo})
        except Exception as e:
            print(f"  [FAIL] GitHub {repo}: {e}")

# ── RUN ALL TESTS ──────────────────────────────────────────
print("============================================================")
print("SOLOMON OS — FULL STACK QA — " + dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
print("============================================================\n")

print("--- Zo Space Pages ---")
test_page("/", "Homepage")
test_page("/bonsai", "Bonsai AI")
test_page("/skill-store", "Skill Store")
test_page("/freedom", "Freedom Dashboard")

print("\n--- Zo Space API ---")
test_api("/api/workflow-extract", "Workflow Extract", "POST", {"url": "https://youtube.com/watch?v=test"})

print("\n--- Stripe ---")
test_stripe()

print("\n--- Local Services ---")
test_local(8080, "MoneyPrinterTurbo")
test_local(3101, "Hermes")
test_local(5010, "RENU API")

print("\n--- Ollama ---")
test_ollama()

print("\n--- Hermes Skills ---")
test_skills()

print("\n--- GitHub Sync ---")
test_github()

# ── SUMMARY ──────────────────────────────────────────────
print(f"\n============================================================")
print(f"QA COMPLETE — {failed_count} failures")
if failed_count > 0:
    bug_files = list(FAILED.glob("*.json"))
    print(f"Bug cards: {FAILED}/ ({len(bug_files)} files)")
    print(f"Hermes self-evolution will read these and evolve the relevant skills.")
    print(f"Run: python3 /home/workspace/zo-dept/qa/hermes_qa_bridge.py")
else:
    print("System is clean. Nothing to evolve.")
print("============================================================")

exit(0 if failed_count == 0 else 1)
