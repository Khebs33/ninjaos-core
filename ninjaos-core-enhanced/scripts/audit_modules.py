# Audit script for verifying module registry completeness

import importlib
from pathlib import Path

def run_audit():
    try:
        mod = importlib.import_module("core.module_registry_80")
        registry = getattr(mod, "MODULE_REGISTRY", {})
        errors = []

        for module_id, module in registry.items():
            if not module.description:
                errors.append(f"{module_id} missing description")
            if not module.lenses:
                errors.append(f"{module_id} missing lenses")
            if not module.stress_points:
                errors.append(f"{module_id} missing stress points")

        print(f"✅ Found {len(registry)} modules.")
        if errors:
            print("❌ Issues found:")
            for e in errors:
                print(" -", e)
        else:
            print("✅ All modules look good.")
    except Exception as e:
        print("❌ Audit failed:", str(e))

if __name__ == "__main__":
    run_audit()
