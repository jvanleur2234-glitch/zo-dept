#!/usr/bin/env python3
"""
Hermes QA Bridge — Reads failed/ folder, triggers Hermes self-evolution
$5/night via NVIDIA free credits
"""
import os, json, subprocess, datetime as dt
from pathlib import Path

FAILED = Path("/home/workspace/zo-dept/qa/failed")
REPORTS = Path("/home/workspace/zo-dept/qa/reports")
HERMES_SELF_EVO = Path("/home/workspace/hermes-agent-self-evolution")
SKILLS_DIR = Path("/home/workspace/solomon-skills")

NVIDIA_KEY = os.environ.get("NVIDIA_API_KEY", "")
EVOLUTION_CFG = Path("/home/workspace/zo-dept/qa/evolution_config.json")

def read_ev_cfg():
    with open(EVOLUTION_CFG) as f:
        return json.load(f)

def get_failed_bugs():
    if not FAILED.exists():
        return []
    return [f for f in FAILED.iterdir() if f.suffix == ".json"]

def trigger_hermes_evolution(skill_name: str, bug_report: dict, cfg: dict) -> dict:
    """
    Trigger Hermes self-evolution for a specific skill.
    Runs: python -m evolution.skills.evolve_skill --skill <name> --iterations 10
    """
    # Parse skill name from bug report
    skill_to_fix = bug_report.get("skill", skill_name)
    if not skill_to_fix:
        return {"status": "skip", "reason": "no skill specified in bug"}

    skill_path = SKILLS_DIR / skill_to_fix
    if not skill_path.exists():
        return {"status": "skip", "reason": f"skill not found: {skill_to_fix}"}

    report_file = REPORTS / f"evo_{skill_to_fix}_{dt.datetime.now().strftime('%Y%m%d_%H%M')}.txt"

    cmd = [
        "python3", "-m", "evolution.skills.evolve_skill",
        "--skill", skill_to_fix,
        "--iterations", str(cfg["iterations"]),
        "--eval-source", cfg["eval_source"],
        "--output", str(report_file),
    ]

    env = os.environ.copy()
    if NVIDIA_KEY:
        env["NVIDIA_API_KEY"] = NVIDIA_KEY

    try:
        result = subprocess.run(
            cmd,
            cwd=str(HERMES_SELF_EVO),
            env=env,
            capture_output=True,
            text=True,
            timeout=300,
        )
        return {
            "status": "done",
            "skill": skill_to_fix,
            "returncode": result.returncode,
            "stdout": result.stdout[:500],
            "stderr": result.stderr[-200:],
            "report": str(report_file),
            "cost_estimate": cfg["iterations"] * 0.5,  # ~$0.50/run at NVIDIA rates
        }
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "skill": skill_to_fix}
    except FileNotFoundError:
        return {"status": "skip", "reason": "evolution module not installed"}
    except Exception as e:
        return {"status": "error", "skill": skill_to_fix, "error": str(e)}

def run_qa_cycle():
    """Main QA cycle — read failures, trigger evolution, report."""
    cfg = read_ev_cfg()
    bugs = get_failed_bugs()
    results = []

    if not bugs:
        return {"status": "clean", "message": "No failures found. System passing."}

    print(f"[Hermes QA] Found {len(bugs)} failures. Triggering evolution...")

    for bug_file in bugs:
        try:
            with open(bug_file) as f:
                bug = json.load(f)

            skill = bug.get("skill", "unknown")
            test_name = bug.get("test", "unknown")
            print(f"  [→] Evolving skill: {skill} (from test: {test_name})")

            result = trigger_hermes_evolution(skill, bug, cfg)

            result["bug_file"] = str(bug_file)
            result["test_name"] = test_name
            results.append(result)

            # Move to fixed if evolved
            if result["status"] == "done":
                fixed_dir = Path("/home/workspace/zo-dept/qa/fixed")
                os.makedirs(fixed_dir, exist_ok=True)
                os.rename(bug_file, fixed_dir / bug_file.name)
                print(f"  [✓] {skill} evolved. Report: {result.get('report', 'N/A')}")
            else:
                print(f"  [!] {skill}: {result.get('status')} — {result.get('reason', result.get('error', ''))}")

        except Exception as e:
            print(f"  [ERROR] {bug_file.name}: {e}")

    return {
        "status": "cycle_complete",
        "bugs_found": len(bugs),
        "results": results,
        "total_cost_estimate": sum(r.get("cost_estimate", 0) for r in results),
    }

if __name__ == "__main__":
    result = run_qa_cycle()
    print("\n=== HERMES QA BRIDGE RESULT ===")
    print(json.dumps(result, indent=2))

    # Write report
    os.makedirs(REPORTS, exist_ok=True)
    report_path = REPORTS / f"qa_bridge_{dt.datetime.now().strftime('%Y%m%d_%H%M')}.json"
    with open(report_path, "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"\nReport saved: {report_path}")
